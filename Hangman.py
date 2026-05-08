#steps:
#finding a randomized word
#displaying word length
#loops for guessing letters and displaying the guessed letter
#a mistake counter
#error control if non literal ch is entered

# class Game :
#     score = 0

#     def changeScore(newSc, self):
#         self.score = newSc

import random
def load_words(path='words.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    words = []
    for line in lines:
        parts = line.split('-', 1)
        if len(parts) == 2:
            words.append((parts[0].strip().lower(), parts[1].strip()))
    return words

def choose_random_word(words):
    if not words:
        raise ValueError('No words available to choose from.')
    return random.choice(words)

def get_guess_input(hidden_word, wrongs):
    print(' '.join(hidden_word))
    print(f'Wrong letters guessed: {wrongs}')
    return input('Guess one letter: ').strip()

def run_game_session():
    """Run a single game session and return game metrics."""
    words = load_words()
    word, definition = choose_random_word(words)
    hidden_word = ['_'] * len(word)
    wrongs = ''
    mistake_counter = 0

    print(f'The word has {len(word)} letters.')
    while mistake_counter <= 10:
        if mistake_counter == 10:
            print('10/10 attempts used.\nFailed this game, word has not been guessed correctly.')
            print(f'The word is: {word}, meaning: {definition}')
            break
        if '_' not in hidden_word:
            print('Congratulations, you have guessed the word correctly!')
            print(f'The word is: {word}, meaning: {definition}')
            break
        guess = get_guess_input(hidden_word, wrongs)
        if len(guess) != 1 or not guess.isalpha():
            print('Nope, try again.')
            continue
        if guess not in word:
            mistake_counter += 1
            if guess not in wrongs:
                wrongs += f'{guess} '
            print(f'Letter is not in the word\n{mistake_counter}/10 attempts used.')
        else:
            for index, ch in enumerate(word):
                if guess == ch:
                    hidden_word[index] = guess

    correct_letters = len([ch for ch in hidden_word if ch != '_'])
    total_letters = len(hidden_word)
    return {
        'mistake_counter': mistake_counter,
        'correct_letters': correct_letters,
        'total_letters': total_letters,
    }

