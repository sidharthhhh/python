# Day 1 Quick Reference - Python Internals

## 🔑 Key Concepts

### 1. Everything is a PyObject
```c
typedef struct _object {
    Py_ssize_t ob_refcnt;  // Reference count
    PyTypeObject *ob_type;  // Type pointer
} PyObject;
```

### 2. Reference Counting
- **Increment**: When new reference created (`y = x`)
- **Decrement**: When reference deleted (`del x`)
- **Free**: When refcount reaches 0

```python
import sys
x = [1, 2, 3]
sys.getrefcount(x)  # Get reference count
```

### 3. Circular References
```python
# Creates cycle - won't be freed by refcounting alone
node1.next = node2
node2.next = node1

# Solution: Use gc.collect() or weakref
import gc
gc.collect()  # Break cycles
```

### 4. Integer Interning
```python
a = 256
b = 256
a is b  # True - cached!

a = 257
b = 257
a is b  # False - not cached
```

**Range**: Python caches integers from **-5 to 256**

---

## 🚨 Common Pitfalls

### 1. Mutable Default Arguments
```python
# ❌ WRONG
def func(items=[]):
    items.append(1)
    return items

# ✅ CORRECT
def func(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
```

### 2. Object Aliasing
```python
# ❌ WRONG
config = base_config
config['key'] = 'value'  # Modifies base_config!

# ✅ CORRECT
import copy
config = copy.deepcopy(base_config)
```

### 3. Memory Leaks in Long-Running Services
```python
# ❌ WRONG - Unbounded growth
cache = {}  # Never cleaned

# ✅ CORRECT - LRU with max size
from collections import OrderedDict
cache = OrderedDict()
if len(cache) > MAX_SIZE:
    cache.popitem(last=False)
```

### 4. Storing Full Objects
```python
# ❌ WRONG - Circular refs
self.pods[name] = pod_object  # Full K8s pod

# ✅ CORRECT - Extract only needed data
self.pods[name] = {
    'name': pod.metadata.name,
    'status': pod.status.phase
}
```

### 5. Using 'is' for Value Comparison
```python
# ❌ WRONG
if count is 100:  # Only works for small numbers!

# ✅ CORRECT
if count == 100:  # Always use == for values
```

---

## ⚡ Performance Tips

### 1. Cache Method References
```python
# Slow
for item in items:
    results.append(item)

# Faster
append = results.append
for item in items:
    append(item)
```

### 2. Use Generators for Large Data
```python
# Memory intensive
def get_all(): return [x for x in range(1000000)]

# Memory efficient
def get_all(): return (x for x in range(1000000))
```

### 3. Choose Right Data Structure
- **List**: Mutable, ordered, allows duplicates
- **Tuple**: Immutable, slightly faster/smaller
- **Array**: Numeric data, 50-70% less memory
- **Set**: Unique items, O(1) lookup

### 4. Avoid Repeated Lookups
```python
# Slow
for i in range(len(data)):
    process(data[i])

# Faster
for item in data:
    process(item)
```

---

## 🔍 Debugging Commands

```python
import sys
import gc

# Check reference count
sys.getrefcount(obj)

# Find all objects of a type
[o for o in gc.get_objects() if isinstance(o, MyClass)]

# Force garbage collection
gc.collect()

# Get GC stats
gc.get_count()  # (gen0, gen1, gen2)
gc.get_stats()

# Track object creation
import tracemalloc
tracemalloc.start()
# ... run code ...
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
```

---

## 📊 Memory Monitoring

```python
import psutil

process = psutil.Process()
mem = process.memory_info()

print(f"RSS: {mem.rss / 1024 / 1024:.2f} MB")  # Physical memory
print(f"VMS: {mem.vms / 1024 / 1024:.2f} MB")  # Virtual memory
```

---

## 🎯 Interview Questions - Quick Answers

**Q: Why does Python use reference counting?**  
A: Deterministic cleanup (immediate freeing), predictable performance (no GC pauses), C extension compatibility.

**Q: What's the downside of reference counting?**  
A: Can't handle circular references alone, needs supplemental GC.

**Q: When does garbage collection run?**  
A: When generation thresholds are exceeded, or manually via `gc.collect()`.

**Q: Why is everything heap-allocated in Python?**  
A: Dynamic typing requires runtime type information, objects need to outlive stack frames.

**Q: What's the cost of a Python function call?**  
A: ~100-200ns overhead (frame creation, argument packing, name lookup) vs ~1ns in C.

---

## 📁 CPython Source Files to Read

```
Objects/
  ├── longobject.c      # Integer implementation
  ├── listobject.c      # List implementation
  ├── dictobject.c      # Dictionary implementation
  
Python/
  ├── ceval.c           # Main interpreter loop
  
Modules/
  ├── gcmodule.c        # Garbage collector
  
Include/
  ├── object.h          # PyObject definition
```

---

## 🛠️ Useful Patterns

### LRU Cache with TTL
```python
from collections import OrderedDict
import time

class TTLCache:
    def __init__(self, max_size=100, ttl=300):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.ttl = ttl
    
    def get(self, key):
        if key not in self.cache:
            return None
        
        value, timestamp = self.cache[key]
        if time.time() - timestamp > self.ttl:
            del self.cache[key]
            return None
        
        self.cache.move_to_end(key)
        return value
    
    def put(self, key, value):
        if len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)
        
        self.cache[key] = (value, time.time())
```

### Memory Profiler Decorator
```python
import tracemalloc
import functools

def profile_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"{func.__name__}: Current={current/1024/1024:.2f}MB, "
              f"Peak={peak/1024/1024:.2f}MB")
        
        return result
    return wrapper
```

---

## 🎓 Next Steps

1. Complete all homework exercises
2. Debug the production challenge
3. Build the Lambda memory profiler
4. Read `Objects/longobject.c` in CPython source
5. Move to Day 2: Memory Deep Dive (GIL, Heap, Stack)

---

**Remember**: Understanding internals makes you 10x more effective at debugging and optimization.
