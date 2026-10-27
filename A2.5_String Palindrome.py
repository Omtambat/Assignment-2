# A2.5 - String Palindrome

text = input("Enter a string: ")

reverse_text = ""

for character in text:
    reverse_text = character + reverse_text

if text == reverse_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")