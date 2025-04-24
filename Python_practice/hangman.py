import random
def hangman():
 

    word_list = ["cat", "dog", "sun", "run", "pen", "cup", "tree", "book", "fish", "bird",
             "apple", "banana", "orange", "purple", "window", "garden", "soccer", "pencil", "rabbit", "flower",
             "elephant", "computer", "mountain", "library", "bicycle", "sandwich", "holiday", "whisper", "journey", "mystery",
             "tiger", "dolphin", "monkey", "giraffe", "penguin", "squirrel", "butterfly", "crocodile", "kangaroo", "octopus",
             "pizza", "burger", "salad", "pasta", "cookie", "carrot", "cheese", "grapes", "tomato", "lemon",
             "India", "Canada", "Brazil", "France", "Japan", "Mexico", "Germany", "Australia", "Nigeria", "Egypt",
             "cloud", "music", "dream", "silence", "puzzle", "shadow", "planet", "secret", "wisdom", "laughter"]
    
    secret_word  = random.choice(word_list).lower()
    print(secret_word)
    word_length = len(secret_word)
    guessed_letters = set()
    lives = 7
    display = ["_"]* word_length
    print("Welcome to Hangman!")
    print(f"The secret word has {word_length} letters.")
    print("You have", lives, "lives.")
    print("Current word:", " ".join(display))
   
    
    while  lives > 0 and "_" in display :
        user_guess = input("guess the letter: ").lower()
        if not user_guess.isalpha() or len(user_guess) != 1:
            print("Invalid guess. Please enter a single letter.")
            continue

        if user_guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(user_guess)

        if user_guess in secret_word:
            print("Correct guess")
            for i in range(word_length):
                if secret_word[i] ==user_guess:
                    display[i] = user_guess
        else:
            lives-=1
            print(f"Incorrect guess. You have {lives} lives left.")

            print("Current word:", " ".join(display))
                
        if lives > 0:
            print("Gusessed letter",",".join(sorted(list(guessed_letters))))

    if "_" not in display:
        print("Congratulations! You guessed the word:", secret_word)
    else:
        print("You ran out of lives! The word was:", secret_word)
hangman()


            
            






