import json
import random
from typing import Tuple


class WordDictionary:
    """"""

    def __init__(self, file_path: str):
        self.__words = self.__download_words(file_path)


    def __iter__(self):
        return (
            (category, word)
            for category in self.__words.keys()
            for word in self.__words[category]
        )


    def __len__(self) -> int:
        return sum(
            map(lambda category: len(self.__words[category]), self.__words.keys())
        )


    def get_random_word(self) -> Tuple[str]:
        category = random.choice(list(self.__words.keys()))
        word = random.choice(self.__words[category])

        return (category, word)


    def remove_word(self, category: str, word: str):
        if category in self.__words and word in self.__words[category]:
            word_idx = self.__words[category].index(word)
            del self.__words[category][word_idx]

            if len(self.__words[category]) == 0:
                del self.__words[category]


    # ==================== private methods ====================================


    def __download_words(self, file_path: str):
        try:
            with open(file_path, "rt", encoding="utf-8") as file:
                words = file.read()
                return json.loads(words)
        except:
            return {}
