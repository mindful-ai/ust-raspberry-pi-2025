# 🐒 Monkey Patching in Python

## 📌 What is Monkey Patching?

**Monkey patching** is the dynamic (runtime) modification of a class, method, or module in Python. It allows you to change or extend the behavior of libraries **without modifying their original source code**.

---

## 🤔 Why is it Called "Monkey" Patching?

The term comes from the idea of a monkey randomly changing or "patching" things — it’s **clever**, but can also be **risky** if used carelessly.

---

## 🔧 Example 1: Overriding a Method at Runtime

```python
class Greet:
    def say_hello(self):
        print("Hello")

def new_greeting(self):
    print("Hello, patched world!")

# Monkey patching the method
Greet.say_hello = new_greeting

g = Greet()
g.say_hello()  # Output: Hello, patched world!
```

✅ We changed the behavior of `say_hello()` without modifying the original class definition.

---

## 🔌 Example 2: Monkey Patching a Module Function

```python
import math

# Original behavior
print(math.sqrt(4))  # Output: 2.0

# Monkey patch
math.sqrt = lambda x: "This is not a square root"

print(math.sqrt(4))  # Output: This is not a square root
```

🔴 This should generally be avoided unless absolutely necessary.

---

## 📦 Real-World Example: `eventlet.monkey_patch()`

```python
import eventlet
eventlet.monkey_patch()

# After this, modules like `socket`, `time`, and `threading` become cooperative and non-blocking
```

This is often used in asynchronous applications like **Flask-SocketIO** to support thousands of concurrent users via WebSockets.

---

## ✅ When to Use Monkey Patching

- ✅ For **temporary fixes** or quick solutions
- ✅ In **unit testing** to mock functions or methods
- ✅ To integrate **async behavior** using frameworks like `eventlet` or `gevent`

---

## ⚠️ Use With Caution

Monkey patching can:
- ❌ Make code harder to maintain and debug
- ❌ Cause unexpected side effects
- ❌ Break when dependencies are updated

Use it **sparingly** and **clearly document** its usage when necessary.

---

## 📚 Summary

| 🧩 Feature | ✅ Good For | ❌ Risk |
|-----------|------------|---------|
| Dynamic modification | Quick fixes, mocking, async I/O | Debugging, stability |
| No source changes needed | Yes | Can break libraries |
| Common in async libs | Eventlet, Gevent | Must be applied early |

---

