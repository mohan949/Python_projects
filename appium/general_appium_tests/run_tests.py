#!/usr/bin/env python3
"""
Simple test runner for General Appium Tests
Provides easy commands to run different types of tests
"""

import sys
import subprocess
import os
from pathlib import Path

def show_help():
    """Show available commands"""
    print("""
General Appium Tests Runner

Usage: python run_tests.py [command]

Commands:
  check            Check environment setup
  basic            Run basic device test
  settings         Run Settings app test
  calculator       Run Calculator app test
  all              Run all available tests
  help             Show this help message

Examples:
  python run_tests.py check
  python run_tests.py basic
  python run_tests.py all
""")

def run_command(command, description):
    """Run a command and show the description"""
    print(f"\n🚀 {description}")
    print("=" * 50)
    
    try:
        result = subprocess.run(f"python {command}", shell=True, cwd=Path(__file__).parent)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running command: {e}")
        return False

def main():
    """Main function"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "help" or command == "-h" or command == "--help":
        show_help()
        
    elif command == "check":
        run_command("tests/check_setup.py", "Checking environment setup")
        
    elif command == "basic":
        run_command("tests/test_basic.py", "Running basic device test")
        
    elif command == "settings":
        run_command("tests/test_settings.py", "Running Settings app test")
        
    elif command == "calculator":
        run_command("tests/test_appium.py", "Running Calculator app test")
        
    elif command == "all":
        print("🚀 Running all available tests")
        print("=" * 50)
        
        tests = [
            ("tests/check_setup.py", "Environment Check"),
            ("tests/test_basic.py", "Basic Device Test"),
            ("tests/test_settings.py", "Settings App Test"),
            ("tests/test_appium.py", "Calculator Test")
        ]
        
        results = []
        for test_file, description in tests:
            print(f"\n▶️ {description}")
            print("-" * 30)
            success = run_command(test_file, description)
            results.append((description, success))
        
        print("\n" + "=" * 50)
        print("📊 TEST SUMMARY")
        print("=" * 50)
        
        for description, success in results:
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{status} - {description}")
            
    else:
        print(f"Unknown command: {command}")
        show_help()

if __name__ == "__main__":
    main() 