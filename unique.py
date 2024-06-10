def count_unique_substrings(s: str) -> int:
    unique_substrings = set()
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if substring != s: 
                unique_substrings.add(substring)
    
    return len(unique_substrings)

s = "ababa"
print(count_unique_substrings(s))  
