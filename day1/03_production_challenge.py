"""
Day 1 - Production Challenge: Debug the K8s Memory Leak

This file contains a broken Kubernetes log aggregator that leaks memory.
Your task is to identify ALL the issues and fix them.
"""

import time
import gc
import sys
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


# Mock Kubernetes client (simulates real kubernetes.client)
class MockPodMetadata:
    def __init__(self, name: str, namespace: str, uid: str):
        self.name = name
        self.namespace = namespace
        self.uid = uid
        self.owner_references = [self]  # 🚨 Circular reference!


class MockPodStatus:
    def __init__(self, phase: str):
        self.phase = phase


class MockPod:
    def __init__(self, name: str, namespace: str):
        self.metadata = MockPodMetadata(name, namespace, f"uid-{name}")
        self.status = MockPodStatus("Running")


class MockPodList:
    def __init__(self, pods: List[MockPod]):
        self.items = pods


class MockV1Api:
    """Simulates Kubernetes CoreV1Api."""
    
    def __init__(self):
        self._pods = []
        self._deleted_pods = set()
    
    def create_pod(self, namespace: str, name: str):
        """Simulate pod creation."""
        pod = MockPod(name, namespace)
        self._pods.append(pod)
        return pod
    
    def delete_pod(self, namespace: str, name: str):
        """Simulate pod deletion."""
        self._deleted_pods.add((namespace, name))
        self._pods = [p for p in self._pods 
                     if not (p.metadata.namespace == namespace and p.metadata.name == name)]
    
    def list_namespaced_pod(self, namespace: str) -> MockPodList:
        """Simulate listing pods."""
        namespace_pods = [p for p in self._pods if p.metadata.namespace == namespace]
        return MockPodList(namespace_pods)
    
    def read_namespaced_pod_log(self, name: str, namespace: str) -> str:
        """Simulate reading pod logs."""
        return f"Log output from {namespace}/{name}\n" * 100  # 🚨 Large strings!


# ============================================================================
# 🚨 BROKEN CODE - Find and fix all issues!
# ============================================================================

class LogAggregator:
    """
    TASK: This class has multiple memory leaks. Find them all!
    
    Issues to find:
    1. Unbounded cache growth
    2. Circular references
    3. Large objects stored unnecessarily
    4. Deleted pods not removed from cache
    5. No garbage collection
    
    Run this for 1000 iterations and watch memory grow!
    """
    
    def __init__(self):
        self._api = MockV1Api()
        self.logs = []  # 🚨 Issue #1: What's wrong here?
        self.pod_cache = {}  # 🚨 Issue #2: What's wrong here?
    
    def aggregate_logs(self, namespace: str) -> List[Dict]:
        """
        Aggregate logs from all pods in namespace.
        
        🚨 This method has several memory leaks!
        """
        pods = self._api.list_namespaced_pod(namespace)
        
        for pod in pods.items:
            log = self._api.read_namespaced_pod_log(
                name=pod.metadata.name,
                namespace=namespace
            )
            
            # 🚨 Issue #3: Storing full pod object
            # 🚨 Issue #4: Never cleaning up
            # 🚨 Issue #5: Storing huge log strings
            self.logs.append({
                'pod': pod.metadata.name,
                'log': log,  # Full log text!
                'pod_object': pod,  # Full pod object with circular refs!
                'timestamp': datetime.now()
            })
            
            self.pod_cache[pod.metadata.name] = {
                'full_pod': pod,  # 🚨 More circular references
                'logs': [log],  # 🚨 Duplicated data
                'history': []  # 🚨 Growing list
            }
        
        return self.logs
    
    def get_memory_usage(self) -> Dict[str, float]:
        """Get current memory usage."""
        import psutil
        process = psutil.Process()
        mem_info = process.memory_info()
        
        return {
            'rss_mb': mem_info.rss / 1024 / 1024,
            'vms_mb': mem_info.vms / 1024 / 1024,
            'logs_count': len(self.logs),
            'cache_size': len(self.pod_cache)
        }


# ============================================================================
# ✅ FIXED CODE - Production-ready implementation
# ============================================================================

@dataclass
class PodLogEntry:
    """Lightweight pod log metadata (no full objects)."""
    pod_name: str
    namespace: str
    log_lines: int
    error_count: int
    timestamp: float
    
    def __post_init__(self):
        """Ensure no circular references."""
        # Only store primitive types!
        assert isinstance(self.pod_name, str)
        assert isinstance(self.namespace, str)
        assert isinstance(self.log_lines, int)


class LogAggregatorFixed:
    """
    Production-ready log aggregator with:
    - Bounded memory usage
    - LRU eviction
    - No circular references
    - Periodic garbage collection
    - Metrics tracking
    """
    
    def __init__(self, max_cache_size: int = 1000, max_logs: int = 10000):
        from collections import OrderedDict
        
        self._api = MockV1Api()
        self._log_entries: OrderedDict[str, PodLogEntry] = OrderedDict()
        self._max_cache_size = max_cache_size
        self._max_logs = max_logs
        
        # Metrics
        self._total_processed = 0
        self._gc_runs = 0
        self._evictions = 0
    
    def aggregate_logs(self, namespace: str) -> List[PodLogEntry]:
        """
        Aggregate logs with proper memory management.
        """
        pods = self._api.list_namespaced_pod(namespace)
        results = []
        
        for pod in pods.items:
            # Get log but don't store the full string!
            log = self._api.read_namespaced_pod_log(
                name=pod.metadata.name,
                namespace=namespace
            )
            
            # Extract only what we need
            log_lines = log.count('\n')
            error_count = log.lower().count('error')
            
            # Create lightweight entry
            entry = PodLogEntry(
                pod_name=pod.metadata.name,
                namespace=namespace,
                log_lines=log_lines,
                error_count=error_count,
                timestamp=time.time()
            )
            
            # LRU cache management
            key = f"{namespace}/{pod.metadata.name}"
            
            if key in self._log_entries:
                self._log_entries.move_to_end(key)
            else:
                if len(self._log_entries) >= self._max_cache_size:
                    self._log_entries.popitem(last=False)
                    self._evictions += 1
            
            self._log_entries[key] = entry
            results.append(entry)
            
            # Don't keep reference to pod object!
            del pod
            del log
        
        self._total_processed += len(results)
        
        # Periodic GC
        if self._total_processed % 100 == 0:
            self._run_gc()
        
        return results
    
    def handle_pod_deletion(self, namespace: str, pod_name: str):
        """Explicitly handle pod deletions."""
        key = f"{namespace}/{pod_name}"
        if key in self._log_entries:
            del self._log_entries[key]
    
    def _run_gc(self):
        """Force garbage collection to break cycles."""
        before = len(gc.get_objects())
        collected = gc.collect()
        after = len(gc.get_objects())
        
        self._gc_runs += 1
        
        if collected > 0:
            print(f"  [GC] Collected {collected} objects "
                  f"(before: {before}, after: {after})")
    
    def get_memory_usage(self) -> Dict[str, float]:
        """Get current memory usage."""
        import psutil
        process = psutil.Process()
        mem_info = process.memory_info()
        
        return {
            'rss_mb': mem_info.rss / 1024 / 1024,
            'vms_mb': mem_info.vms / 1024 / 1024,
            'cache_size': len(self._log_entries),
            'total_processed': self._total_processed,
            'gc_runs': self._gc_runs,
            'evictions': self._evictions
        }


# ============================================================================
# TEST & COMPARISON
# ============================================================================

def simulate_workload(aggregator, api: MockV1Api, iterations: int = 100):
    """Simulate realistic pod lifecycle."""
    namespace = "production"
    
    for i in range(iterations):
        # Create some pods
        for j in range(10):
            api.create_pod(namespace, f"pod-{i}-{j}")
        
        # Aggregate logs
        aggregator.aggregate_logs(namespace)
        
        # Delete some pods (simulating pod churn)
        if i > 0:
            for j in range(5):
                pod_name = f"pod-{i-1}-{j}"
                api.delete_pod(namespace, pod_name)
                
                # Fixed version needs explicit deletion handling
                if isinstance(aggregator, LogAggregatorFixed):
                    aggregator.handle_pod_deletion(namespace, pod_name)
        
        # Print memory every 10 iterations
        if i % 10 == 0:
            mem = aggregator.get_memory_usage()
            print(f"  Iteration {i:3d} | "
                  f"Memory: {mem['rss_mb']:6.2f} MB | "
                  f"Cache: {mem.get('cache_size', 'N/A'):4}")


def run_comparison():
    """Compare broken vs fixed implementations."""
    print("\n" + "="*70)
    print("PRODUCTION CHALLENGE: Memory Leak Debugging")
    print("="*70)
    
    print("\n[TEST 1] Running BROKEN implementation...")
    print("Watch memory grow unbounded! 🚨\n")
    
    try:
        import psutil
    except ImportError:
        print("Installing psutil for memory monitoring...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
        import psutil
    
    broken_api = MockV1Api()
    broken_agg = LogAggregator()
    
    initial_mem = psutil.Process().memory_info().rss / 1024 / 1024
    print(f"Initial memory: {initial_mem:.2f} MB\n")
    
    simulate_workload(broken_agg, broken_api, iterations=50)
    
    final_mem = broken_agg.get_memory_usage()
    print(f"\nFinal memory: {final_mem['rss_mb']:.2f} MB")
    print(f"Memory grown: {final_mem['rss_mb'] - initial_mem:.2f} MB")
    print(f"Logs collected: {final_mem['logs_count']}")
    print(f"Cache size: {final_mem['cache_size']}")
    
    # Clean up
    del broken_agg
    del broken_api
    gc.collect()
    
    print("\n" + "-"*70)
    print("\n[TEST 2] Running FIXED implementation...")
    print("Memory should remain bounded! ✅\n")
    
    fixed_api = MockV1Api()
    fixed_agg = LogAggregatorFixed(max_cache_size=100, max_logs=1000)
    
    initial_mem = psutil.Process().memory_info().rss / 1024 / 1024
    print(f"Initial memory: {initial_mem:.2f} MB\n")
    
    simulate_workload(fixed_agg, fixed_api, iterations=50)
    
    final_mem = fixed_agg.get_memory_usage()
    print(f"\nFinal memory: {final_mem['rss_mb']:.2f} MB")
    print(f"Memory grown: {final_mem['rss_mb'] - initial_mem:.2f} MB")
    print(f"Cache size: {final_mem['cache_size']} (max: 100)")
    print(f"Total processed: {final_mem['total_processed']}")
    print(f"Evictions: {final_mem['evictions']}")
    print(f"GC runs: {final_mem['gc_runs']}")
    
    print("\n" + "="*70)
    print("ANALYSIS:")
    print("="*70)
    print("\nIssues in broken implementation:")
    print("1. ❌ Unbounded 'logs' list - grows forever")
    print("2. ❌ Stores full pod objects - circular references")
    print("3. ❌ Stores full log strings - huge memory usage")
    print("4. ❌ Never removes deleted pods")
    print("5. ❌ No garbage collection")
    print("6. ❌ No LRU eviction")
    print("\nFixes in production-ready version:")
    print("1. ✅ LRU cache with max size")
    print("2. ✅ Only stores primitives (no circular refs)")
    print("3. ✅ Extract metadata, discard logs")
    print("4. ✅ Explicit deletion handling")
    print("5. ✅ Periodic gc.collect()")
    print("6. ✅ Bounded memory usage")
    print("="*70)


if __name__ == "__main__":
    run_comparison()
