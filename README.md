# NER FORMAT CONVERTER

For the task you mentioned, we need to convert the input file, input_format.json, into the format of the NER model developed with the BERT language model.

The desired format is as follows:

{
 'id': '0',
 'ner_tags': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 8, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
 'tokens': ['@paulwalk', 'It', "'s", 'the', 'view', 'from', 'where', 'I', "'m", 'living', 'for', 'two', 'weeks', '.', 'Empire', 'State', 'Building', '=', 'ESB', '.', 'Pretty', 'bad', 'storm', 'here', 'last', 'evening', '.']
}

It seems that the token list specified in the WNUT 17 format needs to be generated using BERT's own tokenizer.

The important part of the input file is as follows:


"_etiketler":
    [
        {
            "tokens":
            [
                "Zahit"
            ],
            "ner_tags":
            [
                "ERKEK"
            ]
        }
    ],

Here, the tokens represent the names occurring in the text, and ner_tags represent the corresponding NER labels of these tokens.
Therefore, the code you write should be flexible to add new NER labels as new ones are encountered in the input files as new IDs in the output format.
Additionally, 0 represents "Other," meaning named entities not listed in the _etiketler list.