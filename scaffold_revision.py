import os
import shutil

# Define the new structure mapping (Old -> New) or Just Create New
# We will just ensure the new directories exist and rename useful old ones if they match logic

moves = {
    "days/day02_advanced_patterns": "days/archive_advanced_patterns", # Save for later
    "days/day02_modern_tooling": "days/day04_modern_tooling",
}

creates = [
    "days/day02_io_modules",
    "days/day03_oop_basics",
    "days/day05_testing",
    "days/day06_devops_scripting",
    "days/day08_docker",
    "days/day09_aws_boto3",
    "days/day10_data_pandas",
    "days/day11_ml_basics",
    "days/day12_fastapi",
    "days/day13_mlflow",
    "days/day14_prefect",
]

base_dir = r"C:\Users\Sidharth\Desktop\python"

for old, new in moves.items():
    old_path = os.path.join(base_dir, old)
    new_path = os.path.join(base_dir, new)
    if os.path.exists(old_path):
        print(f"Moving {old} -> {new}")
        os.renames(old_path, new_path)

for folder in creates:
    path = os.path.join(base_dir, folder)
    if not os.path.exists(path):
        print(f"Creating {folder}")
        os.makedirs(path)
        # Create a placeholder README
        with open(os.path.join(path, "README.md"), "w") as f:
            f.write(f"# {folder.split('/')[-1]}\n\nContent coming soon.")

print("Restructure complete.")
