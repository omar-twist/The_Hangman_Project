from Hangman import run_game_session


class HangmanGame:
    def __init__(self):
        self.name = input('Enter your name: ').strip()
        self.final_score = 0.0
        self.total_score = 0.0
        self.games_played = 0

    def _calculate_score(self, correct_letters, total_letters, mistake_counter):
        percent_correct = (correct_letters / total_letters) * 100 if total_letters > 0 else 0
        percent_wrong = (mistake_counter / 10) * 100
        return (percent_correct+ (100-percent_wrong)) /2




        # if total_letters == 0 or mistake_counter >= 10:
        #     return 0.0

        # percent_correct = (correct_letters / total_letters) * 100
        # percent_wrong = (mistake_counter / 10) * 100
        # score = percent_correct - percent_wrong
        # return max(score, 0.0)

    def play(self):
        """Run game cycles until the player decides to stop."""
        print(f'Welcome {self.name}!')

        while True:
            result = run_game_session()
            mistake_counter = result['mistake_counter']
            correct_letters = result['correct_letters']
            total_letters = result['total_letters']

            score_of_single = self._calculate_score(correct_letters, total_letters, mistake_counter)
            self.games_played += 1
            self.total_score += score_of_single
            self.final_score = self.total_score / self.games_played

            print(f'\nScore for this game: {score_of_single:.1f}%')
            print(f'Current average score: {self.final_score:.1f}%')

            again = input('\nPlay again? (yes/no): ').strip().lower()
            if again == 'no':
                break
            else:
                print('I will consider that a yes.\n')

        print(f'\nThanks for playing, {self.name}! Final average score: {self.final_score:.1f}%')


if __name__ == '__main__':
    game = HangmanGame()
    game.play()
