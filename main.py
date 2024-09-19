from bs4 import BeautifulSoup
import requests
from googletrans import Translator


def get_words():
    url = "https://randomword.com/"
    try:
        # Получение слова с сайта:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        words = soup.find("div", id="random_word").text.strip()
        definition = soup.find("div", id="random_word_definition").text.strip()

        # Перевод слова с английского на русский язык:
        translator = Translator()
        ru_words = translator.translate(words, dest="ru").text
        ru_definition = translator.translate(definition, dest="ru").text

        return {
            "en_word": words,  # Оригинальное слово
            "en_definition": definition, # Оригинальное определение
            "ru_word": ru_words, # Перевод оригинального слова на русский
            "ru_definition": ru_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_words()
        if not word_dict:
            print("Не удалось получить слово. Попробуйте позже.")
            break

        word = word_dict.get("en_word")
        definition = word_dict.get("en_definition")
        ru_word = word_dict.get("ru_word")
        ru_definition = word_dict.get("ru_definition")

        print(f"Значение слова: {ru_definition} ({definition})")
        answer = input("Что это за слово? ")

        if answer.lower().strip() == ru_word.lower().strip() or answer.lower().strip() == word.lower().strip():
            print("Вы верно ответили! Поздравляем!")
        else:
            print(f"Вы не угадали слово. Было загадано слово: {ru_word} ({word})")

        play_again = input("Хотите сыграть ещё? y/n ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()







