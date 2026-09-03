"""
05_intermediate_operations.py: Searching, Sorting, Iteration & Real-World Wrangling

This script covers everyday list techniques you will constantly use when:
- Parsing command-line outputs, Docker/Kubernetes statuses, and server logs.
- Iterating over datasets with `enumerate()` and `zip()`.
- Sorting data by custom attributes (e.g., confidence scores, timestamps, CPU load).
- Avoiding critical reference bugs with shallow vs. deep copies.
"""

import copy


def main():
    print("==================================================")
    print("1. SEARCHING & COUNTING IN LISTS")
    print("==================================================")

    log_levels = ["INFO", "DEBUG", "INFO", "WARNING", "ERROR", "INFO", "ERROR"]
    print(f"Log levels: {log_levels}")

    # count(value): Counts how many times a value appears
    info_count = log_levels.count("INFO")
    error_count = log_levels.count("ERROR")
    print(f"Count of 'INFO': {info_count}")
    print(f"Count of 'ERROR': {error_count}")

    # index(value): Returns the index of the FIRST occurrence
    # IMPORTANT: index() raises ValueError if the element is not found! Always check or use try/except.
    try:
        first_warning_idx = log_levels.index("WARNING")
        print(f"First 'WARNING' found at index: {first_warning_idx}")
    except ValueError:
        print("'WARNING' not found in the list.")

    # Safe pattern: Use 'in' before calling .index()
    target = "CRITICAL"
    if target in log_levels:
        print(f"{target} index: {log_levels.index(target)}")
    else:
        print(f"'{target}' was not present (safely avoided ValueError).")


    print("\n==================================================")
    print("2. SORTING LISTS (IN-PLACE vs RETURN NEW)")
    print("==================================================")

    # 1. In-place sorting with .sort() -> Modifies the original list directly, returns None
    latencies = [120, 45, 310, 85, 205]
    print(f"Original latencies: {latencies}")
    latencies.sort()
    print(f"After latencies.sort() [Ascending]:  {latencies}")

    latencies.sort(reverse=True)
    print(f"After latencies.sort(reverse=True) [Descending]: {latencies}")

    # 2. sorted() function -> Returns a NEW sorted list, keeps original intact
    raw_scores = [0.92, 0.45, 0.88, 0.61]
    sorted_scores = sorted(raw_scores, reverse=True)
    print(f"\nOriginal raw_scores: {raw_scores} (unchanged)")
    print(f"New sorted_scores:   {sorted_scores}")

    # 3. Custom Sorting with key=lambda
    # Real-world: Sorting tuples of (model_name, accuracy_score) by score descending
    models = [
        ("bert-base", 0.89),
        ("roberta-large", 0.94),
        ("distilbert", 0.86),
        ("gpt-neo", 0.91)
    ]
    # Sort by the second element in the tuple (the score)
    models.sort(key=lambda item: item[1], reverse=True)
    print("\nModels sorted by accuracy (highest first):")
    for name, acc in models:
        print(f"  - {name:<15}: {acc:.2f}")

    # Sorting strings by length
    service_names = ["authentication", "api", "db", "notification-gateway"]
    service_names.sort(key=len)
    print(f"\nServices sorted by length: {service_names}")


    print("\n==================================================")
    print("3. POWERFUL ITERATION PATTERNS")
    print("==================================================")

    # 1. Standard Loop
    endpoints = ["/health", "/api/v1/predict", "/metrics"]
    print("Standard Loop:")
    for ep in endpoints:
        print(f"  Endpoint: {ep}")

    # 2. enumerate() -> Provides both index AND item (Essential for training step counters & batch tracking)
    print("\nUsing enumerate() [Index + Value]:")
    batches = ["batch_01_tokens", "batch_02_tokens", "batch_03_tokens"]
    for step, batch_data in enumerate(batches, start=1):
        print(f"  Step {step}/{len(batches)}: Processing {batch_data}")

    # 3. zip() -> Iterates multiple lists simultaneously in pairs
    # Real-world: Pairing input prompts with generated AI completions
    user_prompts = [
        "Translate 'hello' to French",
        "Explain Docker in 5 words",
        "Write a python list example"
    ]
    ai_completions = [
        "Bonjour",
        "Containerized applications anywhere easily",
        "my_list = [1, 2, 3]"
    ]

    print("\nUsing zip() [Pairing multiple lists]:")
    for prompt, response in zip(user_prompts, ai_completions):
        print(f"  Q: '{prompt}'")
        print(f"  A: '{response}'")
        print("  ---")

    # 4. reversed() -> Iterates backwards without altering the original list
    history = ["v1.0.0", "v1.1.0", "v1.2.0"]
    print("\nIterating backwards with reversed():")
    for version in reversed(history):
        print(f"  Version: {version}")


    print("\n==================================================")
    print("4. STRINGS & LISTS: SPLIT, STRIP & JOIN")
    print("==================================================")

    # .join(): Combines a list of strings into a single string with a delimiter
    # Super useful for building CLI arguments, file paths, SQL query clauses, or prompt context
    tags = ["python", "machine-learning", "devops", "cloud"]
    tag_string = ", ".join(tags)
    print(f"Joined tags string: '{tag_string}'")

    command_parts = ["docker", "run", "-d", "-p", "8080:80", "nginx:alpine"]
    full_command = " ".join(command_parts)
    print(f"Joined CLI command: '{full_command}'")

    # .split(): Breaks a string into a list based on delimiter
    csv_row = "192.168.1.50,web-node-01,healthy,8080"
    parsed_fields = csv_row.split(",")
    print(f"Parsed CSV fields: {parsed_fields}")

    # Splitting multi-line strings (e.g., shell output)
    ps_output = "PID\tNAME\n101\tpython\n102\tdocker\n103\tnginx"
    lines = ps_output.splitlines()
    print(f"Splitlines count: {len(lines)} -> {lines}")


    print("\n==================================================")
    print("5. SEQUENCE UNPACKING (HEAD, MIDDLE, TAIL)")
    print("==================================================")

    pipeline_stages = ["checkout", "build", "test", "security_scan", "deploy", "notify"]

    # Unpack first element, middle elements as a sublist, and last element
    first_stage, *middle_stages, final_stage = pipeline_stages
    print(f"First Stage:  {first_stage}")
    print(f"Middle Steps: {middle_stages}")
    print(f"Final Stage:  {final_stage}")


    print("\n==================================================")
    print("6. COPYING LISTS (SHALLOW vs DEEP COPY PITFALL)")
    print("==================================================")

    # PITFALL: Simple assignment '=' only copies the REFERENCE, NOT the data!
    original = ["server-a", "server-b"]
    alias_ref = original
    alias_ref.append("server-c")
    print(f"Notice: 'original' was mutated via 'alias_ref': {original}")

    # 1. Shallow Copy: Creates a new independent list container
    list_x = [1, 2, 3]
    list_y = list_x.copy()  # or list_x[:]
    list_y.append(99)
    print(f"\nShallow copy independent: list_x={list_x}, list_y={list_y}")

    # 2. Deep Copy: Needed when lists contain nested lists / dictionaries
    nested_configs = [["db_host", "localhost"], ["db_port", 5432]]
    shallow_nested = nested_configs.copy()
    deep_nested = copy.deepcopy(nested_configs)

    # Modifying inner element
    nested_configs[0][1] = "10.0.0.15"

    print(f"\nAfter changing inner host to '10.0.0.15':")
    print(f"  Original:       {nested_configs}")
    print(f"  Shallow Copy:   {shallow_nested} (Inner item changed too!)")
    print(f"  Deep Copy:      {deep_nested} (Safely preserved independent copy)")


    print("\n==================================================")
    print("7. REAL-WORLD MINI-SCENARIOS")
    print("==================================================")

    # --- Scenario A: Docker Container Resource Sorter ---
    print("\n--- [Scenario A: Docker Container Resource Sorter] ---")
    containers = [
        {"name": "auth-api", "memory_mb": 512, "cpu_percent": 14.5},
        {"name": "inference-worker", "memory_mb": 4096, "cpu_percent": 88.2},
        {"name": "redis-cache", "memory_mb": 256, "cpu_percent": 3.1},
        {"name": "web-frontend", "memory_mb": 1024, "cpu_percent": 22.0},
    ]

    # Sort containers by highest memory consumption first
    containers_by_memory = sorted(containers, key=lambda c: c["memory_mb"], reverse=True)

    print("Containers ranked by Memory Usage (Highest -> Lowest):")
    for idx, c in enumerate(containers_by_memory, start=1):
        print(f"  {idx}. {c['name']:<18} Memory: {c['memory_mb']:>4} MB | CPU: {c['cpu_percent']}%")

    # --- Scenario B: ML Model Evaluation with zip() ---
    print("\n--- [Scenario B: Model Evaluation & Accuracy Calculation] ---")
    ground_truth_labels = ["cat", "dog", "dog", "cat", "bird", "dog", "bird"]
    model_predictions   = ["cat", "dog", "cat", "cat", "bird", "dog", "dog"]

    correct_predictions = 0
    total_samples = len(ground_truth_labels)

    print(f"Evaluating {total_samples} test predictions:")
    for i, (actual, pred) in enumerate(zip(ground_truth_labels, model_predictions), start=1):
        match = (actual == pred)
        status = "[MATCH]" if match else "[MISMATCH]"
        if match:
            correct_predictions += 1
        print(f"  Sample {i}: Actual='{actual:<4}', Predicted='{pred:<4}' -> {status}")

    accuracy = (correct_predictions / total_samples) * 100
    print(f"\nFinal Model Accuracy: {accuracy:.1f}% ({correct_predictions}/{total_samples} correct)")
    print("==================================================")


if __name__ == "__main__":
    main()
