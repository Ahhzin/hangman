import random

def guess_word():
    words = ["itlay", "spain","japan","brazil","peru","korean"]
    secret_word = random.choice(words)
    guessed_lettetrs = []
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the secret word.")
    
    while attempts < max_attempts:
        print("\nSecret word:", end=" ")
        for letter in secret_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        
        guess = input("\nEnter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts += 1
        
        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You've guessed the word:", secret_word)
            break
    
    if attempts >= max_attempts:
        print("Sorry, you've run out of attempts. The secret word was:", secret_word)

guess_word()
