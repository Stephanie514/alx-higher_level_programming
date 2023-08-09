#!/usr/bin/python3

filtered_chars = [
    chr(char_code) for char_code in range(97, 123)
    if chr(char_code) not in ['q', 'e']
]
result_str = "".join(filtered_chars)

print(result_str, end="")
