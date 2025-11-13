word = input("Enter a word:")
letter = input("Enter a letter to search for:")

if letter in word:
    print(f"The letter '{letter}' is found in the word '{word}'")
else:
    print(f"The letter '{letter}' is NOT found in the word '{word}'")