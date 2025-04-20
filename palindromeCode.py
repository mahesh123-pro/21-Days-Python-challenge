def is_palidrome(word):
    
    word=word.lower()
    return word==word[::-1]

user_input=input("Enter a word/number: ")
if is_palidrome(user_input):
    print(f"{user_input} is a palindrome ")
else:
    print(f"{user_input} is not a palindrome ")
    