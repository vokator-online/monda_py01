# Python programming principles

Python is a programming language, based on certain rules and principles.

## Code structure and Block structure

Python code structure is very important, because code blocks are structured by identation - specific spacing from the start of the line. Python does not use semicolons or curly brackets for this, like other languages. Python uses indentation (typically 4 spaces) to define blocks of code.

Correct code structure example

```Python
if x > 0:
    print("x is a positive number")
else:
    print("x is a negative number or equals 0")
```

Incorrect code structure example:

```Python
if x > 0:
print("x is a positive number")
else:
   print("x is a negative number or equals 0")
```

## Code Sentence Structure

Python sentence structure is simple, because every sentence starts from a new line and semicolon (;) is not required to end the sentence.

Simple example of the sentence:

```Python
print("Hello World!")
```

## PEP8 convention

PEP8 is a python code writing ruleset, helping to standardize code formatting. These rules are applied to help coders working in teams to better understand each other's code, and maintain uniformal culture. Some of those rules: 

```Text
❗ Do NOT use tabs for identation, use spaces only. And always same amount of spacing for each block - 4 spaces. VS Code will handle this for you.

❗ Each line of code should not exceed 79 characters in length.

❗ When using several comma separated arguments, leave a space after each comma, not before.

❗ Name variables so that their names can explain what is in them. Variable names should represent their content.

❗ Class names should use CapWords notation, for example, MyClass.

❗ Names of functions, class methods and variables should be consisting only of lowercase letters and numbers, separated by underscores. For example, get_number_list, student_last_name. 

❗ Do not use abbreviations where possible, for example, bd instead of birth_date.

❗ Use clearly understandable forms of operators. For example, != instead of <>.

❗ Use identical identation for separators. For example, if function arguments are not fitting in one line, list them idented evenly from the left on each line, and leave the closing bracket of the function declaration unindented at the new line, at the same level with the function's def statement.
```
More about PEP8 you can read in the [official Python PEP8 documentation page](https://www.python.org/dev/peps/pep-0008/).

💡 These rules are not mandatory to uphold, but by implementing them in practice will improve readability and understandability of your code, especially when working in teams or participating in open source projects.

## Comments

The code is written not only for computers, but also for humans maintaining it. Comments are the feature, allowing developers to leave notes or important contextual information, explaining the meaning of certain code blocks. They may help with contextual understanding while maintaining your own code, especially when it grows with time. 

Comments begin with a hashtag (`#`) and extend to the end of the physical line.. Code interpreter completely ignores comments, they are non-functional. Comments are useful also to temporarily disable existing code, which you do not want to run, without deleting such code.

Examples of comments:

```Python
# This code reads two numbers from the user
number_1 = int(input("Enter 1st number: "))
number_2 = int(input("Enter 2nd number: "))

# This line sums the numbers
result = number_1 + number_2

# This line outputs the result
print("The sum of your inputs is ", result)
```

```Python
# This is how we define variables and set their values
number_1 = 5
number_2 = 10

# This line sums the numbers
result = number_1 + number_2

# This line outputs the result
print("The sum of two numbers is ", result)
```

```Python
# This function checks if the argument number is even
def is_even(number: int):
    return number % 2 == 0

# Here we call the above function with user's input as an argument, and output the result in a human readable format
if is_even(int(input("Enter a number: "))):
    print("Even")
else:
    print("Odd")
```

### Multi-line comments

multi-line comments are denoted by triple single (`'''`) or double (`"""`) quotes. These are also used for docstrings in function definitions, which we will discuss later.

Example:

```Python
"""
All this text and comment will be ignored by Python interpreter.
Not only one line, but everything...
print("this will not print either")
"""
print("but this will print")
# see the difference?
```

## Keyboard Shortcuts in VS Code

Keyboard shortcuts can be used to improve work efficiency with code editors like VS Code, because they allow to write code easier. VS Code is very powerful code creation environment with many extensions, and keyboard shortcuts can be used in all operating systems, including Linux, Mac and Windows.

Some of the most useful shortcuts:

```Text
👉 `Ctrl + Shift + P` (`Cmd + Shift + P` for macOS) - Open VS Code command prompt

👉 `Ctrl + P` (`Cmd + P` for macOS) - Open Fast Menu

👉 `Ctrl + Shift + E` (`Cmd + Shift + E` for macOS) - Open File Browser or cycle between code and file browser.

👉 `Ctrl + Shift + F` (`Cmd + Shift + F` for macOS) - Search panel

👉 `Ctrl + Shift + K` (`Cmd + Shift + K` for macOS) - Delete current line of code / text

👉 `Ctrl + /` (`Cmd + /` for macOS) - Add/remove comment on the cursor's line or for the selection
```

💡 These are only a few examples of many available shortcuts VS Code has. You can find more shortcuts in VS Code documentation, available directly in VS Code or at their [documentation web page](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference). Once there, choose the reference sheet for your operating system (Windows/Mac/Linux)

### inside VS Code

From menu Help -> Keyboard Shortcuts Reference or just use these shorcuts `Ctrl + K`, `Ctrl + R` in quick succession. (`Cmd + K`, `Cmd + R` for macOS)
