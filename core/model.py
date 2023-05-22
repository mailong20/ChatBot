import torch
from transformers import BertTokenizerFast,BertForTokenClassification
from .utils import unique_labels, ids_to_labels, tokenizer


class BertModel(torch.nn.Module):

    def __init__(self):

        super(BertModel, self).__init__()
        
        self.bert = BertForTokenClassification.from_pretrained('bert-base-multilingual-cased', num_labels=len(unique_labels))

    def forward(self, input_id, mask, label):

        output = self.bert(input_ids=input_id, attention_mask=mask, labels=label, return_dict=False)

        return output
def load_model(model_path):
    model = BertModel()
    # load checkpoint
    try:
        model.load_state_dict(torch.load(model_path))
        print("gpu")
    except: 
        model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        print('cpu')
    return model






             
# evaluate_one_text(model, 'tổng thống mỹ joni biden đang có chuyến công tác tại thành phố Đà Nẵng, và đi trên xe oto Merceder rồi dùng chiếc điện thoại Samsung-Flip-v4 tại hội Phụ nữ Việt Nam')
