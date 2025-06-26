# Longest Substring Without Repeating Characters
# Input: "abcabcbb"

# Output: 3 ("abc")

def get_substring(strg):
    sub_str = ""
    largest_str = ""
    for char in strg:
        if char not in sub_str:
            sub_str = sub_str + char
            if len(sub_str) > len(largest_str):
                largest_str = sub_str
        elif char in sub_str:
            if len(sub_str) > len(largest_str):
                largest_str = sub_str
            sub_str = char

    return f"{len(largest_str),largest_str}"

print(get_substring("bbbbb"))