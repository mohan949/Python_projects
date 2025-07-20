# General Appium Testing Framework

A collection of general-purpose Appium tests for Android devices and basic app testing.

## 📁 Project Structure

```
general_appium_tests/
├── tests/                    # Test files
│   ├── test_appium.py       # Calculator app test
│   ├── test_basic.py        # Basic device functionality
│   ├── test_settings.py     # Android Settings test
│   └── check_setup.py       # Environment verification
├── outputs/                 # Test results (auto-generated)
├── config/                  # Configuration files
├── utils/                   # Utility scripts
├── docs/                    # Documentation
└── README.md               # This file
```

## 🎯 Purpose

This project contains **general-purpose Appium tests** that can be used to:
- Test basic Android device functionality
- Verify Appium setup and environment
- Test common Android apps (Calculator, Settings)
- Demonstrate Appium capabilities

## 📋 Available Tests

### 1. **Calculator Test** (`test_appium.py`)
- **Purpose**: Tests the Android Calculator app
- **Actions**: Performs basic arithmetic (2 + 3 = 5)
- **Requirements**: Calculator app must be installed
- **Use Case**: Demonstrates basic app automation

### 2. **Basic Device Test** (`test_basic.py`)
- **Purpose**: Tests basic device interactions
- **Actions**: Gestures, key presses, device info
- **Requirements**: Any Android device/emulator
- **Use Case**: Device capability verification

### 3. **Settings Test** (`test_settings.py`)
- **Purpose**: Tests Android Settings app
- **Actions**: Opens Settings, navigates to About
- **Requirements**: Any Android device (Settings always available)
- **Use Case**: System app automation example

### 4. **Setup Checker** (`check_setup.py`)
- **Purpose**: Verifies Appium environment setup
- **Actions**: Checks prerequisites and connectivity
- **Requirements**: Appium environment
- **Use Case**: Environment troubleshooting

## 🚀 How to Run

### Prerequisites
1. **Appium Server**: `appium`
2. **Android Device**: Connected via ADB
3. **Python**: With appium-python-client

### Quick Start
```bash
# Navigate to project
cd general_appium_tests

# Check environment
python tests/check_setup.py

# Run basic test (works on any device)
python tests/test_basic.py

# Run Settings test (works on any device)
python tests/test_settings.py

# Run Calculator test (needs Calculator app)
python tests/test_appium.py
```

## ⚙️ Configuration

### Device Configuration
Update device settings in test files:
```python
# In each test file, update these:
options.device_name = "your-device-name"    # From 'adb devices'
options.platform_version = "your-version"   # Android version
```

### App Requirements
- **Calculator Test**: Requires `com.android.calculator2` or similar
- **Settings Test**: Uses built-in Settings app
- **Basic Test**: No specific app required

## 📊 Test Results

Results are automatically saved to:
- `outputs/` - Screenshots and logs
- Console output with test results
- Error screenshots on failures

## 🔧 Troubleshooting

### Common Issues

1. **Device Not Found**
   ```bash
   adb devices  # Check connected devices
   ```

2. **Appium Not Running**
   ```bash
   appium       # Start Appium server
   ```

3. **Calculator App Missing**
   ```bash
   # Install a calculator app or use different test
   python tests/test_basic.py  # Try this instead
   ```

4. **Environment Issues**
   ```bash
   python tests/check_setup.py  # Diagnose problems
   ```

## 🎯 Use Cases

### Learning Appium
- Start with `test_basic.py` to understand device interaction
- Move to `test_settings.py` for app navigation
- Try `test_appium.py` for specific app testing

### Environment Verification
- Use `check_setup.py` to verify installation
- Run `test_basic.py` to confirm device connectivity

### General Testing
- Test device capabilities with `test_basic.py`
- Verify system apps work with `test_settings.py`
- Test app installation/functionality patterns

## 📈 Best Practices

1. **Start Simple**: Begin with `test_basic.py`
2. **Check Setup**: Always run `check_setup.py` first
3. **Device Specific**: Update device names in tests
4. **Screenshots**: Automatic capture for debugging
5. **Incremental**: Build from basic to complex tests

## 🔄 Integration with Other Projects

This general testing framework complements:
- **goRentals Automation**: Specific app testing
- **CI/CD Pipelines**: Environment verification
- **Learning Projects**: Appium skill development

## 📚 Documentation

- `README.md` - This overview
- Individual test files contain inline documentation
- `check_setup.py` provides environment diagnostics

---

**Purpose**: General-purpose Appium testing for Android devices and basic app functionality verification. 