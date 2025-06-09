
# 🧪 Pytest Test Fixtures Guide

## What is a Test Fixture?

In **`pytest`**, a **fixture** is a function used to provide a fixed baseline or setup before tests run. This setup can include creating objects, opening files, or initializing a database connection.

Fixtures help make test code **cleaner**, **more readable**, and **less redundant**.

---

## ✅ Basic Example

### Code under test: `calculator.py`

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

### Test file: `test_calculator.py`

```python
import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_add_negative(calc):
    assert calc.add(-1, -1) == -2
```

In this example, the `calc` fixture provides a `Calculator` instance to each test that needs it.

### Without fixtures

```python

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

```

---

## 🧠 Why Use Fixtures?

- Avoid duplication of setup code
- Share resources (e.g., database connections) across multiple tests
- Improve test readability and maintainability
- Allow complex setup/teardown logic

---

## 🔁 Fixture Scope

You can control how long a fixture lives with the `scope` parameter:

```python
@pytest.fixture(scope="function")  # Default, runs before each test
@pytest.fixture(scope="class")     # Once per class
@pytest.fixture(scope="module")    # Once per module
@pytest.fixture(scope="session")   # Once per entire test session
```

---

## 🔧 Teardown with `yield`

```python
@pytest.fixture
def resource():
    setup = "Start Resource"
    yield setup
    print("Teardown Resource")
```

The code after `yield` runs after the test that uses the fixture finishes, ideal for cleanup logic.

---

## 📦 Summary

| Feature            | Description                                |
|--------------------|--------------------------------------------|
| `@pytest.fixture`  | Declares a reusable setup function          |
| Auto-injected      | Use by naming the fixture in test function |
| Supports teardown  | Using `yield` for setup and cleanup        |
| Configurable scope | `function`, `class`, `module`, `session`   |

---

Happy Testing! 🧪
