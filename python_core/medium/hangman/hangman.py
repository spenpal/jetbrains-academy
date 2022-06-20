import random

# CLASS #
class Hangman:
    
    def __init__(self, words, attempts):
        self.words = words
        self.MAX_ATTEMPTS = attempts
        self.ans = random.choice(words)
        
        self.guesses = set()
        self.wins = self.losses = 0
    
    
    def reset(self):
        self.ans = random.choice(self.words)
        self.guesses = set()
            
            
    def valid_input(self, guess):
        if len(guess) != 1:
            print('Please, input a single letter.', end='\n\n')
            return False
        elif not guess.islower():
            print('Please, enter a lowercase letter from the English alphabet.', end='\n\n')
            return False
            
        return True
    
    
    def start(self):
        print(f'H A N G M A N  # {self.MAX_ATTEMPTS} attempts')
        
        while True:
            option = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
            if option == 'exit': break
            elif option == 'results':
                print(f'You won: {self.wins} times.')
                print(f'You lost: {self.losses} times.')
                continue
            
            print()
            
            # Play the game
            self.reset()
            attempts = self.MAX_ATTEMPTS
            revealed = ''.join(let if let in self.guesses else '-' for let in self.ans)
            
            while attempts and revealed != self.ans:
                print(revealed)
                
                guess = input(f'Input a letter: ')
                while not self.valid_input(guess):
                    print(revealed)
                    guess = input(f'Input a letter: ')
                
                if guess in self.guesses:
                    print("You've already guessed this letter.", end='\n\n')
                    continue
                elif guess not in self.ans:
                    print("That letter doesn't appear in the word.", end='')
                    attempts -= 1
                    print(f'  # {attempts} attempts', end='\n\n')
                else:
                    print()
                    
                self.guesses.add(guess)
                revealed = ''.join(let if let in self.guesses else '-' for let in self.ans)
                
            if revealed == self.ans:
                print(f'You guessed the word {self.ans}!')
                print('You survived!')
                self.wins += 1
            else:
                print('You lost!')
                self.losses += 1
            
            
        
# MAIN #
config = {
    'words': ['python', 'java', 'swift', 'javascript'],
    'attempts': 8
}
game = Hangman(**config)
game.start()