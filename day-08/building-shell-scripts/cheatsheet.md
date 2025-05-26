# 🐚 Shell Scripting Cheatsheet

A handy reference for writing and understanding common shell scripting constructs.

---

## 🔧 Script Basics

```sh
#!/bin/bash      # Always start with the shebang
📌 Variables

name="John"
echo "Hello, $name"
Read from input:
sh
Copy
Edit
read -p "Enter your name: " name
📂 File and Directory Operations

mkdir new_folder        # Create directory
cd new_folder           # Change directory
touch file.txt          # Create file
rm file.txt             # Delete file
ls -l                   # List files with details
pwd                     # Print current working directory
🔁 Loops
For Loop

for i in 1 2 3 4 5
do
  echo "Number: $i"
done
While Loop

count=1
while [ $count -le 5 ]
do
  echo "Count: $count"
  ((count++))
done
Until Loop

count=1
until [ $count -gt 5 ]
do
  echo "Count: $count"
  ((count++))
done
❓ Conditionals

if [ $age -ge 18 ]; then
  echo "Adult"
elif [ $age -gt 12 ]; then
  echo "Teen"
else
  echo "Child"
fi
Test expressions:

[ -f filename ]     # True if file exists
[ -d dirname ]      # True if directory exists
[ -z "$var" ]       # True if variable is empty
[ "$a" == "$b" ]    # String comparison
[ $a -eq $b ]       # Numeric comparison
🔢 Arithmetic Operations

a=5
b=3
sum=$((a + b))
echo "Sum: $sum"
🧵 Functions

greet() {
  echo "Hello, $1!"
}
greet "Alice"
📁 Command Substitution

current_dir=$(pwd)
echo "You are in $current_dir"
📦 Script Arguments

echo "Script name: $0"
echo "First argument: $1"
echo "All arguments: $@"
🛑 Exit Codes

exit 0       # Exit with success
exit 1       # Exit with failure
Checking exit status

if [ $? -eq 0 ]; then
  echo "Success"
else
  echo "Failure"
fi
🧪 Case Statement

read -p "Enter choice: " choice
case $choice in
  y|Y) echo "Yes";;
  n|N) echo "No";;
  *)   echo "Invalid choice";;
esac
⚠️ Error Handling & Debugging

set -e          # Exit on any error
set -x          # Print commands as they execute (debug mode)
🧹 Tips
Use "${var}" to safely handle spaces in variables.

Quote your paths and inputs to avoid errors.

Use functions to organize large scripts.

📚 Resources
man bash — Bash manual

https://tldp.org/LDP/abs/html/ — Advanced Bash Scripting Guide