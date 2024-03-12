import unittest
from src.tokenizer import convert_to_ner_format

class TestTokenizer(unittest.TestCase):

    def test_convert_to_ner_format(self):
        
        input_data = {
            "kararlar": [
                {
                    "_etiketler":
                                [
                                    {
                                        "tokens":
                                        [
                                            "Cem",
                                            "Talip",
                                            "Ovgu",
                                            "Kerem",
                                            "Ali"
                                        ],
                                        "ner_tags":
                                        [
                                            "ERKEK",
                                            "ERKEK",
                                            "KADIN",
                                            "ERKEK",
                                            "ERKEK"
                                        ]
                                    }
                                ],
                    "_karar": "Davanın kısmen Cem kabulünen 2022/1584 Talip Karar sayılı BOZMA kararı Ovgu Kerem Ali",
                }
            ]
        }

        expected_output_data = {
            "id": "0",
            "ner_tags": [
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                1,
                1
            ],
            "tokens": [
                "Dava",
                "##nın",
                "kısmen",
                "Cem",
                "kabulü",
                "##ne",
                "##n",
                "20",
                "##22",
                "/",
                "15",
                "##84",
                "Talip",
                "Karar",
                "sayılı",
                "BO",
                "##Z",
                "##MA",
                "kararı",
                "Ovgu",
                "Kerem",
                "Ali"
            ]
        }
        
        output_data = convert_to_ner_format(input_data)

        self.assertEqual(output_data, expected_output_data)

if __name__ == '__main__':
    unittest.main()
