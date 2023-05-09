from deep_translator import GoogleTranslator

import json

class LanguageTranslator:
  """
  Language Translation class a blue
  print for the tranlation object

  Attributes: source_lang: str, target_lang: str
  """

  def __init__(self, source_lang: str, target_lang: str) -> None:
      self.source_lang = source_lang
      self.target_lang = target_lang

  def translate_string(self, string_value: str):
      """
      translation string performs the tranlation of a string

      Attributes: string_value: str
      """
      return GoogleTranslator(source = self.source_lang, target = self.target_lang).translate(string_value)

  def open_json_file(self, file_path: str):
     """
      open json file accesses the source file
      and translate the string by string

      Attributes: file_path: str
      """
     output = {}

     with open(file_path, 'r') as data:
         json_data = list(json.load(data))

         for string_value in json_data:
             trans_value = self.translate_string(string_value)
             print(f'--- {string_value} : {trans_value} ---') # Act as processing indication
             output[string_value] = trans_value

     return output

  def save_output_json_file(self , output: dict, file_path: str):
     """
      save output json file writes translated dict
      into a json file

      Attributes:output: dist,  file_path: str
      """
     with open(f'{file_path}{self.target_lang}.json', 'w', newline='') as output_data:
          output_data.write(json.dumps(output))

     print(f'File successfully saved in {file_path}{self.target_lang}.json')

     return {"message": "Saved Successfully!!"}

  def translate_json(self):
      """
      translate_json performs translations from a json file
      and saves the output into a json file
      """
      output = self.open_json_file('./data/source.json')
      self.save_output_json_file(output, './data/')







