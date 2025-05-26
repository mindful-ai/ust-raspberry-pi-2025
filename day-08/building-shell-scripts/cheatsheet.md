🗂️ 1. File Test Operators
Operator	Description
-e	File exists (any type)
-f	File exists and is a regular file
-d	File exists and is a directory
-s	File exists and is not empty
-r	File is readable
-w	File is writable
-x	File is executable
-L	File is a symbolic link
-b	File is a block device
-c	File is a character device

🧮 2. Numeric Comparison Operators
Use -eq, -ne, -gt, etc., for comparing integers.

Operator	Meaning	Example
-eq	Equal to	[ "$a" -eq "$b" ]
-ne	Not equal to	[ "$a" -ne "$b" ]
-gt	Greater than	[ "$a" -gt "$b" ]
-lt	Less than	[ "$a" -lt "$b" ]
-ge	Greater than or equal	[ "$a" -ge "$b" ]
-le	Less than or equal	[ "$a" -le "$b" ]

📝 3. String Comparison Operators
Operator	Description
=	Strings are equal
!=	Strings are not equal
<	String1 is less than String2 (ASCII)
>	String1 is greater than String2
-z	String is null (zero length)
-n	String is not null

🔔 Note: When using < or > for strings, enclose the condition in double brackets ([[ ... ]]) to avoid shell interpretation issues.

🔗 4. Logical Operators (inside [[ ... ]])
Operator	Meaning	Example
&&	Logical AND	[[ $a -gt 5 && $a -lt 10 ]]
`		`
!	Logical NOT	[[ ! -e myfile.txt ]]

