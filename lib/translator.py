from deep_translator import GoogleTranslator

import json

class LanguageTranslator:

  def __init__(self, source_lang, target_lang) -> None:
      self.source_lang = source_lang
      self.target_lang = target_lang


  def translate_string(self, string_value: str):
      return GoogleTranslator(source = self.source_lang, target = self.target_lang).translate(string_value)



  def open_json_file(self):

     output = {}

     with open('./data/en.json', 'r') as data:
         json_data = list(json.load(data))

         for string_value in json_data:
             trans_value = self.translate_string(string_value)
             print(f'--- {string_value} : {trans_value} ---') # Act as processing indication
             output[string_value] = trans_value

     return output


  def save_output_json_file(self , output):
     with open(f'./data/{self.target_lang}.json', 'w', newline='') as output_data:
          output_data.write(json.dumps(output))

  def translate_json(self, source_lang: str, target_lang: str):
      """
      translate_json performs translations from a json file
      and saves the output into a json file

      Attribute: source_lang: str,
        target_lang: str
      """

      output = self.open_json_file(source_lang, target_lang)
      self.save_output_json_file(target_lang, output)






