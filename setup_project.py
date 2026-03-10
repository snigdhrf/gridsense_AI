import os

# Project structure
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "models",
    "dashboard",
    "configs",
    "tests"
]

files = [
    "README.md",
    "requirements.txt",
    "src/data_pipeline.py",
    "src/features.py",
    "src/forecast_model.py",
    "src/anomaly_detection.py",
    "src/utils.py",
    "notebooks/01_data_exploration.ipynb"
]

def create_folders(base_path):
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

def create_files(base_path):
    for file in files:
        path = os.path.join(base_path, file)
        if not os.path.exists(path):
            with open(path, "w") as f:
                pass
            print(f"Created file: {path}")

def main():
    base_path = os.getcwd()
    print(f"Creating GridSense project structure in: {base_path}")

    create_folders(base_path)
    create_files(base_path)

    print("\nProject structure created successfully!")

if __name__ == "__main__":
    main()