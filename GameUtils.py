import os
from typing import List, Union


class GameUtils:
    """"""

    __cyrillic_lower_letters = (
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    )


    @staticmethod
    def clear_console():
        os.system("cls" if os.name == "nt" else "clear")


    @staticmethod
    def get_safe_input(prompt):
        try:
            return input(prompt)
        except KeyboardInterrupt:
            print("\nПрограмма завершена пользователем!\n")
            exit(0)
        except:
            return "%"


    @staticmethod
    def get_checked_input(
        prompt: str, allowed_answers: Union[str, List[str]], err_message: str
    ) -> str:
        res = GameUtils.get_safe_input(prompt)

        while res not in allowed_answers:
            # GameUtils.clear_console()
            print(err_message)
            res = GameUtils.get_safe_input(prompt)
        return res


    @staticmethod
    def is_user_want_play() -> bool:
        err_message = "\t[Введите 'да' или 'нет']"
        res = GameUtils.get_checked_input(
            "Вы готовы сыграть? да/нет: ", ["да", "нет"], err_message
        )

        return res == "да"


    @staticmethod
    def get_user_answer():
        err_message = "\t[Введите один символ кириллицы а-я]"
        return GameUtils.get_checked_input(
            "Ваша буква: ", GameUtils.__cyrillic_lower_letters, err_message
        )
