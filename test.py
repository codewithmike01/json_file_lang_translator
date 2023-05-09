import unittest
from lib.translator import LanguageTranslator


class TestLanguageTranslator(unittest.TestCase):

    def setUp(self) -> None:
        self.translator = LanguageTranslator('en', 'es')
        self.expected_output = {"April": "Abril","May": "Puede"}

    def test_translate_string(self):
        string_value = "Hello world"
        result = self.translator.translate_string(string_value)

        self.assertEqual(result, 'Hola Mundo')

    def test_open_json_file(self):
        file_path = './mock/source.json'
        result = self.translator.open_json_file(file_path)
        self.assertEqual(result, self.expected_output)

    def test_save_output_json_file(self):
        result = self.translator.save_output_json_file(self.expected_output, './mock/')
        self.assertEqual(result['message'], 'Saved Successfully!!' )