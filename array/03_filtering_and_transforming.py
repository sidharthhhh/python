"""
03_filtering_and_transforming.py: Step-by-Step Filtering & Transforming

Almost every task in data processing, DevOps, and AI boils down to two operations:
1. FILTERING: Selecting a subset of items that meet a specific condition.
2. TRANSFORMING (Mapping): Modifying every item into a new format or value.

This script breaks down both patterns using manual step-by-step loops first,
then shows how List Comprehensions do the exact same thing concisely.
"""


def main():
    print("==================================================")
    print("1. THE FILTER PATTERN (SELECTING SUBSETS)")
    print("==================================================")
    # MENTAL MODEL:
    # Input List --> Loop through each item --> Condition Check (True/False) --> Collect into New List

    ports = [22, 80, 443, 8080, 3306, 9090, 27017]
    print(f"Original Ports: {ports}")

    # Goal: Filter only web ports (< 1000)
    
    # Approach A: The Explicit Manual Loop
    web_ports_manual = []
    for p in ports:
        if p < 1000:
            web_ports_manual.append(p)
    print(f"[Approach A - Manual Loop] Web ports (<1000): {web_ports_manual}")

    # Approach B: The List Comprehension Equivalent
    # Syntax: [item for item in list if condition]
    web_ports_comp = [p for p in ports if p < 1000]
    print(f"[Approach B - Comprehension] Web ports (<1000): {web_ports_comp}")

    # Practical Filtering Example: Cleaning Training Sentences (AI/NLP)
    sentences = [
        "The quick brown fox",
        "",                  # Empty
        "AI is awesome",
        "Hi",                # Too short (< 3 words)
        "Large language models understand context deeply"
    ]
    # Keep only sentences with at least 3 words
    valid_sentences = [s for s in sentences if len(s.split()) >= 3]
    print(f"\nOriginal Sentences count: {len(sentences)}")
    print(f"Filtered Training Sentences (>=3 words): {valid_sentences}\n")


    print("==================================================")
    print("2. THE TRANSFORMATION (MAP) PATTERN")
    print("==================================================")
    # MENTAL MODEL:
    # Input List --> Loop through each item --> Apply an Expression/Formula --> Collect New Result

    raw_user_inputs = ["   Hello World!  ", "  WHAT IS DOCKER?  ", "  Kubernetes Deploy  "]
    print(f"Raw inputs: {raw_user_inputs}")

    # Goal: Clean whitespace and convert to lowercase for LLM prompt normalization

    # Approach A: The Explicit Manual Loop
    clean_inputs_manual = []
    for text in raw_user_inputs:
        cleaned = text.strip().lower()
        clean_inputs_manual.append(cleaned)
    print(f"[Approach A - Manual Loop] Cleaned: {clean_inputs_manual}")

    # Approach B: The List Comprehension Equivalent
    # Syntax: [expression(item) for item in list]
    clean_inputs_comp = [text.strip().lower() for text in raw_user_inputs]
    print(f"[Approach B - Comprehension] Cleaned: {clean_inputs_comp}")

    # Practical Transform Example: Parsing String Sizes to Integer Megabytes (DevOps)
    raw_memory_strings = ["128MB", "256MB", "1024MB", "512MB"]
    # Strip the "MB" and convert to integer
    memory_integers = [int(m.replace("MB", "")) for m in raw_memory_strings]
    print(f"\nRaw memory strings: {raw_memory_strings}")
    print(f"Parsed integer values: {memory_integers} (Total: {sum(memory_integers)} MB)\n")


    print("==================================================")
    print("3. COMBINED: FILTER + TRANSFORM TOGETHER")
    print("==================================================")
    # Recipe:
    # 1. Filter out unwanted items with 'if condition'
    # 2. Transform the remaining items with 'expression'

    server_logs = [
        "200 OK - 45ms",
        "500 InternalServerError - 820ms",
        "200 OK - 120ms",
        "404 NotFound - 15ms",
        "200 OK - 60ms"
    ]

    # Goal: Extract the latency integer (in ms) from ONLY successful "200 OK" requests

    # Approach A: Manual Loop
    successful_latencies_manual = []
    for log in server_logs:
        if "200 OK" in log:
            # Extract latency: split on "-" -> take second part -> remove "ms" -> convert to int
            ms_str = log.split("-")[1].strip().replace("ms", "")
            successful_latencies_manual.append(int(ms_str))
    print(f"Logs: {server_logs}")
    print(f"[Manual Loop] Successful Latencies: {successful_latencies_manual} ms")

    # Approach B: List Comprehension
    successful_latencies_comp = [
        int(log.split("-")[1].strip().replace("ms", ""))
        for log in server_logs
        if "200 OK" in log
    ]
    print(f"[Comprehension] Successful Latencies: {successful_latencies_comp} ms")
    print(f"Average latency for 200 OK: {sum(successful_latencies_comp)/len(successful_latencies_comp):.1f} ms\n")


    print("==================================================")
    print("4. NESTED LISTS / 2D DATA CODE FLOW")
    print("==================================================")
    # A 2D list is simply a "list of lists".
    # Think of it as rows and columns in a spreadsheet or database table.

    # Table of servers: [Hostname, Environment, CPU_Cores, RAM_GB]
    server_inventory = [
        ["web-prod-01", "production", 8, 32],
        ["web-prod-02", "production", 8, 32],
        ["db-prod-01",  "production", 16, 64],
        ["web-dev-01",  "development", 2, 8],
        ["test-runner", "testing",    4, 16]
    ]

    print("Server Inventory Table:")
    # Outer loop visits each ROW
    for row in server_inventory:
        host, env, cpu, ram = row
        print(f"  Host: {host:<12} | Env: {env:<12} | CPU: {cpu:>2} cores | RAM: {ram:>2} GB")

    # Filtering production rows only:
    prod_servers = [row[0] for row in server_inventory if row[1] == "production"]
    print(f"\nProduction Hostnames: {prod_servers}")

    # Calculating total RAM across production nodes:
    total_prod_ram = sum(row[3] for row in server_inventory if row[1] == "production")
    print(f"Total Production RAM Allocated: {total_prod_ram} GB\n")


    print("==================================================")
    print("5. REAL-WORLD CODE FLOW SCENARIOS")
    print("==================================================")

    # --- Scenario A: Building Security Firewall Rule (DevOps) ---
    print("--- [Scenario A: Security Group Firewall Rule Builder] ---")
    allowed_incoming_ips = [
        "192.168.1.10",
        "10.0.0.1",       # Internal, not public
        "192.168.1.55",
        "0.0.0.0/0",      # Dangerous wild card
        "192.168.1.200"
    ]

    # Rule: Keep only subnet 192.168.1.x and exclude wildcards
    clean_ip_rules = [
        f"--allow-from {ip}"
        for ip in allowed_incoming_ips
        if ip.startswith("192.168.1.") and ip != "0.0.0.0/0"
    ]

    print(f"Raw IP list: {allowed_incoming_ips}")
    print("Generated Firewall Flags:")
    for rule in clean_ip_rules:
        print(f"  {rule}")

    # --- Scenario B: Normalizing Feature Embeddings (AI/ML) ---
    print("\n--- [Scenario B: Min-Max Feature Normalization] ---")
    # In ML, raw feature values are often normalized between 0.0 and 1.0
    # Formula: normalized = (x - min) / (max - min)
    
    raw_feature_values = [10.0, 25.0, 50.0, 75.0, 100.0]
    f_min = min(raw_feature_values)
    f_max = max(raw_feature_values)

    normalized_features = [(x - f_min) / (f_max - f_min) for x in raw_feature_values]

    print(f"Raw Features:        {raw_feature_values}")
    print(f"Normalized (0 to 1): {[round(val, 2) for val in normalized_features]}")
    print("==================================================")


if __name__ == "__main__":
    main()
