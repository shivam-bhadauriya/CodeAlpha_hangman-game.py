import random
words = ["apple", "train", "chair", "table", "plant"]

word_to_guess = random.choice(words)

guessed_letters = []            
incorrect_guesses = 0          
max_incorrect_guesses = 6     
display_word = ["_"] * len(word_to_guess) 

print("🎮 Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 chances to make wrong guesses.\n")

while incorrect_guesses < max_incorrect_guesses and "_" in display_word:
    print("Word:", " ".join(display_word)) 
    print("Guessed letters so far:", guessed_letters)
    
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter only one alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. Try something else.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct guess!\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} tries left.\n")

if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Game Over! The correct word was:", word_to_guess)
