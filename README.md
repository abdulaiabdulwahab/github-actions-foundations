# github-actions-foundations
Build a small Python application and create a GitHub Actions CI workflow for automation

# GitHub Actions Foundations Project

This project is a simple introduction to **GitHub Actions** and Continuous Integration (CI).

The goal is to learn how GitHub Actions can automatically test an application whenever code is pushed to a repository or a pull request is created.

## Project Overview

This project contains a small Python calculator application with automated tests.

GitHub Actions is used to:

* Checkout the repository code
* Set up Python
* Install dependencies
* Run automated tests
* Test against multiple Python versions
* Upload test results as workflow artifacts

## Project Structure

```text
github-actions-foundations/
│
├── src/
│   ├── __init__.py
│   └── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Git
* GitHub
* GitHub Actions
* Python
* Pytest
* YAML

## GitHub Actions Workflow

The workflow is stored in:

```text
.github/workflows/ci.yml
```

The workflow runs automatically when:

* Code is pushed to the `main` branch
* A pull request targets the `main` branch
* The workflow is manually triggered

The workflow follows this process:

```text
Git Push / Pull Request
        ↓
GitHub Actions
        ↓
Checkout Code
        ↓
Set Up Python
        ↓
Install Dependencies
        ↓
Run Pytest
        ↓
Upload Test Results
```

## Matrix Testing

The workflow tests the application using multiple Python versions:

```text
Python 3.11
Python 3.12
Python 3.13
```

This demonstrates how a GitHub Actions **matrix strategy** can run the same job using different configurations.

## Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/abdulaiabdulwahab/github-actions-foundations.git
```

Navigate into the project:

```bash
cd github-actions-foundations
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
pytest -v
```

A successful test run should show all tests passing.

## Key GitHub Actions Concepts Learned

This project demonstrates several core GitHub Actions concepts:

* **Workflow** — the complete automation pipeline
* **Event** — something that triggers the workflow
* **Job** — a group of steps executed on a runner
* **Step** — an individual command or reusable action
* **Runner** — the virtual machine that executes the job
* **Action** — reusable automation used inside a workflow
* **Matrix** — runs the same job using multiple configurations
* **Artifact** — files saved from a workflow run
* **workflow_dispatch** — allows manual workflow execution

## Troubleshooting Practiced

The project also provides opportunities to troubleshoot common CI issues such as:

* Workflow not triggering
* Incorrect branch configuration
* Python dependency installation failures
* Module import errors
* Failed automated tests
* Matrix jobs failing on specific Python versions
* Missing workflow artifacts

## What I Learned

By completing this project, I gained practical experience creating a basic Continuous Integration pipeline using GitHub Actions.

I learned how GitHub Actions can automatically validate code changes, execute tests across multiple environments, store workflow artifacts, and provide fast feedback when code changes introduce errors.

## Next Step

The next project builds on these fundamentals by using GitHub Actions to create a CI/CD pipeline that authenticates securely with Microsoft Azure and deploys an application to Azure App Service.
