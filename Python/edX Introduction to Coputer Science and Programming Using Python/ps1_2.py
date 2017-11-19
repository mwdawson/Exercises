# Instructions:
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.

n_bob = 0
for i in range(len(s) - 2):
    sub = s[i:i+3]
    if sub == 'bob':
        n_bob += 1

print('Number of times bob occurs is: ' + str(n_bob))