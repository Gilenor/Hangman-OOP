import hang


class Board:
    """"""

    __MAX_ATTEMPTS = 7

    def __init__(self, word: str, category: str = "Отсутствует"):
        self.__attempts = 0
        self.__wrong_letters = []

        self.__word = word.strip().upper()
        self.__category = category.strip().upper()

        self.__user_data = ["*"] * len(self.__word)
        self.__field = self.make_empty_field(self.__word)


    def __str__(self):
        field = self.__get_user_data_field()
        # Добавить проверку на выход за пределы списка?
        hang_field = hang.states[self.__attempts]
        category = f"Категория: {self.__category}"
        errors = f"Ошибки ({self.__attempts}): {self.__wrong_letters}"

        return f"{hang_field}\n{field}\n{category}\n{errors}\n"


    def open_letter(self, letter: str) -> bool:
        # добавить проверку на ошибку?
        letter = letter.strip().upper()
        idx = self.__word.find(letter)

        if idx == -1 and not self.__is_letter_in_wrongs(letter):
            self.__attempts += 1
            self.__wrong_letters.append(letter)
            return False

        while idx != -1:
            self.__user_data[idx] = letter
            idx = self.__word.find(letter, idx + 1)

        return True


    def get_word(self) -> str:
        return self.__word


    def get_game_over_board(self) -> str:
        return hang.states[-1]


    def is_word_guessed(self) -> bool:
        return self.__user_data.count("*") == 0


    def is_user_has_attempts(self) -> bool:
        return self.__attempts < self.__MAX_ATTEMPTS - 1


    def is_letter_was_opened(self, letter: str) -> bool:
        return self.__is_letter_in_wrongs(letter) or self.__is_letter_in_opens(letter)


    # ==================== private methods ====================================


    def __get_user_data_field(self):
        return self.__field.format(*self.__user_data)


    def __is_letter_in_opens(self, letter: str) -> bool:
        return letter in self.__user_data


    def __is_letter_in_wrongs(self, letter: str) -> bool:
        return letter in self.__wrong_letters


    # ==================== static methods =====================================


    @staticmethod
    def make_empty_field(word: str):
        top = ("┌", "─", "┐", "┬")
        mid = ("│", "{}", "│")
        bot = ("└", "─", "┘", "┴")

        chars = len(word)
        top_field = f"{top[0]}{(top[1]+top[3]) * (chars-1)}{top[1]}{top[2]}\n"
        mid_field = f"{(mid[0]+mid[1]) * (chars)}{mid[2]}\n"
        bot_field = f"{bot[0]}{(bot[1]+bot[3]) * (chars-1)}{bot[1]}{bot[2]}"

        return top_field + mid_field + bot_field
