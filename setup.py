#!/usr/bin/env python3
"""
Setup script for Bitcoin Volatility Analysis project
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages from requirements.txt"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing packages: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("Creating project directories...")
    directories = ['data/raw', 'data/processed', 'results']
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def main():
    """Main setup function"""
    print("=" * 50)
    print("BITCOIN VOLATILITY ANALYSIS - SETUP")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Install requirements
    if install_requirements():
        print("\n" + "=" * 50)
        print("SETUP COMPLETE!")
        print("=" * 50)
        print("You can now run the analysis with:")
        print("  python main.py")
        print("\nOr install packages manually with:")
        print("  pip install -r requirements.txt")
    else:
        print("\n" + "=" * 50)
        print("SETUP FAILED!")
        print("=" * 50)
        print("Please install packages manually:")
        print("  pip install -r requirements.txt")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
