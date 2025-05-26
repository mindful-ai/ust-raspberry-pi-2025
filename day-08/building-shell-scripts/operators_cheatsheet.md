
# 🧮 Shell Scripting Operators and Expressions Cheatsheet

A quick reference for essential operators used in shell scripts.

---

## 📁 File and Directory Test Operators

| Expression         | Meaning                               |
|--------------------|----------------------------------------|
| `-e file`          | True if file exists                    |
| `-f file`          | True if file exists and is a regular file |
| `-d directory`     | True if directory exists               |
| `-r file`          | True if file is readable               |
| `-w file`          | True if file is writable               |
| `-x file`          | True if file is executable             |
| `-s file`          | True if file is not empty              |
| `! expression`     | Negates the expression                 |

---

## 🔢 Numeric Comparison Operators

| Operator   | Description                    |
|------------|--------------------------------|
| `-eq`      | Equal                          |
| `-ne`      | Not equal                      |
| `-gt`      | Greater than                   |
| `-lt`      | Less than                      |
| `-ge`      | Greater than or equal to       |
| `-le`      | Less than or equal to          |

**Example:**

```bash
if [ "$a" -gt "$b" ]; then
  echo "$a is greater than $b"
fi
```

---

## 🔤 String Comparison Operators

| Operator         | Description                         |
|------------------|-------------------------------------|
| `=` or `==`      | Strings are equal                   |
| `!=`             | Strings are not equal               |
| `<`              | String1 is less than String2        |
| `>`              | String1 is greater than String2     |
| `-z string`      | True if string is empty             |
| `-n string`      | True if string is not empty         |

**Note:** Use `[[ ... ]]` for `<` and `>` to avoid syntax errors.

---

## 🔗 Logical Operators

| Operator   | Description                        |
|------------|------------------------------------|
| `-a`       | AND (deprecated in `[[`])          |
| `-o`       | OR (deprecated in `[[`])           |
| `!`        | NOT                                |
| `&&`       | AND (in command chaining)          |
| `||`       | OR (in command chaining)           |

**Examples:**

```bash
if [[ $a -gt 5 && $b -lt 10 ]]; then
  echo "a > 5 AND b < 10"
fi

if [ -z "$str" ] || [ "$str" == "default" ]; then
  echo "Empty or default string"
fi
```

---

## 🧠 Other Useful Expressions

### Command Substitution

```bash
now=$(date)
echo "Current time: $now"
```

### Arithmetic Evaluation

```bash
(( sum = a + b ))
```

### String Manipulation

```bash
len=${#str}                   # Length of string
substr=${str:0:4}             # Substring from index 0, length 4
newstr=${str/old/new}         # Replace 'old' with 'new'
```

### Arrays

```bash
arr=(one two three)
echo "${arr[0]}"              # Access element
echo "${arr[@]}"              # All elements
echo "${#arr[@]}"             # Length
```

---

## ✅ Best Practices

- Always quote variables: `"$var"`
- Prefer `[[ ... ]]` for test expressions.
- Use functions for better structure.
- Validate inputs and handle errors gracefully.

---

## 📚 References

- `man test`
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/)

---
