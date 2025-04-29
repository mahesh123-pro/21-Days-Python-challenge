def cout_vowels_consonants(text):
    vowels='aeiouAEIOU'
    consonant_count=0
    vowel_count=0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    return vowel_count, consonant_count
#------------Main program------------------
user_input=input("Enter a word or sentence: ")
vowel_count, consonant_count=cout_vowels_consonants(user_input)
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
#------------------End of program----------------