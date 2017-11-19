# Instructions:
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s

vowel_count = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowel_count += 1
        
print('Number of vowels: ' + str(vowel_count))
