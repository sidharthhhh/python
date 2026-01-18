# Day 1 – Python Core Internals for DevOps

> **"You can't optimize what you don't understand."**

## 🎯 Learning Objectives

- Python's memory model and PyObject system
- Reference counting and garbage collection
- Memory leaks in long-running services
- Production debugging and optimization

---

## 1. Core Concept: Everything is a PyObject

```c
// CPython source: Include/object.h
typedef struct _object {
    Py_ssize_t ob_refcnt;  // Reference count
    PyTypeObject *ob_type;  // Type pointer
} PyObject;
```

**Key Points:**
- Every value is heap-allocated (overhead: ~28 bytes/int vs 4 bytes in C)
- Variables are pointers, not values
- Reference counting manages memory (immediate cleanup)
- Garbage collector handles circular references (periodic)

---

## 2. Production Example: K8s Pod Watcher

### ❌ Bad Code - Memory Leak

```python
from kubernetes import client, watch

def watch_pods_bad():
    v1 = client.CoreV1Api()
    pod_cache = {}  # Never cleaned!
    
    for event in watch.Watch().stream(v1.list_pod_for_all_namespaces):
        pod_cache[event['object'].metadata.name] = {
            'status': event['object'].status.phase,
            'full_object': event['object']  # Circular refs!
        }
    # After 24h: 50GB+ memory
```

**Issues:**
1. Unbounded cache growth
2. Deleted pods never removed
3. Circular references in `full_object`

### ✅ Good Code - Production Ready

```python
from collections import OrderedDict
import gc, time

class PodWatcher:
    def __init__(self, max_size=1000, ttl=300):
        self._cache = OrderedDict()
        self._max_size = max_size
        self._ttl = ttl
    
    def watch_pods(self):
        v1 = client.CoreV1Api()
        for event in watch.Watch().stream(v1.list_pod_for_all_namespaces):
            pod = event['object']
            name = f"{pod.metadata.namespace}/{pod.metadata.name}"
            
            if event['type'] == "DELETED":
                self._cache.pop(name, None)
            else:
                # Store only needed fields
                self._cache[name] = {
                    'status': pod.status.phase,
                    'timestamp': time.time()
                }
                self._cache.move_to_end(name)
            
            # LRU eviction
            if len(self._cache) > self._max_size:
                self._cache.popitem(last=False)
```

**Fixes:**
- ✅ LRU cache with max size
- ✅ TTL-based eviction
- ✅ Explicit deletion handling
- ✅ No circular references

---

## 3. Edge Cases

### Integer Interning

```python
a = 256; b = 256
print(a is b)  # True - cached!

a = 257; b = 257
print(a is b)  # False - not cached

# CPython caches integers [-5, 256]
# Always use == for values, is for identity
```

### Mutable Default Arguments

```python
# ❌ WRONG
def create_policy(actions, resources=[]):
    policy = {"Resource": resources}
    return policy

# Both share same list!
p1 = create_policy(["s3:Get"])
p2 = create_policy(["s3:Put"])

# ✅ CORRECT
def create_policy(actions, resources=None):
    if resources is None:
        resources = []
    # ...
```

---

## 4. Performance Tips

### Cache Method References

```python
# Slow - attribute lookup each iteration
for line in lines:
    results.append(process(line))

# Fast - cache method
append = results.append
for line in lines:
    append(process(line))
```

### Use Generators for Large Data

```python
# Memory intensive
def get_all(): return [x for x in range(1_000_000)]

# Memory efficient
def get_all(): return (x for x in range(1_000_000))
```

---

## 5. Debugging Tools

```python
import sys, gc, psutil

# Reference count
sys.getrefcount(obj)

# Find objects
[o for o in gc.get_objects() if isinstance(o, MyClass)]

# Force GC
gc.collect()

# Memory usage
process = psutil.Process()
print(f"Memory: {process.memory_info().rss / 1024 / 1024:.2f} MB")

# Track allocations
import tracemalloc
tracemalloc.start()
# ... code ...
current, peak = tracemalloc.get_traced_memory()
```

---

## 6. Interview Questions

**Q: Why reference counting instead of GC only?**  
A: Deterministic cleanup (file handles), predictable performance (no pauses), C extension compatibility. Trade-off: can't handle cycles alone.

**Q: Why is Python slower than C?**  
A: Every operation involves PyObject overhead, type checks, reference counting, dynamic dispatch.

**Q: When does GC run?**  
A: When generation thresholds exceeded or `gc.collect()` called manually.

---

## 7. Mini Project: Lambda Memory Profiler

Build a decorator to track Lambda memory usage:

```python
import tracemalloc, functools

def memory_profile(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        snapshot_before = tracemalloc.take_snapshot()
        
        result = func(*args, **kwargs)
        
        current, peak = tracemalloc.get_traced_memory()
        snapshot_after = tracemalloc.take_snapshot()
        top_stats = snapshot_after.compare_to(snapshot_before, 'lineno')
        
        # TODO: Send to CloudWatch
        print(f"Peak: {peak / 1024 / 1024:.2f} MB")
        
        tracemalloc.stop()
        return result
    return wrapper
```

---

## 8. Homework

1. **Circular Reference Demo** - Create cycle, show refcounts, prove `gc.collect()` frees it
2. **SSM Parameter Cache** - LRU cache with TTL (see `02_homework.py`)
3. **Data Structure Benchmark** - Compare list/tuple/array for memory and speed

---

## 9. Production Challenge

Debug memory leak in `03_production_challenge.py`:
- Find 6 different leaks in K8s log aggregator  
- Fix unbounded cache, circular refs, large objects
- Add memory monitoring

---

## 10. What to Learn Next

**Break intentionally:**
- Reference cycles
- Unbounded caches
- Mutable defaults
- File handle leaks

**Benchmark:**
- List append vs extend
- Dict lookup vs get
- Function call overhead

**Read CPython source:**
- `Objects/longobject.c` - Integer implementation
- `Modules/gcmodule.c` - Garbage collector
- `Python/ceval.c` - Main interpreter loop

---

## Quick Reference

See [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) for cheat sheet.

## Code Examples

Run interactive demos:
```bash
python 00_quick_test.py          # Verify
python 01_reference_counting.py  # Demos
python 02_homework.py            # Exercises
python 03_production_challenge.py # Debug
```

---

**Next:** Day 2 - Memory Deep Dive (GIL, Heap, `__slots__`)
