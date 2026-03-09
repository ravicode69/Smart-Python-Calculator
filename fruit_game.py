import random

# Fruit list
fruits = [
    "apple","banana","mango","strawberry","orange","grape",
    "pineapple","apricot","lemon","coconut","watermelon",
    "cherry","papaya","berry","peach","lychee","muskmelon"
]

def play_game():
    secret_word = random.choice(fruits)
    guessed_letters = []
    display = ["_"] * len(secret_word)

    lives = 6
    score = 0

    print("\n🎮 Fruit Guessing Game")
    print("Hint: It is a fruit name\n")
    print(" ".join(display))

    while lives > 0:

        guess = input("\nEnter a letter: ").lower()

        # Validation
        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Enter only ONE alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct guess!")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess
                    score += 1
        else:
            print("❌ Wrong guess!")
            lives -= 1

        print("Word:", " ".join(display))
        print("❤️ Lives left:", lives)
        print("⭐ Score:", score)

        if "_" not in display:
            print("\n🏆 Congratulations! You guessed the fruit:", secret_word)
            return

    print("\n😢 Game Over! The fruit was:", secret_word)


# Main game loop
while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("👋 Thanks for playing!")
        break     
