import os

print("Step 1: Training model...")
os.system("python train.py")

print("Step 2: Starting API server...")
os.system("python app.py")
