import sys
import time

def train(epochs: int = 1):
    for epoch in range(epochs):
        print(f"Training epoch {epoch + 1}")
        time.sleep(1)
    print("Training complete!")
    return True

if __name__ == "__main__":
    epochs = int(sys.argv[sys.argv.index("--epochs") + 1]) if "--epochs" in sys.argv else 1
    success = train(epochs)
    if not success:
        sys.exit(1)