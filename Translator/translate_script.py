from translate import Translator

translator = Translator(to_lang="ko")

try:
    with open('./text.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        # Write the translation to a new file
        with open('./translated-ko.txt', mode='w', encoding='utf-8') as my_translated_file:
            my_translated_file.write(translation)
except FileNotFoundError as err:
    print('Check file path')
