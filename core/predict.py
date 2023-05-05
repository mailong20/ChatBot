from model import *
from utils import align_word_ids
import re

class NER_BERT:
    def __init__(self) -> None:
        self.model = load_model(r'E:\PROJECT\core\checkpoints\bert_model_2.pth')
        use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if use_cuda else "cpu")
        if use_cuda:
            self.model = self.model.cuda()
    def evaluate_one_text(self, sentence):
        label_ids = torch.Tensor(align_word_ids(sentence)).unsqueeze(0).to(self.device)
        # print(label_ids)
        text = tokenizer(sentence, padding='max_length', max_length = 512, truncation=True, return_tensors="pt")
        mask = text['attention_mask'].to(self.device)
        input_id = text['input_ids'].to(self.device)
        logits = self.model(input_id, mask, None)
        logits_clean = logits[0][label_ids != -100]
        predictions = logits_clean.argmax(dim=1).tolist()
    
        prediction_label = [ids_to_labels[i] for i in predictions]
        print(prediction_label)
        sentence = re.findall(r'\w+|[^\w\s]', sentence)
        prediction_label = [sentence[i] for i in range(len(prediction_label)) if 'LOCATION' in prediction_label[i]]
        return ' '.join(prediction_label)

if __name__ == '__main__':
    ner_bert = NER_BERT()
    print(ner_bert.evaluate_one_text('Tôi muốn mua bất động sản xung quanh quận Thanh Khê, Đà Nẵng'))