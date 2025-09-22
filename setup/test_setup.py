#!/usr/bin/env python3
"""
Test script to verify Bitcoin Volatility Analysis setup
"""

import sys
import importlib
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing package imports...")
    
    required_packages = [
        'pandas',
        'numpy', 
        'yfinance',
        'scipy',
        'matplotlib'
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package}")
            failed_imports.append(package)
    
    return failed_imports

def test_project_structure():
    """Test if project structure is correct"""
    print("\nTesting project structure...")
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    required_files = [
        'main.py',
        'setup/requirements.txt',
        'setup/setup.py',
        'src/data_collection/bitcoin_prices.py',
        'src/data_collection/market_events.py',
        'src/analysis/descriptive_stats.py',
        'src/analysis/distribution_analysis.py',
        'src/analysis/hypothesis_tests.py',
        'src/visualization/plots.py'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if (repo_root / file_path).exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path}")
            missing_files.append(file_path)
    
    return missing_files

def test_data_collection():
    """Test data collection functions"""
    print("\nTesting data collection functions...")
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    try:
        # Add src to path
        sys.path.insert(0, str(repo_root / 'src'))
        
        from data_collection.bitcoin_prices import collect_bitcoin_data
        from data_collection.market_events import create_events_database
        
        # Test market events (doesn't require internet)
        events = create_events_database()
        print(f"✓ Market events database: {len(events)} events")
        
        # Test Bitcoin data collection (requires internet)
        print("Testing Bitcoin data collection (requires internet)...")
        btc_data = collect_bitcoin_data('2024-01-01', '2024-01-31')  # Small date range for testing
        if btc_data is not None:
            print(f"✓ Bitcoin data collection: {len(btc_data)} records")
        else:
            print("✗ Bitcoin data collection failed")
            return False
            
    except Exception as e:
        print(f"✗ Data collection test failed: {e}")
        return False
    
    return True

def main():
    """Main test function"""
    print("=" * 50)
    print("BITCOIN VOLATILITY ANALYSIS - TEST")
    print("=" * 50)
    
    # Test imports
    failed_imports = test_imports()
    
    # Test project structure
    missing_files = test_project_structure()
    
    # Test data collection
    data_test_passed = test_data_collection()
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    
    if failed_imports:
        print(f"✗ Failed imports: {', '.join(failed_imports)}")
        print("  Run: pip install -r setup/requirements.txt")
    else:
        print("✓ All imports successful")
    
    if missing_files:
        print(f"✗ Missing files: {', '.join(missing_files)}")
    else:
        print("✓ Project structure complete")
    
    if data_test_passed:
        print("✓ Data collection functions working")
    else:
        print("✗ Data collection functions failed")
    
    if not failed_imports and not missing_files and data_test_passed:
        print("\n🎉 ALL TESTS PASSED! The project is ready to use.")
        print("Run: python main.py")
        return 0
    else:
        print("\n❌ Some tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
