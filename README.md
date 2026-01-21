# 20-Day Intensive Python, DevOps & MLOps Learning Roadmap

**Goal:** Transition from Cloud/Infra background to Mid-Level Python Engineer for MLOps.
**Prerequisites:** Linux, Docker, Kubernetes, Terraform, CI/CD, AWS, Basic Backend.

---

## 📅 Phase 1: Python Foundations & Automation (Days 1-7)
**Focus:** Mastering the core language, file handling, and writing clean production code.

### [Day 1: Python Fundamentals](./days/day01_fundamentals/)
**Core Concepts:**
- Variables & Data Types.
- Lists `[]` vs Dictionaries `{}`.
- Loops (`for`, `while`) and Logic (`if`).

### [Day 2: real-world I/O & Modules](./days/day02_io_modules/)
**Core Concepts:**
- Reading/Writing Files (`open`, `with`).
- Handling JSON & CSV (`json`, `csv` modules).
- Modularizing code: Imports, `__name__ == "__main__"`.

### [Day 3: Object-Oriented Programming (OOP)](./days/day03_oop_basics/)
**Core Concepts:**
- Classes vs Dictionaries (The "Why").
- `__init__`, Methods, `self`.
- Inheritance (Basic).

### [Day 4: Modern Tooling & Quality](./days/day04_modern_tooling/)
**Core Concepts:**
- Virtual Environments (`poetry`).
- Linting (`ruff`) & Type Hints (`typing`).
- Running scripts professionally.

### [Day 5: Testing with Pytest](./days/day05_testing/)
**Core Concepts:**
- Writing your first test.
- Assertions.
- Fixtures (Setup/Teardown).

### [Day 6: DevOps Scripting](./days/day06_devops_scripting/)
**Core Concepts:**
- `subprocess` (Running shell commands).
- `os` and `sys` modules (File paths, Env vars).
- Arguments (`argparse` or `typer`).

### [Day 7: Mini-Project 1: The CLI Tool](./days/day07_capstone_cli/)
**Goal:** Build a tool that reads a file, processes it, and saves a report.

---

## 📅 Phase 2: Cloud Automation & MLOps Foundations (Days 8-14)
**Focus:** Taking Python to the cloud, containers, and starting ML.

### [Day 8: Dockerizing Python](./days/day08_docker/)
**Core Concepts:**
- Dockerfiles, Multi-stage builds.
- `docker-compose`.

### [Day 9: Cloud Automation (Boto3)](./days/day09_aws_boto3/)
**Core Concepts:**
- AWS SDK (Boto3).
- Automating S3/EC2 tasks.

### [Day 10: Data Manipulation](./days/day10_data_pandas/)
**Core Concepts:**
- Pandas basics (DataFrames).
- Reading/Cleaning data.

### [Day 11: Machine Learning 101](./days/day11_ml_basics/)
**Core Concepts:**
- Scikit-learn training.
- Model persistence.

### [Day 12: Model Serving (FastAPI)](./days/day12_fastapi/)
**Core Concepts:**
- Building an API.
- Serving the model.

### [Day 13: MLOps Tracking (MLflow)](./days/day13_mlflow/)
**Core Concepts:**
- Experiment tracking.
- Model Registry.

### [Day 14: Orchestration (Prefect)](./days/day14_prefect/)
**Core Concepts:**
- Building data pipelines.
- Retries and Scheduling.

---

## 📅 Phase 3: Production, Kubernetes & The Capstone (Days 15-20)
**Focus:** Deploying, scaling, and monitoring the ML application in a cloud-native way.

### [Day 15: Python & Kubernetes](./days/day15_kubernetes/)
**Core Concepts:**
- K8s Python client.

### [Day 16: CI/CD for ML](./days/day16_cicd_ml/)
**Core Concepts:**
- GitHub Actions for ML (CML).

### [Day 17: Observability & Logging](./days/day17_observability/)
**Core Concepts:**
- Prometheus metrics.
- Structured logging context.

### [Day 18: Advanced Deployment](./days/day18_advanced_deployment/)
**Core Concepts:**
- Blue/Green, Canary.
- Helm Charts.

### [Days 19-20: Capstone Project](./days/day19_20_capstone/)
**Goal:** End-to-End MLOps Platform (Data -> Train -> Deploy -> Monitor).

---

## 📂 Repository Structure
- `days/`: Contains daily lessons and code.
- `data/`: Shared data directory.
- `docker/`: Shared Docker resources.
