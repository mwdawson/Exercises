# Instructions
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

longest = s[0]

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        sort = True
        for k in range(len(sub) - 1):
            if(sub[k] > sub[k+1]):
                sort = False
        if sort and len(sub) > len(longest):
            longest = sub

print('Longest substring in alphabetical order is: ' + longest)