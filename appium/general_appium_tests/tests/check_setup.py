#!/usr/bin/env python3
"""
Check if all prerequisites for running Appium tests are met.
"""

import subprocess
import sys

def run_command(cmd):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return 1, "", str(e)

def check_requirement(name, cmd, success_condition=lambda rc, out, err: rc == 0):
    """Check if a requirement is met."""
    print(f"\nChecking {name}...")
    returncode, stdout, stderr = run_command(cmd)
    
    if success_condition(returncode, stdout, stderr):
        print(f"✅ {name} is installed")
        if stdout:
            print(f"   Version: {stdout}")
        return True
    else:
        print(f"❌ {name} is NOT installed or not configured properly")
        if stderr:
            print(f"   Error: {stderr}")
        return False

def main():
    print("=" * 60)
    print("Appium Test Setup Checker")
    print("=" * 60)
    
    requirements_met = True
    
    # Check Python
    check_requirement("Python", "python --version")
    
    # Check Appium Python Client
    if not check_requirement("Appium Python Client", "pip show appium-python-client | grep Version"):
        requirements_met = False
        print("   Install with: pip install Appium-Python-Client")
    
    # Check Node.js
    if not check_requirement("Node.js", "node --version"):
        requirements_met = False
        print("   Install from: https://nodejs.org/")
    
    # Check npm
    if not check_requirement("npm", "npm --version"):
        requirements_met = False
        print("   npm should come with Node.js")
    
    # Check Appium
    if not check_requirement("Appium", "appium --version 2>/dev/null | tail -1"):
        requirements_met = False
        print("   Install with: npm install -g appium")
    
    # Check Java
    if not check_requirement("Java", "java -version 2>&1 | head -1"):
        requirements_met = False
        print("   Install JDK from: https://adoptium.net/")
    
    # Check Android SDK
    if not check_requirement("Android SDK (adb)", "adb version | head -1"):
        requirements_met = False
        print("   Install Android Studio from: https://developer.android.com/studio")
    
    # Check connected devices
    print("\nChecking Android devices...")
    rc, out, err = run_command("adb devices | grep -v 'List of devices' | grep -v '^$' | wc -l")
    device_count = int(out.strip()) if out.strip().isdigit() else 0
    
    if device_count > 0:
        print(f"✅ {device_count} Android device(s) connected")
        run_command("adb devices")
    else:
        print("⚠️  No Android devices or emulators connected")
        print("   Start an emulator or connect a device")
        requirements_met = False
    
    # Check if Appium server is running
    print("\nChecking Appium server...")
    rc, out, err = run_command("curl -s http://localhost:4723/status")
    
    if rc == 0 and "ready" in out.lower():
        print("✅ Appium server is running on localhost:4723")
    else:
        print("⚠️  Appium server is NOT running")
        print("   Start with: appium")
        requirements_met = False
    
    print("\n" + "=" * 60)
    if requirements_met:
        print("✅ All requirements are met! You can run: python test_appium.py")
    else:
        print("❌ Some requirements are missing. Please install them first.")
    print("=" * 60)
    
    return 0 if requirements_met else 1

if __name__ == "__main__":
    sys.exit(main()) 