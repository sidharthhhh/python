"""
02_loops_and_code_flow.py: Mastering Code Flows with Loops & Control Statements

Before learning advanced patterns, you must master how Python executes code step-by-step:
1. How a `for` loop moves through a list element by element.
2. The Accumulator Pattern (building totals, counters, and new collector lists).
3. `break` statement: Stopping immediately when a condition is met (Early Exit).
4. `continue` statement: Skipping unwanted elements and moving to the next iteration.
5. `for ... else` block: Detecting whether a loop completed fully or exited early.
6. `while` loops with lists: Draining task queues until empty.
"""


def main():
    print("==================================================")
    print("1. HOW A FOR LOOP WORKS (STEP-BY-STEP TRACING)")
    print("==================================================")

    # When you write: for item in items:
    # Python assigns the next element from the list to 'item' on every pass.
    
    server_pool = ["web-01", "web-02", "web-03"]
    
    print(f"Target list: {server_pool}")
    print("Loop execution starts:")
    
    step = 1
    for server in server_pool:
        print(f"  [Pass #{step}] -> Variable 'server' is currently holding: '{server}'")
        # You do your work here on 'server'
        print(f"               Pinging {server}... [OK]")
        step += 1
        
    print("Loop finished! Execution continues to the next block.\n")


    print("==================================================")
    print("2. THE ACCUMULATOR PATTERN")
    print("==================================================")
    # The Accumulator Pattern is the most fundamental coding pattern.
    # Recipe:
    # 1. Initialize an accumulator variable (0, 0.0, "", or []) BEFORE the loop.
    # 2. Iterate through the list.
    # 3. Update the accumulator inside the loop.
    # 4. Use the accumulated result AFTER the loop.

    # Example A: Running Sum & Average (Tracking Memory Usage)
    memory_usages_mb = [256, 512, 128, 1024, 512]
    total_memory = 0  # 1. Initialize accumulator

    for mem in memory_usages_mb:
        total_memory += mem  # 3. Update accumulator

    avg_memory = total_memory / len(memory_usages_mb)
    print(f"Memory list: {memory_usages_mb}")
    print(f"Total Memory: {total_memory} MB")
    print(f"Average Memory: {avg_memory:.2f} MB")

    # Example B: The Collector List Pattern (Accumulating matching items)
    all_status_codes = [200, 404, 200, 500, 502, 200, 403]
    failed_requests = []  # 1. Initialize empty collector list

    for code in all_status_codes:
        if code >= 400:
            failed_requests.append(code)  # 3. Collect item

    print(f"\nAll status codes: {all_status_codes}")
    print(f"Collected failed requests: {failed_requests}")
    print(f"Failure rate: {(len(failed_requests) / len(all_status_codes)) * 100:.1f}%\n")


    print("==================================================")
    print("3. EARLY EXIT WITH 'break'")
    print("==================================================")
    # 'break' immediately terminates the current loop.
    # Use case: Why scan 10,000 items if you found what you needed on item #3?

    log_stream = [
        "INFO: Database connected",
        "INFO: Auth token verified",
        "FATAL: Database connection lost!",
        "INFO: User logged in",
        "INFO: Page rendered"
    ]

    print("Scanning log stream for critical failures:")
    critical_error_found = False

    for idx, log in enumerate(log_stream, start=1):
        print(f"  Checking line {idx}: '{log}'")
        if "FATAL" in log:
            print("  --> [!] FATAL ERROR DETECTED! Stopping scan immediately with 'break'.")
            critical_error_found = True
            break  # Stops the loop right here! Lines after this will NOT be processed.

    print(f"Scan finished early. Alert trigger status: {critical_error_found}\n")


    print("==================================================")
    print("4. SKIPPING UNWANTED ITEMS WITH 'continue'")
    print("==================================================")
    # 'continue' stops the CURRENT iteration and jumps immediately to the NEXT iteration.
    # Use case: Skip comments, empty lines, null values, or invalid inputs.

    config_lines = [
        "PORT=8080",
        "# This is a comment explaining the database",
        "DB_HOST=127.0.0.1",
        "",  # Empty blank line
        "# Another comment",
        "LOG_LEVEL=DEBUG",
        "   "  # Whitespace only line
    ]

    valid_configs = []

    print("Parsing config lines (skipping comments and blank lines):")
    for line in config_lines:
        cleaned = line.strip()
        
        # Guard clause 1: Skip empty strings
        if not cleaned:
            # print("  [Skipping blank line]")
            continue
            
        # Guard clause 2: Skip comments starting with '#'
        if cleaned.startswith("#"):
            # print(f"  [Skipping comment: {cleaned}]")
            continue
            
        # If we reached here, the line is a valid config!
        print(f"  [+] Valid setting parsed: {cleaned}")
        valid_configs.append(cleaned)

    print(f"Final parsed configs list: {valid_configs}\n")


    print("==================================================")
    print("5. PYTHON'S UNIQUE 'for ... else' CONSTRUCT")
    print("==================================================")
    # In Python, a 'for' loop can have an 'else' block!
    # The 'else' block runs ONLY IF the loop completed normally (i.e. NO 'break' was hit).
    # If a 'break' occurs, the 'else' block is completely SKIPPED.

    # Scenario 1: All servers healthy -> loop completes -> 'else' runs
    cluster_a = ["healthy", "healthy", "healthy"]
    print(f"Testing Cluster A: {cluster_a}")
    for node in cluster_a:
        if node != "healthy":
            print("  [!] Found unhealthy node! Breaking.")
            break
    else:
        print("  -> [for-else executed]: ALL nodes in Cluster A are healthy! [OK]")

    # Scenario 2: One server degraded -> hits 'break' -> 'else' is skipped
    cluster_b = ["healthy", "degraded", "healthy"]
    print(f"\nTesting Cluster B: {cluster_b}")
    for node in cluster_b:
        if node != "healthy":
            print(f"  [!] Found '{node}' node! Breaking out.")
            break
    else:
        print("  -> This will NOT print because break was triggered.")


    print("\n==================================================")
    print("6. 'while' LOOPS WITH LISTS (DRAINING QUEUES)")
    print("==================================================")
    # While loops run as long as a condition is True.
    # In Python, an empty list '[]' is Falsy, and a non-empty list is Truthy!
    # Therefore: 'while task_queue:' means 'while task_queue is not empty'.

    deployment_queue = ["deploy_backend", "run_migrations", "deploy_frontend", "purge_cdn"]
    print(f"Initial Deployment Queue: {deployment_queue}")

    step_num = 1
    while deployment_queue:
        # .pop(0) extracts the first item from the queue (FIFO - First In First Out)
        current_task = deployment_queue.pop(0)
        print(f"  Step {step_num}: Executing '{current_task}'... Done! Remaining in queue: {deployment_queue}")
        step_num += 1

    print("Queue is now completely empty. Deployment finished successfully!\n")


    print("==================================================")
    print("7. REAL-WORLD CODE FLOW SCENARIOS")
    print("==================================================")

    # --- Scenario A: Retry Loop with Backoff Counter ---
    print("--- [Scenario A: API Health Checker with Retries] ---")
    simulated_server_responses = ["ConnectionRefused", "Timeout", "200_OK"]
    max_retries = 3
    attempt = 1
    connected = False

    for response in simulated_server_responses:
        print(f"Attempt {attempt}/{max_retries}: Contacting API server... Response: '{response}'")
        if response == "200_OK":
            print("  -> Connection established successfully! [OK]")
            connected = True
            break
        else:
            print("  -> Connection failed. Retrying next attempt...")
        attempt += 1

    if not connected:
        print("  -> [ALERT] Failed to connect after all retry attempts.")

    # --- Scenario B: Batching Token Sequence until Max Length ---
    print("\n--- [Scenario B: LLM Prompt Token Accumulator] ---")
    # Say we have incoming user paragraphs and we want to pack them into a prompt
    # without exceeding MAX_WORDS = 15 words.
    
    incoming_paragraphs = [
        "Python is a versatile programming language.",     # 6 words
        "It is widely used in DevOps, Cloud, and AI.",     # 8 words (Total: 14)
        "Large language models rely on deep learning.",     # 7 words (Would exceed 15 -> STOP)
        "Automation saves engineering hours."               # 4 words
    ]

    MAX_WORDS = 15
    packed_prompt_lines = []
    current_word_count = 0

    for paragraph in incoming_paragraphs:
        words = paragraph.split()
        num_words = len(words)
        
        if current_word_count + num_words > MAX_WORDS:
            print(f"  Stopping pack: adding '{paragraph}' ({num_words} words) would exceed limit {MAX_WORDS}.")
            break
            
        packed_prompt_lines.append(paragraph)
        current_word_count += num_words
        print(f"  Added: '{paragraph}' | Current word total: {current_word_count}/{MAX_WORDS}")

    print(f"\nFinal packed prompt ({current_word_count} words):")
    for line in packed_prompt_lines:
        print(f"  > {line}")
    print("==================================================")


if __name__ == "__main__":
    main()
