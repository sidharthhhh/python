"""
01_basics.py: Python Lists - Fundamentals & Practical Mechanics

Lists are the single most important built-in data structure in Python.
Whether you are:
- Collecting logs from 50 Kubernetes pods (DevOps)
- Batching user prompts for an LLM (GenAI)
- Storing feature values and training loss history (AI/ML)
...you will use Python lists every single day.
"""


def main():
    print("==================================================")
    print("1. CREATING LISTS")
    print("==================================================")

    # Empty list (used as a collector in loops)
    empty_list = []
    print(f"Empty list: {empty_list}")

    # Populated lists
    server_names = ["web-01", "web-02", "db-primary", "cache-01"]
    status_codes = [200, 200, 404, 500, 200]
    mixed_info = ["gpt-4o", 0.7, 4096, True]  # model_name, temperature, max_tokens, stream

    print(f"Servers (strings): {server_names}")
    print(f"Status codes (ints): {status_codes}")
    print(f"LLM Config (mixed): {mixed_info}")

    # Generating lists with range()
    epoch_numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
    print(f"Epoch numbers: {epoch_numbers}")

    # Repeating elements (useful for pre-allocating default values or masks)
    initial_weights = [0.0] * 4  # [0.0, 0.0, 0.0, 0.0]
    print(f"Initialized weights: {initial_weights}")

    # Creating a list from a string (splitting logs or CSV rows)
    raw_log = "INFO,2026-09-03,service-auth,authenticated"
    log_parts = raw_log.split(",")
    print(f"Split log line into list: {log_parts}")


    print("\n==================================================")
    print("2. ACCESSING ELEMENTS (INDEXING)")
    print("==================================================")

    # 0-based indexing (first element is at index 0)
    first_server = server_names[0]
    second_server = server_names[1]
    print(f"First server: {first_server}")
    print(f"Second server: {second_server}")

    # Negative Indexing: Count backwards from the end!
    # -1 is ALWAYS the last element (super useful for latest log/status)
    latest_server = server_names[-1]
    second_last = server_names[-2]
    print(f"Latest (last) server via [-1]: {latest_server}")
    print(f"Second-to-last server via [-2]: {second_last}")

    # Safe access tip: Always verify index < len(list) or handle IndexError
    try:
        non_existent = server_names[10]
    except IndexError:
        print("Note: Accessing an out-of-bounds index raises IndexError (handled safely).")


    print("\n==================================================")
    print("3. SLICING LISTS (EXTRACTING SUBSETS)")
    print("==================================================")
    # Syntax: list[start : end : step]
    # start is inclusive, end is exclusive

    predictions = ["cat", "dog", "fox", "bear", "lion", "wolf"]
    print(f"Full predictions: {predictions}")

    # Top-3 predictions (from index 0 up to index 3)
    top_3 = predictions[:3]
    print(f"Top-3 predictions [:3]: {top_3}")

    # Tail items (from index 3 onwards to the end)
    remaining = predictions[3:]
    print(f"Remaining from index 3 [3:]: {remaining}")

    # Middle slice (index 1 to 4)
    middle = predictions[1:4]
    print(f"Middle slice [1:4]: {middle}")

    # Step slice (every 2nd element - useful for downsampling data)
    downsampled = predictions[::2]
    print(f"Every 2nd element [::2]: {downsampled}")

    # Reverse a list using slicing
    reversed_predictions = predictions[::-1]
    print(f"Reversed list [::-1]: {reversed_predictions}")


    print("\n==================================================")
    print("4. ADDING & COMBINING ELEMENTS")
    print("==================================================")

    active_tasks = ["lint_code", "run_tests"]
    print(f"Initial tasks: {active_tasks}")

    # .append(): Adds a single item to the END of the list (most common)
    active_tasks.append("build_docker_image")
    print(f"After .append('build_docker_image'): {active_tasks}")

    # .insert(): Inserts an item at a specific index (pushes existing elements right)
    active_tasks.insert(0, "checkout_repo")  # Put at the very beginning
    print(f"After .insert(0, 'checkout_repo'): {active_tasks}")

    # .extend(): Adds multiple items from another list/iterable
    post_deploy_tasks = ["run_smoke_tests", "send_slack_alert"]
    active_tasks.extend(post_deploy_tasks)
    print(f"After .extend(post_deploy_tasks): {active_tasks}")

    # Combining lists using the '+' operator (creates a new list)
    group_a = ["model_v1", "model_v2"]
    group_b = ["model_v3", "model_v4"]
    all_models = group_a + group_b
    print(f"Combined with '+': {all_models}")


    print("\n==================================================")
    print("5. REMOVING ELEMENTS")
    print("==================================================")

    queue = ["job_101", "job_102", "job_103", "job_104", "job_105"]
    print(f"Queue: {queue}")

    # .pop(): Removes and returns the LAST item (default)
    last_job = queue.pop()
    print(f"Popped last item: '{last_job}', Queue now: {queue}")

    # .pop(0): Removes and returns the FIRST item (FIFO queue behavior)
    first_job = queue.pop(0)
    print(f"Popped index 0: '{first_job}', Queue now: {queue}")

    # .remove(value): Searches for the FIRST occurrence of value and removes it
    queue.remove("job_103")
    print(f"After .remove('job_103'): {queue}")

    # del keyword: Remove item by index or remove a slice
    del queue[0]
    print(f"After del queue[0]: {queue}")

    # .clear(): Empties the entire list
    temp_list = [1, 2, 3]
    temp_list.clear()
    print(f"After .clear(): {temp_list}")


    print("\n==================================================")
    print("6. ESSENTIAL BUILT-IN INSPECTION FUNCTIONS")
    print("==================================================")

    loss_values = [0.82, 0.64, 0.45, 0.31, 0.28]

    # Length of a list
    print(f"Number of epochs recorded: {len(loss_values)}")

    # Checking membership with 'in' and 'not in'
    servers = ["api-gw", "auth-svc", "billing-svc"]
    print(f"Is 'auth-svc' in servers? {'auth-svc' in servers}")
    print(f"Is 'search-svc' missing? {'search-svc' not in servers}")

    # Numerical summaries (very common in metrics & ML evaluation)
    print(f"Initial loss (max): {max(loss_values)}")
    print(f"Final loss (min): {min(loss_values)}")
    print(f"Sum of losses: {sum(loss_values):.4f}")
    print(f"Average loss: {sum(loss_values) / len(loss_values):.4f}")

    # any() and all() checks (super useful in DevOps health checks)
    health_checks = [True, True, True, False]
    print(f"Are all checks passing (all)? {all(health_checks)}")  # False
    print(f"Did at least one check pass (any)? {any(health_checks)}")  # True


    print("\n==================================================")
    print("7. REAL-WORLD MINI-SCENARIOS")
    print("==================================================")

    # --- Scenario A (DevOps): Server Health & HTTP Status Tracker ---
    print("\n--- [Scenario A: DevOps Server Health Tracker] ---")
    http_responses = [200, 200, 200, 502, 200, 504, 200]

    # Quick check for errors:
    error_codes = []
    for code in http_responses:
        if code >= 400:
            error_codes.append(code)

    print(f"Total requests: {len(http_responses)}")
    print(f"Error count: {len(error_codes)} (Errors found: {error_codes})")
    status_msg = "UNHEALTHY [!]" if len(error_codes) > 0 else "HEALTHY [OK]"
    print(f"System status: {status_msg}")

    # --- Scenario B (GenAI): Chat History Context Window Manager ---
    print("\n--- [Scenario B: GenAI Chat History Manager] ---")
    # In LLMs, chat messages are stored as a list of message strings or dicts.
    chat_history = [
        "System: You are an AI cloud assistant.",
        "User: How do I deploy a Docker container?",
        "Assistant: Use 'docker run -d -p 80:80 my-image'.",
        "User: How do I check its logs?",
        "Assistant: Use 'docker logs <container_id>'.",
        "User: How do I stop it?",
        "Assistant: Use 'docker stop <container_id>'."
    ]

    # If the history is too long for LLM token limits, keep only the System prompt + Last 4 messages
    MAX_MESSAGES = 4
    system_prompt = chat_history[0]
    recent_messages = chat_history[-MAX_MESSAGES:]

    trimmed_history = [system_prompt] + [msg for msg in recent_messages if msg != system_prompt]
    print("Trimmed Chat Context for LLM prompt:")
    for msg in trimmed_history:
        print(f"  * {msg}")

    # --- Scenario C (AI/ML): Epoch Loss & Metric Progression ---
    print("\n--- [Scenario C: AI/ML Loss Progression Tracker] ---")
    epoch_losses = [1.25, 0.89, 0.62, 0.41, 0.38]

    print(f"Training started with Loss: {epoch_losses[0]}")
    print(f"Training ended with Loss:   {epoch_losses[-1]}")
    improvement = epoch_losses[0] - epoch_losses[-1]
    print(f"Total Loss Improvement:     {improvement:.4f}")
    print("==================================================")


if __name__ == "__main__":
    main()
