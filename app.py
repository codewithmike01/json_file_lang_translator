from deep_translator import GoogleTranslator
from pprint import pprint
from lib.translator import LanguageTranslator


def main():
    print('List of Supported Languages')

    pprint(GoogleTranslator().get_supported_languages(as_dict=True))

    try:
      source_lang: str = str(input('Enter abbreviation of source Language: '))
      target_lang: str = str(input('Enter abbreviation of target Language: '))

    except ValueError:
       print("""
        Source and Target Value Must be String
       """)

    except KeyboardInterrupt:
       return exit()

    json_tranlation = LanguageTranslator()
    json_tranlation.translate_json(source_lang, target_lang)


main() # Main calling point


