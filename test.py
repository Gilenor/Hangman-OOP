from Game import Game
from WordDictionary import WordDictionary


if __name__ == "__main__":
    words = WordDictionary("words.json")

    if not words:
        print("File empty or non exist!")
        exit(1)

    game = Game(words)
    game.run()
