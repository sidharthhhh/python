# Python Lists for Automation, DevOps, and AI/ML

Welcome to the **Python Lists Mastery** module. 

Instead of theoretical Data Structures & Algorithms (DSA) puzzles, this curriculum focuses on **step-by-step code flow, loop logic, data filtering/transforming, and real-world engineering**:
- 🛠️ **DevOps & Automation:** Parsing command-line outputs, managing server pools, filtering log events, building CLI flags, and draining task queues.
- 🤖 **AI / ML & GenAI:** Batching training datasets, managing prompt context windows, normalizing feature vectors, and calculating similarity dot products.

---

## 📚 6-Step Learning Roadmap

Follow and run the scripts in numerical order to build complete mastery of list code flows:

### [01_basics.py](file:///c:/Users/Sidharth/Desktop/python/array/01_basics.py) — Fundamentals & List Syntax Mechanics
* **What you'll learn:** List creation, 0-based indexing, negative indexing (`[-1]` for latest item), slicing (`[:3]`, `[::-1]`), mutating (`append`, `extend`, `insert`), removing (`pop`, `remove`, `del`, `clear`), and built-in inspection functions (`len`, `in`, `min`, `max`, `sum`, `all`, `any`).
* **Real-World Scenarios:** HTTP status code error tracker, LLM prompt context window trimmer, and epoch loss logger.

### [02_loops_and_code_flow.py](file:///c:/Users/Sidharth/Desktop/python/array/02_loops_and_code_flow.py) — Loops, Flow Control & Queues
* **What you'll learn:** Visualizing how Python steps through loops pass-by-pass, the **Accumulator Pattern** (running totals and collector lists), early exit with `break`, skipping items with `continue`, the unique `for ... else` construct, and draining task queues with `while`.
* **Real-World Scenarios:** Scanning log streams with early exit on `FATAL` errors, API health retry counter, and token word accumulator.

### [03_filtering_and_transforming.py](file:///c:/Users/Sidharth/Desktop/python/array/03_filtering_and_transforming.py) — Filter & Map Mental Models
* **What you'll learn:** The two foundational data operations: **Filtering** (extracting subsets) and **Transforming** (modifying values). Compares manual step-by-step loops side-by-side with List Comprehensions, plus 2D table/grid code flows.
* **Real-World Scenarios:** Extracting response latencies from log lines, building security group firewall flags, and Min-Max feature normalization.

### [04_common_beginner_pitfalls.py](file:///c:/Users/Sidharth/Desktop/python/array/04_common_beginner_pitfalls.py) — Top 5 Traps & Debugging
* **What you'll learn:** The top 5 bugs every beginner faces:
  1. Modifying a list during iteration (the index skipping bug) & the slice fix.
  2. Forgetting that `.append()` / `.sort()` return `None`.
  3. Default mutable arguments in functions (`log_list=[]`).
  4. Variable aliasing vs real shallow/deep copying (`b = a` vs `b = a.copy()`).
  5. Off-by-one errors with `range()` and slicing boundaries.

### [05_intermediate_operations.py](file:///c:/Users/Sidharth/Desktop/python/array/05_intermediate_operations.py) — Sorting, Enumerate, Zip & Strings
* **What you'll learn:** Searching (`count`, `index`), in-place `.sort()` vs `sorted()`, custom sorting with `key=lambda` (sorting models by accuracy, containers by memory), `enumerate()` (index + value), `zip()` (parallel iteration), string `.split()` / `", ".join()`, and sequence unpacking (`head, *middle, tail`).
* **Real-World Scenarios:** Sorting Docker containers by memory/CPU load, and calculating model accuracy percentage with `zip()`.

### [06_applied_automation_and_ai.py](file:///c:/Users/Sidharth/Desktop/python/array/06_applied_automation_and_ai.py) — End-to-End Real World Pipelines
* **What you'll learn:** Advanced list comprehensions with inline conditionals, multi-line log parsers, dynamic Docker CLI command generators, dataset mini-batch chunking, GenAI prompt templating, and vector math (dot product similarity & Mean Squared Error loss).

---

## ⚡ Quick Reference Cheat Sheet

### 1. Essential List Operations
| Operation | Syntax | Example | Result / Purpose |
| :--- | :--- | :--- | :--- |
| **Create** | `[a, b, c]` | `servers = ["web1", "web2"]` | Creates a new list |
| **Last item** | `list[-1]` | `servers[-1]` | `"web2"` (Negative indexing) |
| **Slice Top-k** | `list[:k]` | `[10, 20, 30, 40][:2]` | `[10, 20]` (First 2 items) |
| **Reverse** | `list[::-1]` | `[1, 2, 3][::-1]` | `[3, 2, 1]` |
| **Append** | `list.append(x)` | `tasks.append("deploy")` | Adds to end in-place (returns `None`) |
| **Extend** | `list.extend(iter)` | `tasks.extend(["test", "notify"])` | Appends all items from iterable |
| **Pop** | `list.pop(0)` | `tasks.pop(0)` | Removes & returns first item (FIFO) |

### 2. Code Flow Patterns at a Glance
```python
# 1. ACCUMULATOR PATTERN (Running total / Collector list)
total = 0
for val in values:
    total += val

# 2. FILTER PATTERN (Keep items matching condition)
error_codes = [c for c in status_codes if c >= 400]

# 3. TRANSFORM PATTERN (Modify every item)
clean_prompts = [p.strip().lower() for p in raw_prompts]

# 4. CONDITIONAL TRANSFORM (If/Else inside comprehension)
labels = ["HEALTHY" if ms < 200 else "DEGRADED" for ms in latencies]

# 5. DUAL ITERATION (Loop multiple lists in parallel)
for prompt, response in zip(prompts, responses):
    print(f"Q: {prompt} -> A: {response}")

# 6. ENUMERATE (Track loop step / batch counter)
for step, batch in enumerate(batches, start=1):
    print(f"Step {step}/{len(batches)}: {batch}")
```

---

## 🚀 How to Run the Scripts

Execute any script directly in your terminal:

```bash
# Step 1: Syntax & list mechanics
python array/01_basics.py

# Step 2: Loop mechanics, accumulators & flow control
python array/02_loops_and_code_flow.py

# Step 3: Filtering & transforming mental models
python array/03_filtering_and_transforming.py

# Step 4: Top 5 beginner traps & debugging
python array/04_common_beginner_pitfalls.py

# Step 5: Sorting, enumerate, zip & string parsing
python array/05_intermediate_operations.py

# Step 6: Applied DevOps pipelines & AI/ML batching
python array/06_applied_automation_and_ai.py
```

---

## 🧠 Self-Check Practice Challenges

### Challenge 1: The Queue Draining Flow (DevOps)
Write a `while` loop that processes a list of server hostnames `["server-1", "server-2", "server-3"]` one by one, popping from the front until the list is empty.

<details>
<summary>👉 View Solution</summary>

```python
servers = ["server-1", "server-2", "server-3"]
while servers:
    current = servers.pop(0)
    print(f"Configuring {current}... Done!")
print("All servers configured.")
```
</details>

### Challenge 2: Clean & Filter User Prompts (GenAI)
Given `prompts = ["   what is ai? ", "", "   ", "Explain Docker  ", "Hi"]`, write a list comprehension to strip whitespace, lowercase each string, and keep only prompts with at least 3 words.

<details>
<summary>👉 View Solution</summary>

```python
prompts = ["   what is ai? ", "", "   ", "Explain Docker  ", "Hi"]
clean = [p.strip().lower() for p in prompts if len(p.strip().split()) >= 3]
print(clean)  # ['what is ai?']
```
</details>

### Challenge 3: Calculate Accuracy with zip() (AI/ML)
Given `y_true = ["cat", "dog", "dog", "cat"]` and `y_pred = ["cat", "cat", "dog", "cat"]`, count the number of matching predictions and calculate accuracy.

<details>
<summary>👉 View Solution</summary>

```python
y_true = ["cat", "dog", "dog", "cat"]
y_pred = ["cat", "cat", "dog", "cat"]

matches = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
accuracy = (matches / len(y_true)) * 100
print(f"Accuracy: {accuracy}% ({matches}/{len(y_true)})")  # 75.0%
```
</details>
