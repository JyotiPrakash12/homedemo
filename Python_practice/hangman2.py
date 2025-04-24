import random

word_list = ["cat", "dog", "sun", "run", "pen", "cup", "tree", "book", "fish", "bird",
             "apple", "banana", "orange", "purple", "window", "garden", "soccer", "pencil", "rabbit", "flower",
             "elephant", "computer", "mountain", "library", "bicycle", "sandwich", "holiday", "whisper", "journey", "mystery",
             "tiger", "dolphin", "monkey", "giraffe", "penguin", "squirrel", "butterfly", "crocodile", "kangaroo", "octopus",
             "pizza", "burger", "salad", "pasta", "cookie", "carrot", "cheese", "grapes", "tomato", "lemon",
             "India", "Canada", "Brazil", "France", "Japan", "Mexico", "Germany", "Australia", "Nigeria", "Egypt",
             "cloud", "music", "dream", "silence", "puzzle", "shadow", "planet", "secret", "wisdom", "laughter"]


secret_word = random.choice(word_list).lower()
print(secret_word)
stages = ["""
  --------
  |      |
  |      O
  |     \\|/
  |      |
  |     / \\
  -
""", """
  --------
  |      |
  |      O
  |     \\|/
  |      |
  |     /
  -
""", """
  --------
  |      |
  |      O
  |     \\|/
  |      |
  |
  -
""", """
  --------
  |      |
  |      O
  |     \\|
  |      |
  |
  -
""", """
  --------
  |      |
  |      O
  |      |
  |      |
  |
  -
""", """
  --------
  |      |
  |      O
  |
  |
  |
  -
""", """
  --------
  |      |
  |
  |
  |
  |
  -
"""]

placeholder= ""
word_length = len(secret_word)
for position in range(word_length):
    placeholder+="-"
print(placeholder)

correct_letter = []

game_over = False
lives = 6
while not game_over:
    user_guess = input("Guess the letter: ").lower()
    display = ""
    for letter in secret_word:
        if letter == user_guess:
            display+= letter
            correct_letter.append(user_guess)
        elif letter in correct_letter:
            display+= letter
        else:
            display += "_"
            
    print(display)

    if "_" not in display:
        game_over = True
        print("You win")

    if user_guess not in secret_word and lives >0:
        lives-=1
        print(f"you have {lives} left")
        if lives ==0:
            game_over = True
            print("You lose")
    print(stages[lives])


    
