"""
06_applied_automation_and_ai.py: Comprehensions & Real-World AI / DevOps Patterns

This script bridges foundational list mechanics into real-world engineering:
1. List Comprehensions (data transformation, filtering, and conditional logic).
2. DevOps Automation Patterns (log parsing, CLI command generation, health check aggregations).
3. AI / ML & GenAI Patterns (dataset mini-batching, prompt templating, vector calculations).
"""


def main():
    print("==================================================")
    print("1. LIST COMPREHENSIONS (FAST, PYTHONIC TRANSFORMATIONS)")
    print("==================================================")

    # Basic Syntax: [expression for item in iterable]

    # Example 1: Data Cleaning & Normalization (GenAI Prompt Preprocessing)
    raw_prompts = ["  How to run Kubernetes?  ", "WHAT IS DOCKER? ", "  train LLM model  "]
    clean_prompts = [p.strip().lower() for p in raw_prompts]
    print(f"Raw prompts:   {raw_prompts}")
    print(f"Clean prompts: {clean_prompts}")

    # Example 2: Filtering with 'if' (DevOps IP & Port Filtering)
    ip_addresses = ["192.168.1.1", "10.0.0.5", "192.168.1.25", "172.16.0.2", "192.168.1.99"]
    local_subnet_ips = [ip for ip in ip_addresses if ip.startswith("192.168.")]
    print(f"\nAll IPs:          {ip_addresses}")
    print(f"Local Subnet IPs: {local_subnet_ips}")

    # Example 3: Conditional If-Else (Transforming based on condition)
    # Syntax: [val_if_true if condition else val_if_false for item in iterable]
    latencies_ms = [45, 120, 310, 85, 450, 60]
    health_labels = ["OK" if ms < 200 else "SLOW [!]" for ms in latencies_ms]
    print(f"\nLatencies:     {latencies_ms}")
    print(f"Health Labels: {health_labels}")

    # Example 4: Flattening Nested Lists (e.g., token sequences from 3 sentences)
    nested_tokens = [["hello", "world"], ["ai", "is", "cool"], ["python", "scripts"]]
    flat_tokens = [token for sentence in nested_tokens for token in sentence]
    print(f"\nNested token lists: {nested_tokens}")
    print(f"Flattened tokens:   {flat_tokens}")


    print("\n==================================================")
    print("2. DEVOPS & AUTOMATION APPLIED PATTERNS")
    print("==================================================")

    # --- Pattern 2.1: Parsing Multi-line Raw Server Logs ---
    print("--- [Pattern 2.1: Log Parsing to Structured Lists] ---")
    raw_log_output = """
    2026-09-03 10:15:01 | INFO  | /api/v1/health | 200 | 12ms
    2026-09-03 10:15:02 | ERROR | /api/v1/auth   | 500 | 450ms
    2026-09-03 10:15:03 | INFO  | /api/v1/users  | 200 | 35ms
    2026-09-03 10:15:04 | WARN  | /api/v1/pay    | 429 | 110ms
    2026-09-03 10:15:05 | ERROR | /api/v1/db     | 503 | 820ms
    """

    # Parse non-empty lines into clean records
    parsed_logs = []
    for line in raw_log_output.strip().splitlines():
        parts = [col.strip() for col in line.split("|")]
        if len(parts) == 5:
            timestamp, level, endpoint, status, latency = parts
            parsed_logs.append({
                "timestamp": timestamp,
                "level": level,
                "endpoint": endpoint,
                "status": int(status),
                "latency_ms": int(latency.replace("ms", ""))
            })

    # Filter critical errors from parsed logs
    error_endpoints = [log["endpoint"] for log in parsed_logs if log["level"] == "ERROR"]
    print(f"Parsed {len(parsed_logs)} log events.")
    print(f"Endpoints experiencing ERRORs: {error_endpoints}")

    # --- Pattern 2.2: Dynamic CLI Command String Generator ---
    print("\n--- [Pattern 2.2: Dynamic Docker / CLI Command Assembly] ---")
    environment_variables = ["ENV=production", "PORT=8080", "WORKERS=4", "LOG_LEVEL=info"]
    volumes = ["/var/data:/data", "/etc/ssl:/ssl:ro"]

    # Build docker run command dynamically using list comprehensions and .join()
    cmd_parts = ["docker", "run", "-d", "--name", "api-gateway"]
    cmd_parts.extend([f"-e {env}" for env in environment_variables])
    cmd_parts.extend([f"-v {vol}" for vol in volumes])
    cmd_parts.append("my-company/api-gateway:v2.4")

    final_command = " ".join(cmd_parts)
    print("Generated CLI Command:")
    print(f"  $ {final_command}")


    print("\n==================================================")
    print("3. AI / ML & GENAI APPLIED PATTERNS")
    print("==================================================")

    # --- Pattern 3.1: Dataset Mini-Batching (The core of DataLoader & LLM batch API) ---
    print("--- [Pattern 3.1: Chunking Data into Mini-Batches] ---")
    dataset_records = [f"sample_{i:02d}" for i in range(1, 11)]  # 10 samples
    batch_size = 3

    # Slice the list in chunks of batch_size
    batches = [dataset_records[i : i + batch_size] for i in range(0, len(dataset_records), batch_size)]

    print(f"Full Dataset ({len(dataset_records)} items): {dataset_records}")
    print(f"Batch Size: {batch_size}")
    print(f"Generated {len(batches)} Batches:")
    for batch_idx, batch in enumerate(batches, start=1):
        print(f"  Batch #{batch_idx} ({len(batch)} items): {batch}")

    # --- Pattern 3.2: GenAI Prompt Templating ---
    print("\n--- [Pattern 3.2: GenAI Prompt Templating Pipeline] ---")
    user_queries = [
        "How do I create a Kubernetes Pod?",
        "What is gradient descent in ML?",
        "Explain Python list slicing."
    ]

    system_instruction = "You are an expert tech mentor. Answer concisely in 2 sentences."

    # Generate ready-to-send prompt payloads for each query
    formatted_prompts = [
        f"Instruction: {system_instruction}\nUser Query: {query}\nResponse:"
        for query in user_queries
    ]

    print(f"Generated {len(formatted_prompts)} formatted LLM inputs:")
    for i, p in enumerate(formatted_prompts, start=1):
        print(f"\n[Prompt #{i}]\n{p}")

    # --- Pattern 3.3: Basic Vector Math (Dot Product & Mean Squared Error) ---
    print("\n--- [Pattern 3.3: Vector Math & Metric Calculation with Lists] ---")

    # Vector Dot Product (Used in Attention mechanisms & Cosine Similarity)
    # Dot Product = sum(v1[i] * v2[i])
    vector_a = [0.2, 0.8, 0.5, 0.1]  # e.g., query embedding
    vector_b = [0.3, 0.7, 0.4, 0.2]  # e.g., document embedding

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print(f"Vector Dot Product (Similarity Score): {dot_product:.4f}")

    # Mean Squared Error (MSE Loss Calculation)
    # MSE = average of (actual - predicted)^2
    actual_targets   = [10.0, 15.0, 20.0, 25.0]
    predicted_values = [10.5, 14.2, 21.1, 24.0]

    squared_errors = [(act - pred) ** 2 for act, pred in zip(actual_targets, predicted_values)]
    mse_loss = sum(squared_errors) / len(squared_errors)

    print(f"\nActual Targets:    {actual_targets}")
    print(f"Predicted Values:  {predicted_values}")
    print(f"Squared Errors:    {[round(se, 4) for se in squared_errors]}")
    print(f"Mean Squared Error (MSE Loss): {mse_loss:.4f}")
    print("==================================================")


if __name__ == "__main__":
    main()
