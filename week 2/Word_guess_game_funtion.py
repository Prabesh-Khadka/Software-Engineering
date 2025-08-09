import random as rd

class GuessWordGame:
    def __init__(self):
        # Set up the game when an object is created
        self.secret_word = self.get_random_word()
        self.guessed_letters = []
        self.attempts = 5

    def get_random_word(self):
        """Return a random fruit from the list."""
        words = ["apple", "banana", "strawberry", "pineapple", "guava",
                 "watermelon", "lemon", "dragonfruit", "coconut", "kiwi"]
        return rd.choice(words)

    def display_word_state(self):
        """Show the word with guessed letters and underscores."""
        display = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.secret_word])
        print("\nWord:", display)

    def get_player_guess(self):
        """Ask player for a guess and return it in lowercase."""
        return input("Guess a letter: ").lower()

    def process_guess(self, guess):
        """Process player's guess and update attempts/letters."""
        if guess in self.guessed_letters:
            print("You already guessed that letter!!!")
            return
        elif guess in self.secret_word:
            self.guessed_letters.append(guess)
            print("Good guess!")
        else:
            self.attempts -= 1
            print(f"Wrong guess! Remaining attempts: {self.attempts}")

    def check_win_condition(self):
        """Return True if all letters are guessed."""
        return all(letter in self.guessed_letters for letter in self.secret_word)

    def play_game(self):
        """Main game loop."""
        print("Welcome to the Fruit Guessing Game!")
        print(f"The word has {len(self.secret_word)} letters.")

        while self.attempts > 0:
            self.display_word_state()
            guess = self.get_player_guess()
            self.process_guess(guess)

            if self.check_win_condition():
                print(f"\nYou guessed it! The word was '{self.secret_word}'.")
                break
        else:
            print(f"\nGame Over! The word was '{self.secret_word}'.")


# -----------------------
# Run the game
# -----------------------
game = GuessWordGame()  # create an object
game.play_game()        # start the game
