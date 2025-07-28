import random

words = ['python', 'hangman', 'keyboard', 'banana', 'pikachu', 'gaming', 'explore']

stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

word = random.choice(words)
word_letters = set(word)
guessed_letters = set()
lives = len(stages) - 1

print("🎮 Welcome to Hangman! Let's play!\n")

while len(word_letters) > 0 and lives > 0:
    print(stages[len(stages) - 1 - lives])
    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
    print(f"Lives left: {lives}")
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: " + ' '.join(display_word))
    
    guess = input("🔤 Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single letter from A-Z.\n")
        continue
    
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. Try another.\n")
        continue
    
    guessed_letters.add(guess)
    if guess in word_letters:
        word_letters.remove(guess)
        print("✅ Correct!\n")
    else:
        lives -= 1
        print("❌ Wrong!\n")

if lives == 0:
    print(stages[-1])
    print(f"💀 You lost! The word was: {word}")
else:
    print(f"🎉 You won! The word was: {word}")
print("Thanks for playing Hangman! 🎮")