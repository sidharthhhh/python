"""
Day 1 - Code Examples: Reference Counting Explorer

This script demonstrates Python's reference counting mechanism
and helps you understand object lifetime management.
"""

import sys
import gc
from typing import Any


class ReferenceCountMonitor:
    """Monitor reference counts of objects in real-time."""
    
    def __init__(self):
        self.tracked_objects = {}
    
    def track(self, name: str, obj: Any) -> None:
        """Register an object for tracking."""
        # Store object ID to check later
        self.tracked_objects[name] = (id(obj), obj)
    
    def show_counts(self) -> None:
        """Display current reference counts."""
        print("\n" + "="*60)
        print("REFERENCE COUNT STATUS")
        print("="*60)
        
        for name, (obj_id, obj) in list(self.tracked_objects.items()):
            try:
                # Check if object still exists by trying to get refcount
                count = sys.getrefcount(obj) - 2  # Subtract temp ref and our storage
                print(f"{name:20s} | RefCount: {count:3d} | Type: {type(obj).__name__}")
            except:
                print(f"{name:20s} | [DELETED]")
                del self.tracked_objects[name]
        
        print("="*60 + "\n")


def demo_1_basic_refcount():
    """Demonstrate basic reference counting behavior."""
    print("\n### DEMO 1: Basic Reference Counting ###\n")
    
    monitor = ReferenceCountMonitor()
    
    # Create an object
    x = [1, 2, 3]
    monitor.track("x (initial)", x)
    monitor.show_counts()  # Should be 1
    
    # Create another reference
    y = x
    monitor.show_counts()  # Should be 2
    
    # Create more references
    z = x
    my_list = [x, x, x]
    monitor.show_counts()  # Should be 5 (z + 3 in list + original)
    
    # Delete references
    del y
    monitor.show_counts()  # Should decrease by 1
    
    del z
    del my_list
    monitor.show_counts()  # Should be back to 1
    
    del x
    monitor.show_counts()  # Object should be deleted


def demo_2_circular_reference():
    """Show how circular references prevent deallocation."""
    print("\n### DEMO 2: Circular Reference Problem ###\n")
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
        
        def __del__(self):
            print(f"  🗑️  Node({self.value}) is being deleted")
    
    print("Creating circular linked list...")
    
    # Create circular reference
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Creates cycle!
    
    print(f"RefCount node1: {sys.getrefcount(node1) - 1}")
    print(f"RefCount node2: {sys.getrefcount(node2) - 1}")
    print(f"RefCount node3: {sys.getrefcount(node3) - 1}")
    
    print("\nDeleting all references...")
    del node1, node2, node3
    
    print("After del - objects should still exist (cycle prevents deletion)")
    print(f"Garbage objects: {len(gc.get_objects())}")
    
    print("\nRunning gc.collect()...")
    collected = gc.collect()
    print(f"Collected {collected} objects")


def demo_3_aws_policy_mutable_default():
    """Real-world bug: mutable default arguments."""
    print("\n### DEMO 3: Mutable Default Argument Bug ###\n")
    
    # ❌ WRONG - Bug that affects multiple calls
    def create_iam_policy_wrong(actions, resources=[]):
        """DO NOT USE - Demonstrates common bug."""
        policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Action": actions,
                "Resource": resources
            }]
        }
        return policy
    
    # ✅ CORRECT - Proper implementation
    def create_iam_policy_correct(actions, resources=None):
        """Proper implementation with None default."""
        if resources is None:
            resources = []
        
        policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Action": actions,
                "Resource": resources
            }]
        }
        return policy
    
    print("Using WRONG implementation:")
    policy1_wrong = create_iam_policy_wrong(["s3:GetObject"])
    policy2_wrong = create_iam_policy_wrong(["s3:PutObject"])
    
    # Add resource to first policy
    policy1_wrong['Statement'][0]['Resource'].append("arn:aws:s3:::bucket1/*")
    
    print(f"Policy 1 Resources: {policy1_wrong['Statement'][0]['Resource']}")
    print(f"Policy 2 Resources: {policy2_wrong['Statement'][0]['Resource']}")
    print("🚨 BUG: Both share same list!\n")
    
    print("Using CORRECT implementation:")
    policy1_correct = create_iam_policy_correct(["s3:GetObject"])
    policy2_correct = create_iam_policy_correct(["s3:PutObject"])
    
    policy1_correct['Statement'][0]['Resource'].append("arn:aws:s3:::bucket1/*")
    
    print(f"Policy 1 Resources: {policy1_correct['Statement'][0]['Resource']}")
    print(f"Policy 2 Resources: {policy2_correct['Statement'][0]['Resource']}")
    print("✅ FIXED: Each has independent list")


def demo_4_integer_interning():
    """Show Python's integer caching behavior."""
    print("\n### DEMO 4: Integer Interning (Small Int Cache) ###\n")
    
    # Small integers are cached
    a = 256
    b = 256
    print(f"a = 256, b = 256")
    print(f"a is b: {a is b}")  # True
    print(f"id(a) = {id(a)}, id(b) = {id(b)}")
    print(f"RefCount of 256: {sys.getrefcount(256)}")
    print()
    
    # Large integers are NOT cached
    a = 257
    b = 257
    print(f"a = 257, b = 257")
    print(f"a is b: {a is b}")  # False!
    print(f"id(a) = {id(a)}, id(b) = {id(b)}")
    print(f"RefCount of 257: {sys.getrefcount(257)}")
    print()
    
    # Production impact
    print("🚨 Production Bug Example:")
    instance_count = 256
    expected_count = 256
    
    # WRONG - accidentally using 'is' instead of '=='
    if instance_count is 256:  # Works by accident!
        print("  ✓ Count is 256 (using 'is')")
    
    instance_count = 257
    expected_count = 257
    
    if instance_count is 257:  # Fails!
        print("  ✓ Count is 257 (using 'is')")
    else:
        print("  ✗ Failed! 'is' doesn't work for larger numbers")
    
    # CORRECT - always use '==' for value comparison
    if instance_count == 257:
        print("  ✓ Count is 257 (using '==')")


def demo_5_memory_leak_simulation():
    """Simulate a memory leak in a long-running service."""
    print("\n### DEMO 5: Memory Leak Simulation ###\n")
    
    class PodCache:
        """Simulates K8s pod watcher with memory leak."""
        
        def __init__(self):
            self.pods = {}  # Never cleaned!
        
        def process_event(self, event_type, pod_name, pod_data):
            """Process pod event - leaky version."""
            if event_type == "ADDED" or event_type == "MODIFIED":
                self.pods[pod_name] = pod_data
            # Bug: Never removes deleted pods!
        
        def get_cache_size(self):
            return len(self.pods)
    
    class PodCacheFixed:
        """Fixed version with proper cleanup."""
        
        def __init__(self, max_size=1000):
            from collections import OrderedDict
            self.pods = OrderedDict()
            self.max_size = max_size
        
        def process_event(self, event_type, pod_name, pod_data):
            """Process pod event - fixed version."""
            if event_type == "DELETED":
                self.pods.pop(pod_name, None)
            elif event_type in ("ADDED", "MODIFIED"):
                self.pods[pod_name] = pod_data
                self.pods.move_to_end(pod_name)
                
                # LRU eviction
                while len(self.pods) > self.max_size:
                    self.pods.popitem(last=False)
        
        def get_cache_size(self):
            return len(self.pods)
    
    print("Simulating 1000 pod events...")
    
    # Leaky version
    cache_leaky = PodCache()
    for i in range(1000):
        cache_leaky.process_event("ADDED", f"pod-{i}", {"data": "x" * 1000})
    
    # Simulate deletions
    for i in range(0, 500):
        cache_leaky.process_event("DELETED", f"pod-{i}", None)
    
    print(f"Leaky cache size: {cache_leaky.get_cache_size()} (should be 500!)")
    
    # Fixed version
    cache_fixed = PodCacheFixed(max_size=100)
    for i in range(1000):
        cache_fixed.process_event("ADDED", f"pod-{i}", {"data": "x" * 1000})
    
    for i in range(0, 500):
        cache_fixed.process_event("DELETED", f"pod-{i}", None)
    
    print(f"Fixed cache size: {cache_fixed.get_cache_size()} (capped at 100)")


def demo_6_object_aliasing():
    """Show object aliasing pitfalls."""
    print("\n### DEMO 6: Object Aliasing ###\n")
    
    # Lists
    print("List aliasing:")
    a = [1, 2, 3]
    b = a  # Same object!
    b.append(4)
    print(f"a = {a}")  # [1, 2, 3, 4]
    print(f"b = {b}")  # [1, 2, 3, 4]
    print(f"a is b: {a is b}\n")
    
    # Dictionaries - common in config management
    print("Dict aliasing (Terraform config example):")
    base_config = {
        "instance_type": "t2.micro",
        "subnet_id": "subnet-abc123"
    }
    
    # ❌ WRONG
    dev_config = base_config
    dev_config["instance_type"] = "t2.small"
    
    print(f"base_config: {base_config}")  # Modified!
    print(f"dev_config: {dev_config}")
    print("🚨 Bug: Modified base config!\n")
    
    # ✅ CORRECT
    import copy
    
    base_config = {
        "instance_type": "t2.micro",
        "subnet_id": "subnet-abc123"
    }
    
    prod_config = copy.deepcopy(base_config)
    prod_config["instance_type"] = "m5.large"
    
    print(f"base_config: {base_config}")  # Unchanged
    print(f"prod_config: {prod_config}")
    print("✅ Fixed: Used deepcopy")


if __name__ == "__main__":
    print("="*60)
    print("DAY 1: PYTHON REFERENCE COUNTING & MEMORY INTERNALS")
    print("="*60)
    
    try:
        demo_1_basic_refcount()
        input("\nPress Enter to continue to Demo 2...")
        
        demo_2_circular_reference()
        input("\nPress Enter to continue to Demo 3...")
        
        demo_3_aws_policy_mutable_default()
        input("\nPress Enter to continue to Demo 4...")
        
        demo_4_integer_interning()
        input("\nPress Enter to continue to Demo 5...")
        
        demo_5_memory_leak_simulation()
        input("\nPress Enter to continue to Demo 6...")
        
        demo_6_object_aliasing()
        
        print("\n" + "="*60)
        print("All demos completed!")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\nDemos interrupted by user.")
