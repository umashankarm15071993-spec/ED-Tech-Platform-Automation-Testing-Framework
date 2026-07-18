# 🎓 ED Tech Platform Automation Testing Framework

## 📌 Project Overview

This project is an end-to-end web automation testing framework developed using **Python**, **Selenium WebDriver**, and **Pytest**. The framework follows the **Page Object Model (POM)** design pattern to create a reusable, maintainable, and scalable test automation solution.

The framework automates key functionalities of the ED Tech Platform, including homepage validation, user login, signup, logout, and UI element verification. It also supports Data-Driven Testing (DDT), detailed reporting, logging, and automatic screenshot capture for failed test cases.

---

# 🚀 Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- OpenPyXL
- Pytest HTML Report
- Allure Report
- Logging
- Git & GitHub

---

# ✨ Features Implemented

- Page Object Model (POM)
- Cross Browser Testing (Chrome, Firefox & Edge)
- Data-Driven Testing (DDT) using Excel
- Dynamic Browser Selection
- Explicit Waits
- Implicit Waits
- Reusable Base Page Methods
- Exception Handling
- Logging
- Automatic Screenshot Capture on Test Failure
- HTML Report Generation
- Allure Report Generation

---

# 📂 Project Structure

```text
Guvi_projects/
│
├── pages/
├── tests/
├── utilities/
├── reports/
├── screenshot/
├── logs/
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ✅ Automated Test Scenarios

## Home Page

- Verify Application URL
- Verify Page Title
- Verify Login Button
- Verify Sign Up Button
- Verify Navigation Menu
- Verify Chatbot Availability

## Login Module

- Verify Login with Valid Credentials
- Verify Login with Invalid Credentials (DDT using Excel)
- Verify Logout Functionality

## Sign Up Module

- Verify Sign Up Page Navigation

---

# 📊 Reporting

### HTML Report

Generate the HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

### Allure Report

Generate Allure Results:

```bash
pytest --alluredir=allure-results
```

Generate Allure HTML Report:

```bash
allure generate allure-results -o reports/allure-report --clean
```

Open Allure Report:

```bash
allure open reports/allure-report
```

---

# ▶️ Execute Test Suite

Run all test cases:

```bash
pytest
```

Run tests on Chrome:

```bash
pytest --browser=chrome
```

Run tests on Firefox:

```bash
pytest --browser=firefox
```

Run tests on Edge:

```bash
pytest --browser=edge
```

---

# 📸 Screenshot Capture

The framework automatically captures screenshots whenever a test case fails. The screenshots are stored in the **screenshot** folder for debugging and analysis.

---

# 📝 Logging

The framework uses Python's **logging** module to record test execution details, making it easier to trace execution flow and troubleshoot failures.

---

# 🔮 Future Enhancements

- Jenkins CI/CD Integration
- Parallel Test Execution using Pytest-xdist

---

# 👨‍💻 Author

**Uma Shankar M**

QA Automation Engineer

**Skills:** Python | Selenium | Pytest | POM | DDT | HTML Reports | Allure Reports | Git | GitHub

---

## ⭐ Note

This project was developed for learning, hands-on practice, and portfolio purposes to demonstrate automation testing skills using Python Selenium and Pytest.