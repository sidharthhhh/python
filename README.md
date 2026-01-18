# 20-Day Python Production Engineering Bootcamp

> **Senior-level training for DevOps/Backend Engineers**

---

## 🎯 Course Goal

Transform from DevOps Engineer → Senior Python Platform Engineer in 20 days.

**Focus Areas:** Python Internals • FastAPI • Kubernetes • AWS • AI/ML/GenAI  
**Time:** 3-4 hours/day  
**Level:** Senior/Staff Engineer

---

## 📚 Course Status & Curriculum

### ✅ Week 1: Python Internals & Core Systems

| Day | Topic | Status | Content |
|-----|-------|--------|---------|
| **1** | **[Python Core Internals](./day1/)** | ✅ **COMPLETE** | PyObject, RefCount, Memory, GC |
| **2** | **Memory Deep Dive** | ⏳ Planned | GIL, Heap, `__slots__`, Allocator |
| **3** | **Concurrency Fundamentals** | ⏳ Planned | Threading vs Async vs Multiprocessing |
| **4** | **AsyncIO Internals** | ⏳ Planned | Event Loop, Coroutines, Tasks |
| **5** | **Performance Profiling** | ⏳ Planned | cProfile, Flame Graphs, Optimization |

### ⏳ Week 2: FastAPI & Backend Systems

| Day | Topic | Status | Content |
|-----|-------|--------|---------|
| **6** | FastAPI Deep Dive | ⏳ Planned | Dependency Injection, Background Tasks |
| **7** | Async Database Patterns | ⏳ Planned | SQLAlchemy, Connection Pools |
| **8** | API Design & Versioning | ⏳ Planned | REST, Rate Limiting, Auth |
| **9** | Testing & CI/CD | ⏳ Planned | pytest, Docker, GitHub Actions |
| **10** | Observability | ⏳ Planned | Logging, Prometheus, Tracing |

### ⏳ Week 3: Kubernetes & Cloud Automation

| Day | Topic | Status | Content |
|-----|-------|--------|---------|
| **11** | Kubernetes Python Client | ⏳ Planned | Watch API, Informers |
| **12** | Kubernetes Operators | ⏳ Planned | CRDs, Controllers |
| **13** | Helm & GitOps | ⏳ Planned | Templating, ArgoCD |
| **14** | AWS Automation | ⏳ Planned | Boto3, EKS, Cost Optimization |
| **15** | Infrastructure as Code | ⏳ Planned | Pulumi, State Management |

### ⏳ Week 4: AI/ML & GenAI Systems

| Day | Topic | Status | Content |
|-----|-------|--------|---------|
| **16** | ML Pipeline Fundamentals | ⏳ Planned | scikit-learn, pandas |
| **17** | Deep Learning Systems | ⏳ Planned | PyTorch, GPU, Distributed Training |
| **18** | Vector DBs & RAG | ⏳ Planned | Embeddings, Pinecone, Chroma |
| **19** | LLM Agents | ⏳ Planned | OpenAI, Function Calling |
| **20** | Production GenAI | ⏳ Planned | Caching, Monitoring, Cost |

---

## 📂 Daily Structure

Each day follows this pattern:

```
dayN/
├── README.md                    # Main tutorial
├── QUICK_REFERENCE.md          # Cheat sheet
├── 00_quick_test.py            # Verification
├── 01_<topic>_demo.py          # Interactive demos
├── 02_homework.py              # Exercises + solutions
└── 03_production_challenge.py  # Debug real bugs
```

---

## 🚀 Quick Start

### Day 1 (Available Now)
```bash
cd day1
python 00_quick_test.py          # Verify setup
python 01_reference_counting.py  # Interactive demos
python 02_homework.py            # Exercises
python 03_production_challenge.py # Debug challenge
```

---

## 🎓 Teaching Philosophy

1. **Production First** - Real K8s/AWS/Backend scenarios, not toy examples
2. **Bad Code First** - Show mistakes, then fixes
3. **Deep Internals** - CPython source code, not just APIs
4. **Measure Everything** - Benchmarks for all performance claims
5. **Learn by Breaking** - Intentional bugs teach more than perfect code

---

## 📦 Setup

### Minimal (Day 1-5)
```bash
pip install psutil memory-profiler
```

### Full Course
```bash
pip install -r requirements.txt
```

---

## 📚 Day 1 Summary

**Topics Covered:**
- PyObject system & reference counting
- Memory leaks in K8s watchers
- Circular references & garbage collection
- AWS SSM parameter caching (LRU + TTL)
- Integer interning edge cases
- Mutable default argument bugs

**Files Created:**
- Tutorial README (5KB)
- 6 interactive demos
- 3 homework exercises
- Production debugging challenge
- Quick reference guide

**Key Outputs:**
- Lambda memory profiler (mini project)
- K8s log aggregator (broken → fixed)
- SSM cache implementation

---

## 🎯 Learning Outcomes By Week

**Week 1:** Understand Python internals, memory model, GIL, async, profiling  
**Week 2:** Build production FastAPI services, testing, observability  
**Week 3:** Write K8s operators, automate AWS, IaC with Pulumi  
**Week 4:** Build ML pipelines, RAG systems, LLM agents

---

## 📖 Recommended Reading

**Books:**
- CPython Internals (Anthony Shaw)
- Fluent Python (Luciano Ramalho)
- High Performance Python (Gorelick & Ozsvald)

**Source Code:**
- CPython: `Objects/`, `Python/ceval.c`, `Modules/gcmodule.c`
- FastAPI source
- kubernetes-client Python

---

**Current Status:** Day 1 complete ✅ | Days 2-20 in progress 🚀