import subprocess

def test_training_script():
    """Test the training script to ensure it runs without errors."""
    result = subprocess.run(['python', 'train.py', '--epochs', '1'], capture_output=True, text=True)
    assert result.returncode == 0, f"Training script failed with error: {result.stderr}"