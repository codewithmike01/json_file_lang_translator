from deep_translator import GoogleTranslator
from pprint import pprint
from lib.translator import LanguageTranslator
import logging

SUPPORTED_LANG = GoogleTranslator().get_supported_languages(as_dict=True)

def main():
    check_valid = False
    print('List of Supported Languages')

    pprint(SUPPORTED_LANG)

    while not check_valid:
      try:
        check_valid = True
        source_lang: str = str(input('Enter abbreviation of source Language: '))
        target_lang: str = str(input('Enter abbreviation of target Language: '))

        json_tranlation = LanguageTranslator(source_lang, target_lang)
        json_tranlation.translate_json()

      except KeyboardInterrupt:
        return exit()

      except Exception:
         check_valid = False # Not valid to pass

         print("""
          **********************************************************
          Value you entered does not exist in supported languages

          Please re-enter correct supported language
          **********************************************************

          """)










main() # Main calling point


