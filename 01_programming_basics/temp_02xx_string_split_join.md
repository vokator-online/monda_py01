### 5. `split()` and `join()`

`split()` divides a string into a list of substrings based on a delimiter, and `join()` joins a list of strings into one string.

```python
words = "apple,banana,orange"
fruit_list = words.split(",")
print(fruit_list)  # ['apple', 'banana', 'orange']

joined_words = "-".join(fruit_list)
print(joined_words)  # apple-banana-orange
```

**Quick Assignment**: Split the string "Python|Java|C++" using the "|" delimiter, and then join the resulting list with a comma.
