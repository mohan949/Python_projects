# How to Run GoRentals Automation

## 🚀 Quick Start (3 Steps)

### 1. Setup
```bash
cd gorentals_automation
python run_tests.py setup-check
```

### 2. Configure
Edit `config/app_config.py`:
- Update APK path: `APPIUM_CONFIG["app"] = "/your/path/goRentals.apk"`
- Update device: `APPIUM_CONFIG["device_name"] = "your-device"`

### 3. Run
```bash
# Start Appium in another terminal
appium

# Run tests
python run_tests.py all
```

---

## 📂 What Each Folder Does

| Folder | Purpose | Key Files |
|--------|---------|-----------|
| `src/` | Core framework code | `base_test.py`, `registration_page.py` |
| `tests/` | Test cases | `test_registration.py` |
| `config/` | Settings & locators | `app_config.py` |
| `utils/` | Tools & runners | `test_runner.py`, `gorentals_inspector.py` |
| `outputs/` | Results (auto-created) | Screenshots, reports, logs |

---

## 🎯 Running Options

### Basic Commands
```bash
# Check setup
python run_tests.py setup-check

# Run all tests
python run_tests.py all

# Run registration tests only
python run_tests.py registration

# Interactive app explorer
python run_tests.py inspector
```

### Advanced Commands
```bash
# Detailed test runner
python utils/test_runner.py

# Specific test class
python utils/test_runner.py TestRegistration

# Individual test file
python tests/test_registration.py
```

---

## 📊 After Running Tests

Check these folders:
- `outputs/screenshots/` - Visual evidence
- `outputs/reports/` - HTML/JSON reports (open .html in browser)
- `outputs/page_sources/` - XML UI structure

---

## 🔧 Common Issues

**App not found?** → Update APK path in `config/app_config.py`

**Device not connected?** → Run `adb devices` and update device name

**Appium not running?** → Start with `appium` command

**Elements not found?** → Use `python run_tests.py inspector` to discover new locators

---

**For detailed explanation, see `PROJECT_GUIDE.md`** 📖 