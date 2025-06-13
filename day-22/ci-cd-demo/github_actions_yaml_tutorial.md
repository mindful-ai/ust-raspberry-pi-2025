
# 🛠️ GitHub Actions: Writing YAML Workflow Files – A Beginner’s Guide

## 📌 What Are GitHub Actions?

GitHub Actions is a CI/CD platform that allows you to automate workflows like testing, building, and deploying your code whenever you push to your repository.

All workflow definitions are written in `.yml` (YAML) format and stored in:
```
.github/workflows/<workflow-name>.yml
```

---

## 📋 Basic Structure of a Workflow File

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest
```

---

## 🔍 Explanation of Key Sections

### `name:`
Gives your workflow a name that appears in the GitHub Actions UI.

### `on:`
Defines when to trigger the workflow.
Examples:
```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

### `jobs:`
A job is a set of steps that runs in the same environment.

### `runs-on:`
Specifies the virtual machine image for the job.
- Common options: `ubuntu-latest`, `windows-latest`, `macos-latest`

### `steps:`
A list of tasks to perform. These can be GitHub actions or shell commands.

---

## 🎯 Commonly Used Actions

### ✅ Checkout Code
```yaml
- uses: actions/checkout@v4
```

### 🐍 Setup Python
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.10'
```

### 💾 Install Dependencies
```yaml
- run: pip install -r requirements.txt
```

### 🧪 Run Tests with Pytest
```yaml
- run: pytest
```

---

## 🚦 Advanced Examples

### 🧪 Matrix Strategy (Multiple Python Versions)
```yaml
strategy:
  matrix:
    python-version: [3.8, 3.9, 3.10]
```

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - run: pip install -r requirements.txt
    - run: pytest
```

### 🧯 Deploy Only on Merge to Main
```yaml
on:
  push:
    branches:
      - main
```

### 🕹️ Manually Triggered Workflow
```yaml
on:
  workflow_dispatch:
```

---

## 🧠 YAML Tips

| Tip | Why |
|-----|-----|
| Use `:` followed by a space | YAML syntax requirement |
| Use consistent indentation (2 spaces) | YAML is indentation-sensitive |
| Use `run: |` for multi-line commands | Clean formatting |
| Quote strings with colons or special characters | Avoid parsing errors |

---

## 🧪 Validating Your Workflow

1. Create a `.yml` file in `.github/workflows/`
2. Commit and push to GitHub
3. Go to the **Actions** tab in your repo
4. View workflow run logs

---

## ✅ Example: Complete Python CI

```yaml
name: Python CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - uses: actions/setup-python@v5
      with:
        python-version: '3.9'

    - run: pip install -r requirements.txt
    - run: pytest
```

---

## 📘 Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Awesome Actions](https://github.com/sdras/awesome-actions)

Happy Automating! 🚀
