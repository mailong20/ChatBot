from transformers import BertTokenizerFast,BertForTokenClassification
unique_labels = {'I-ORGANIZATION', 'I-PERSONTYPE', 'B-ORGANIZATION', 'I-LOCATION', 'O', 'B-PERSON', 'B-LOCATION', 'I-PRODUCT', 'I-PERSON', 'B-PRODUCT', 'B-PERSONTYPE'}
ids_to_labels = {v: k for v, k in enumerate(sorted(unique_labels))}

tokenizer = BertTokenizerFast.from_pretrained('bert-base-multilingual-cased')

label_all_tokens = False
def align_word_ids(texts):
  
    tokenized_inputs = tokenizer(texts, padding='max_length', max_length=512, truncation=True)

    word_ids = tokenized_inputs.word_ids()

    previous_word_idx = None
    label_ids = []

    for word_idx in word_ids:

        if word_idx is None:
            label_ids.append(-100)

        elif word_idx != previous_word_idx:
            try:
                label_ids.append(1)
            except:
                label_ids.append(-100)
        else:
            try:
                label_ids.append(1 if label_all_tokens else -100)
            except:
                label_ids.append(-100)
        previous_word_idx = word_idx

    return label_ids