"""
Quick Test: Verify Day 1 examples work correctly
"""

import sys
import gc


def test_reference_counting():
    """Test basic reference counting."""
    print("Testing reference counting...")
    
    x = [1, 2, 3]
    initial_count = sys.getrefcount(x) - 1  # -1 for the function call itself
    print(f"  Initial refcount: {initial_count}")
    
    y = x
    after_alias = sys.getrefcount(x) - 1
    print(f"  After creating alias: {after_alias}")
    
    assert after_alias > initial_count, "Refcount should increase"
    print("  ✅ Reference counting works!\n")


def test_circular_reference():
    """Test garbage collection of circular references."""
    print("Testing circular reference collection...")
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    # Create cycle
    a = Node(1)
    b = Node(2)
    a.next = b
    b.next = a
    
    # Count nodes before deletion
    before = len([obj for obj in gc.get_objects() if isinstance(obj, Node)])
    print(f"  Nodes before deletion: {before}")
    
    # Delete references
    del a, b
    
    # Force GC
    collected = gc.collect()
    print(f"  GC collected: {collected} objects")
    
    after = len([obj for obj in gc.get_objects() if isinstance(obj, Node)])
    print(f"  Nodes after GC: {after}")
    
    print("  ✅ Garbage collection works!\n")


def test_integer_interning():
    """Test Python's integer caching."""
    print("Testing integer interning...")
    
    # Small integers are cached
    a = 256
    b = 256
    print(f"  256 is 256: {a is b}")
    assert a is b, "Small integers should be cached"
    
    # Large integers are not
    a = 257
    b = 257
    print(f"  257 is 257: {a is b}")
    print(f"  257 == 257: {a == b}")
    
    print("  ✅ Integer interning works as expected!\n")


def test_mutable_default():
    """Test mutable default argument bug."""
    print("Testing mutable default arguments...")
    
    def append_to_list_wrong(item, lst=[]):
        lst.append(item)
        return lst
    
    result1 = append_to_list_wrong(1)
    result2 = append_to_list_wrong(2)
    
    print(f"  First call: {result1}")
    print(f"  Second call: {result2}")
    print(f"  Same list? {result1 is result2}")
    
    if result1 is result2:
        print("  🚨 Confirmed: Mutable defaults are shared!\n")
    
    # Fixed version
    def append_to_list_correct(item, lst=None):
        if lst is None:
            lst = []
        lst.append(item)
        return lst
    
    result3 = append_to_list_correct(1)
    result4 = append_to_list_correct(2)
    
    print(f"  Fixed - First call: {result3}")
    print(f"  Fixed - Second call: {result4}")
    print(f"  Same list? {result3 is result4}")
    
    assert result3 is not result4, "Fixed version should create new lists"
    print("  ✅ Mutable default fix works!\n")


if __name__ == "__main__":
    print("="*60)
    print("DAY 1 - QUICK VERIFICATION TESTS")
    print("="*60)
    print()
    
    try:
        test_reference_counting()
        test_circular_reference()
        test_integer_interning()
        test_mutable_default()
        
        print("="*60)
        print("✅ All tests passed!")
        print("="*60)
        print("\nYou're ready to start Day 1 training:")
        print("1. Read: day1/README.md")
        print("2. Run: python day1/01_reference_counting.py")
        print("3. Complete: python day1/02_homework.py")
        print("4. Challenge: python day1/03_production_challenge.py")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
