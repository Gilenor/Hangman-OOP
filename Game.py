from Board import Board
from GameUtils import GameUtils as gu
from WordDictionary import WordDictionary


class Game:
    """"""

    def __init__(self, words: WordDictionary):
        self.__words = words
        self.__board = None


    def run(self):
        while gu.is_user_want_play():
            category, word = self.__words.get_random_word()
            self.__board = Board(word, category)
            self.__new_game()
            self.__print_game_result()


    def __new_game(self):
        while not self.__is_game_over():
            print(self.__board)
            letter = gu.get_user_answer()

            # ToDo: может сделать паузу перед очисткой экрана
            # if self.__board.is_letter_was_opened(letter):
            # 	print("Вы уже вводили эту букву")
            # elif not self.__board.open_letter(letter):
            # 	print("Такой буквы нет в слове")

            self.__board.open_letter(letter)
            gu.clear_console()


    def __print_game_result(self):
        if self.__board.is_word_guessed():
            print("Поздравляем, вы угадали слово!\n")
        else:
            print(self.__board.get_game_over_board())
            print(f"Было загадано слово: {self.__board.get_word()}\n")


    def __is_game_over(self):
        return self.__board.is_word_guessed() or not self.__board.is_user_has_attempts()
