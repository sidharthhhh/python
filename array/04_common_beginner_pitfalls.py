"""
04_common_beginner_pitfalls.py: Top 5 Traps & Debugging Code Flows

Every beginner encounters these 5 subtle bugs when working with lists.
Understanding WHY these happen will save you days of debugging in automation and AI scripts.
"""


def main():
    print("==================================================")
    print("PITFALL 1: MODIFYING A LIST WHILE ITERATING OVER IT")
    print("==================================================")
    # THE BUG:
    # Python tracks loops using an internal index counter (0, 1, 2, ...).
    # If you remove an item during the loop, all subsequent elements shift left,
    # causing the loop to SKIP the next item!

    # [WRONG APPROACH]:
    numbers = [1, 2, 2, 3, 4]
    print(f"Original list: {numbers}")
    for num in numbers:
        if num == 2:
            numbers.remove(num)
    print(f"[WRONG] Result of removal during loop: {numbers}  <- Notice the second '2' was SKIPPED!")

    # [CORRECT APPROACH 1]: Use a List Comprehension (Recommended)
    numbers_clean = [1, 2, 2, 3, 4]
    numbers_clean = [x for x in numbers_clean if x != 2]
    print(f"[CORRECT] Way 1 (Comprehension): {numbers_clean}")

    # [CORRECT APPROACH 2]: Iterate over a copy using slice [:]
    numbers_copy = [1, 2, 2, 3, 4]
    for num in numbers_copy[:]:  # [:] creates a temporary shallow copy to iterate over
        if num == 2:
            numbers_copy.remove(num)
    print(f"[CORRECT] Way 2 (Slice Copy):    {numbers_copy}\n")


    print("==================================================")
    print("PITFALL 2: ASSIGNING THE RESULT OF IN-PLACE METHODS")
    print("==================================================")
    # In Python, methods that modify a list in-place (.append, .sort, .reverse, .extend)
    # return None!
    # If you assign the result back to your variable, your list becomes None!

    # [WRONG APPROACH]:
    servers = ["web-02", "web-01"]
    result = servers.append("web-03")
    print(f"[WRONG] Assigned .append(): result is '{result}', servers is '{servers}'")

    sorted_result = servers.sort()
    print(f"[WRONG] Assigned .sort():   sorted_result is '{sorted_result}'")

    # [CORRECT APPROACH]:
    # 1. Just call the method without assigning:
    my_tasks = ["task_b", "task_a"]
    my_tasks.append("task_c")  # Just call it
    my_tasks.sort()            # Just call it
    print(f"[CORRECT] In-place call: {my_tasks}")

    # 2. Or use the built-in sorted() if you want a new variable:
    raw_list = [5, 1, 3]
    new_sorted_list = sorted(raw_list)
    print(f"[CORRECT] sorted() function: original={raw_list}, new={new_sorted_list}\n")


    print("==================================================")
    print("PITFALL 3: DEFAULT MUTABLE ARGUMENT IN FUNCTIONS")
    print("==================================================")
    # Default argument values are evaluated ONCE when Python defines the function,
    # NOT every time the function is called!
    # If the default is a mutable list '[]', ALL function calls share the SAME list!

    # [WRONG APPROACH]:
    def buggy_add_log(event, log_list=[]):
        log_list.append(event)
        return log_list

    print("Buggy function calls:")
    first_run = buggy_add_log("Pod Started")
    print(f"  Call 1: {first_run}")
    second_run = buggy_add_log("Pod Crashed")  # Unexpected: contains Call 1's data!
    print(f"  Call 2: {second_run}  <- Shared list bug!")

    # [CORRECT APPROACH]: Use None as default and create a fresh list inside
    def safe_add_log(event, log_list=None):
        if log_list is None:
            log_list = []  # Fresh list created on each call!
        log_list.append(event)
        return log_list

    print("\nSafe function calls:")
    print(f"  Call 1: {safe_add_log('Pod Started')}")
    print(f"  Call 2: {safe_add_log('Pod Crashed')}  <- Clean independent list!\n")


    print("==================================================")
    print("PITFALL 4: VARIABLE ALIASING (REFERENCE vs COPY)")
    print("==================================================")
    # Assigning 'b = a' does NOT copy the list. It creates an alias pointing to the
    # same memory address!

    # [WRONG APPROACH]:
    original_config = ["env=prod", "db=postgres"]
    temp_config = original_config  # Only copies reference!
    temp_config.append("debug=true")

    print(f"[WRONG] Original config was modified unintentionally: {original_config}")

    # [CORRECT APPROACH]: Use .copy() or [:]
    safe_original = ["env=prod", "db=postgres"]
    safe_temp = safe_original.copy()
    safe_temp.append("debug=true")

    print(f"[CORRECT] Safe original: {safe_original}")
    print(f"[CORRECT] Safe copy:     {safe_temp}\n")


    print("==================================================")
    print("PITFALL 5: OFF-BY-ONE IN RANGE() & SLICING BOUNDS")
    print("==================================================")
    # Python ranges and slices are EXCLUSIVE of the end boundary.
    # range(start, end) produces numbers from start up to (end - 1).

    # Want numbers 1 to 5:
    print("range(1, 5) produces:", list(range(1, 5)), "<- Stops at 4!")
    print("range(1, 6) produces:", list(range(1, 6)), "<- Correct 1 to 5!")

    # Slicing: list[0:2] takes index 0 and 1 (2 items, NOT 3)
    items = ["A", "B", "C", "D"]
    print(f"\nitems[0:2] -> {items[0:2]} (Indices 0 and 1)")
    print(f"items[0:3] -> {items[0:3]} (Indices 0, 1, and 2)")
    print("==================================================")


if __name__ == "__main__":
    main()
