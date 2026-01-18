"""
Day 1 - Homework Solutions: Reference Counting & Memory Management

Complete these exercises to master Python's internals.
"""

import sys
import gc
import weakref
from typing import Dict, Optional, Any
import time


# ============================================================================
# HOMEWORK 1: Refcount Detective
# ============================================================================

class Node:
    """Simple linked list node for demonstrating reference cycles."""
    
    def __init__(self, value: int):
        self.value = value
        self.next: Optional['Node'] = None
        print(f"  ✓ Created Node({value})")
    
    def __del__(self):
        print(f"  🗑️  Deleting Node({self.value})")


def homework_1_circular_list():
    """
    TASK: Demonstrate circular reference and garbage collection.
    
    Steps:
    1. Create a circular linked list (3 nodes)
    2. Show refcounts at each step
    3. Delete all references
    4. Prove that gc.collect() is needed to free memory
    """
    print("\n" + "="*70)
    print("HOMEWORK 1: Refcount Detective - Circular References")
    print("="*70)
    
    # TODO: Complete this function
    # Hints:
    # - Use sys.getrefcount() to check reference counts
    # - Create Node instances and link them in a circle
    # - Use gc.get_objects() to count live objects
    # - Call gc.collect() to break cycles
    
    print("\n[Step 1] Creating nodes...")
    # YOUR CODE HERE
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    print(f"\nRefCounts after creation:")
    print(f"  node1: {sys.getrefcount(node1) - 1}")
    print(f"  node2: {sys.getrefcount(node2) - 1}")
    print(f"  node3: {sys.getrefcount(node3) - 1}")
    
    print("\n[Step 2] Creating circular links...")
    # YOUR CODE HERE
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Creates cycle!
    
    print(f"\nRefCounts after linking:")
    print(f"  node1: {sys.getrefcount(node1) - 1} (increased because node3.next points to it)")
    print(f"  node2: {sys.getrefcount(node2) - 1}")
    print(f"  node3: {sys.getrefcount(node3) - 1}")
    
    print("\n[Step 3] Counting objects before deletion...")
    before_count = len([obj for obj in gc.get_objects() if isinstance(obj, Node)])
    print(f"  Node objects in memory: {before_count}")
    
    print("\n[Step 4] Deleting all references...")
    # YOUR CODE HERE
    del node1, node2, node3
    
    print("\n[Step 5] Checking if objects were freed...")
    after_del_count = len([obj for obj in gc.get_objects() if isinstance(obj, Node)])
    print(f"  Node objects in memory: {after_del_count}")
    
    if after_del_count == before_count:
        print("  🚨 Objects NOT freed - circular reference prevents deletion!")
    
    print("\n[Step 6] Running gc.collect()...")
    # YOUR CODE HERE
    collected = gc.collect()
    
    after_gc_count = len([obj for obj in gc.get_objects() if isinstance(obj, Node)])
    print(f"  Collected {collected} objects")
    print(f"  Node objects in memory: {after_gc_count}")
    
    if after_gc_count == 0:
        print("  ✅ All Node objects freed by garbage collector!")
    
    print("\n" + "="*70)


# ============================================================================
# HOMEWORK 2: AWS SSM Parameter Cache
# ============================================================================

class SSMParameterCache:
    """
    LRU cache for AWS SSM parameters with TTL.
    
    Requirements:
    - Cache up to max_size parameters
    - Each cached value expires after ttl_seconds
    - Implement LRU eviction when cache is full
    - Prevent memory leaks in long-running containers
    """
    
    def __init__(self, max_size: int = 100, ttl_seconds: int = 300):
        """
        Initialize the cache.
        
        Args:
            max_size: Maximum number of parameters to cache
            ttl_seconds: Time-to-live for cached values
        """
        from collections import OrderedDict
        
        self._cache: OrderedDict[str, Dict[str, Any]] = OrderedDict()
        self._max_size = max_size
        self._ttl = ttl_seconds
        
        # Metrics
        self._hits = 0
        self._misses = 0
    
    def get(self, parameter_name: str) -> Optional[str]:
        """
        Get parameter from cache or return None if not found/expired.
        
        Args:
            parameter_name: SSM parameter name
        
        Returns:
            Parameter value or None
        """
        # TODO: Implement this method
        # Steps:
        # 1. Check if parameter exists in cache
        # 2. Check if it's expired (current_time - cached_time > ttl)
        # 3. If expired, remove from cache and return None
        # 4. If valid, move to end (mark as recently used) and return value
        # 5. Update hit/miss metrics
        
        if parameter_name not in self._cache:
            self._misses += 1
            return None
        
        entry = self._cache[parameter_name]
        
        # Check if expired
        if time.time() - entry['timestamp'] > self._ttl:
            del self._cache[parameter_name]
            self._misses += 1
            return None
        
        # Mark as recently used
        self._cache.move_to_end(parameter_name)
        self._hits += 1
        
        return entry['value']
    
    def put(self, parameter_name: str, value: str) -> None:
        """
        Add/update parameter in cache.
        
        Args:
            parameter_name: SSM parameter name
            value: Parameter value
        """
        # TODO: Implement this method
        # Steps:
        # 1. If parameter exists, update it and move to end
        # 2. If new parameter, add to cache
        # 3. If cache is full, evict oldest (LRU)
        # 4. Store value with timestamp
        
        if parameter_name in self._cache:
            # Update existing
            self._cache[parameter_name] = {
                'value': value,
                'timestamp': time.time()
            }
            self._cache.move_to_end(parameter_name)
        else:
            # Add new
            if len(self._cache) >= self._max_size:
                # Evict oldest
                self._cache.popitem(last=False)
            
            self._cache[parameter_name] = {
                'value': value,
                'timestamp': time.time()
            }
    
    def evict_expired(self) -> int:
        """
        Remove all expired entries from cache.
        
        Returns:
            Number of entries evicted
        """
        # TODO: Implement this method
        now = time.time()
        to_remove = [
            key for key, val in self._cache.items()
            if now - val['timestamp'] > self._ttl
        ]
        
        for key in to_remove:
            del self._cache[key]
        
        return len(to_remove)
    
    def get_stats(self) -> Dict[str, int]:
        """Get cache statistics."""
        return {
            'size': len(self._cache),
            'max_size': self._max_size,
            'hits': self._hits,
            'misses': self._misses,
            'hit_rate': self._hits / (self._hits + self._misses) if (self._hits + self._misses) > 0 else 0.0
        }
    
    def clear(self) -> None:
        """Clear all cached entries."""
        self._cache.clear()
        self._hits = 0
        self._misses = 0


def homework_2_ssm_cache_test():
    """Test the SSM parameter cache."""
    print("\n" + "="*70)
    print("HOMEWORK 2: AWS SSM Parameter Cache")
    print("="*70)
    
    cache = SSMParameterCache(max_size=5, ttl_seconds=2)
    
    print("\n[Test 1] Adding parameters...")
    cache.put('/app/db/host', 'db.example.com')
    cache.put('/app/db/port', '5432')
    cache.put('/app/api/key', 'secret-key-123')
    
    print(f"Cache stats: {cache.get_stats()}")
    
    print("\n[Test 2] Cache hits...")
    assert cache.get('/app/db/host') == 'db.example.com'
    assert cache.get('/app/db/port') == '5432'
    
    print(f"Cache stats: {cache.get_stats()}")
    
    print("\n[Test 3] Cache miss...")
    assert cache.get('/nonexistent') is None
    
    print(f"Cache stats: {cache.get_stats()}")
    
    print("\n[Test 4] LRU eviction (max_size=5)...")
    cache.put('/param1', 'value1')
    cache.put('/param2', 'value2')
    cache.put('/param3', 'value3')  # Should evict oldest
    
    # Oldest should be evicted
    oldest = cache.get('/app/db/host')
    print(f"Oldest parameter still in cache: {oldest is not None}")
    
    print(f"Cache stats: {cache.get_stats()}")
    
    print("\n[Test 5] TTL expiration (ttl=2 seconds)...")
    cache.put('/temp/value', 'expires-soon')
    print("Waiting 3 seconds for expiration...")
    time.sleep(3)
    
    expired_value = cache.get('/temp/value')
    print(f"Expired value: {expired_value} (should be None)")
    
    evicted = cache.evict_expired()
    print(f"Evicted {evicted} expired entries")
    
    print(f"\nFinal cache stats: {cache.get_stats()}")
    print("="*70)


# ============================================================================
# HOMEWORK 3: Benchmark List vs Tuple vs Array
# ============================================================================

def homework_3_data_structure_benchmark():
    """
    Benchmark different data structures for DevOps use cases.
    
    Scenarios:
    - Storing 1 million EC2 instance IDs
    - Accessing elements by index
    - Iterating through all elements
    """
    import timeit
    import array
    
    print("\n" + "="*70)
    print("HOMEWORK 3: Data Structure Performance Comparison")
    print("="*70)
    
    n = 1_000_000
    
    # Test 1: Creation time
    print(f"\n[Test 1] Creating {n:,} integers...")
    
    list_time = timeit.timeit(
        lambda: list(range(n)),
        number=10
    ) / 10
    
    tuple_time = timeit.timeit(
        lambda: tuple(range(n)),
        number=10
    ) / 10
    
    array_time = timeit.timeit(
        lambda: array.array('i', range(n)),
        number=10
    ) / 10
    
    print(f"  List:  {list_time:.4f}s")
    print(f"  Tuple: {tuple_time:.4f}s")
    print(f"  Array: {array_time:.4f}s")
    print(f"  Fastest: {'Array' if array_time < min(list_time, tuple_time) else 'Tuple' if tuple_time < list_time else 'List'}")
    
    # Test 2: Memory usage
    print(f"\n[Test 2] Memory usage...")
    
    lst = list(range(n))
    tpl = tuple(range(n))
    arr = array.array('i', range(n))
    
    print(f"  List:  {sys.getsizeof(lst) / 1024 / 1024:.2f} MB")
    print(f"  Tuple: {sys.getsizeof(tpl) / 1024 / 1024:.2f} MB")
    print(f"  Array: {sys.getsizeof(arr) / 1024 / 1024:.2f} MB")
    
    # Test 3: Random access
    print(f"\n[Test 3] Random access (1M lookups)...")
    
    import random
    indices = [random.randint(0, n-1) for _ in range(1_000_000)]
    
    list_access = timeit.timeit(
        lambda: [lst[i] for i in indices[:1000]],
        number=1000
    ) / 1000
    
    tuple_access = timeit.timeit(
        lambda: [tpl[i] for i in indices[:1000]],
        number=1000
    ) / 1000
    
    array_access = timeit.timeit(
        lambda: [arr[i] for i in indices[:1000]],
        number=1000
    ) / 1000
    
    print(f"  List:  {list_access*1000:.4f}ms")
    print(f"  Tuple: {tuple_access*1000:.4f}ms")
    print(f"  Array: {array_access*1000:.4f}ms")
    
    # Test 4: Iteration
    print(f"\n[Test 4] Full iteration...")
    
    list_iter = timeit.timeit(
        lambda: sum(lst),
        number=10
    ) / 10
    
    tuple_iter = timeit.timeit(
        lambda: sum(tpl),
        number=10
    ) / 10
    
    array_iter = timeit.timeit(
        lambda: sum(arr),
        number=10
    ) / 10
    
    print(f"  List:  {list_iter:.4f}s")
    print(f"  Tuple: {tuple_iter:.4f}s")
    print(f"  Array: {array_iter:.4f}s")
    
    print("\n" + "="*70)
    print("RECOMMENDATIONS FOR DEVOPS:")
    print("  - Use list for: Mutable data, mixed types")
    print("  - Use tuple for: Immutable data, dict keys, slightly less memory")
    print("  - Use array for: Large numeric datasets (50-70% less memory)")
    print("="*70)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("DAY 1 - HOMEWORK EXERCISES")
    print("="*70)
    
    try:
        # Homework 1
        homework_1_circular_list()
        input("\nPress Enter to continue to Homework 2...")
        
        # Homework 2
        homework_2_ssm_cache_test()
        input("\nPress Enter to continue to Homework 3...")
        
        # Homework 3
        homework_3_data_structure_benchmark()
        
        print("\n" + "="*70)
        print("✅ All homework exercises completed!")
        print("="*70)
        print("\nNext steps:")
        print("1. Review the code and understand each concept")
        print("2. Try modifying parameters and observe the effects")
        print("3. Apply these patterns in your own DevOps scripts")
        print("4. Read the recommended CPython source files")
        print("="*70)
        
    except KeyboardInterrupt:
        print("\n\nHomework interrupted by user.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
