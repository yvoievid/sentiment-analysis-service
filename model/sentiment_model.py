import torch
from transformers import BertForSequenceClassification, BertTokenizerFast

class SentimentModel:
    model_path = "./model/BERT_ft.model"
    device = torch.device('cpu')
    def __init__(self):
        self.model_id = "bert-base-uncased"
        self.model = BertForSequenceClassification.from_pretrained(
            self.model_id,
            num_labels = 2,
            output_attentions = False,
            output_hidden_states = False
        )
        self.model.load_state_dict(torch.load(self.model_path, map_location= self.device))
        self.model.eval()
        self.tokenizer = BertTokenizerFast.from_pretrained(self.model_id)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        logits = self.model(**inputs).logits
        probability_class = torch.argmax(logits, dim=1).item()
        review = self.probabilities_to_text(probability_class)
        return review


    def probabilities_to_text(self, probability):
        if probability < 0.5:
            return "Positive"
        else:
            return "Negative"
