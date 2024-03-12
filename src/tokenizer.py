import json
from transformers import BertTokenizer, BertModel

# Declare input and output files
input_file = 'input_short.json'
output_file = 'output.json'

# Converts the input data to desired NER format
def convert_to_ner_format(data):
    
    # Load BERT tokenizer
    # I had the best results with bert-base-turkish-cased tokenizer so I used this.
    # We also need the model since we will be changing the vocabulary
    tokenizer = BertTokenizer.from_pretrained('dbmdz/bert-base-turkish-cased')
    model = BertModel.from_pretrained('dbmdz/bert-base-turkish-cased')

    # these are the 2 lists the output JSON file is comprised of
    ner_tags = []
    tokens = []

    # These hold the JSON data
    ner_tag_strings = []
    special_tokens = []

    # Get the string ner tags and tokens from the json file data
    for entry in data["kararlar"]:
        for etiket in entry.get("_etiketler", []):
            ner_tag_strings = etiket.get("ner_tags", [])
            special_tokens = etiket.get("tokens", [])

    # Add a number corresponding to every new string seen in the ner_tags entry in the json file
    ner_number_dict = {}
    i=1
    for ner_tag_string in ner_tag_strings:
        if ner_tag_string not in ner_number_dict:
            ner_number_dict[ner_tag_string] = i
            i = i + 1


    # Add the corresponding number to every token given in the tokens part of the json file
    ner_dict = {}
    for token, ner_tag in zip(special_tokens, ner_tag_strings):
        ner_dict[token] = ner_number_dict.get(ner_tag)


    # Add all special tokens to tokenizer vocabulary so that they dont get split up if unrecognised
    tokenizer.add_tokens(special_tokens)
    model.resize_token_embeddings(len(tokenizer))

    # Tokenize the _karar entry 
    tokens = tokenizer.tokenize(entry.get("_karar",[]))

    # Fill out the ner_tags according to ner_dict
    for token in tokens:
        if token in ner_dict:
            ner_tags.append(ner_dict.get(token))
        else:
            ner_tags.append(0)

    return {
        'id': '0',
        'ner_tags': ner_tags,
        'tokens': tokens
    }

if __name__ == '__main__':

    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Run the conversion function
    output_data = convert_to_ner_format(data)

    # Write to the output file, ensure_ascii tag is to prevent turkish characters from
    # being printed as ascii code
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

