import copy

from transformers import RobertaTokenizer, RobertaForMaskedLM,BertTokenizer,BertForMaskedLM
import torch


model_path = 'genshin-bert'
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForMaskedLM.from_pretrained(model_path)
model_org = BertForMaskedLM.from_pretrained('/Users/maoyufeng/slash/pre_trained_models/chinese-bert-wwm-ext')
text = '那太好了，那就麻烦珊瑚[MASK]心[MASK]大人啦。'
text_tokens = tokenizer(text, add_special_tokens=True,
                             padding=True, return_tensors='pt')


outputs = model(**text_tokens, return_dict=True,
                            output_hidden_states=True)
outputs1 = model_org(**text_tokens, return_dict=True,
                            output_hidden_states=True)
logits = outputs.logits
pred = torch.argmax(logits, dim=-1)
pred = pred.data.cpu().numpy().tolist()[0]

pred1 = torch.argmax(outputs1.logits, dim=-1).cpu().numpy().tolist()[0]


s = copy.deepcopy(text)
# pos = []
while '[MASK]' in s:
    p = s.find('[MASK]')
    if p != -1:
        # pos.append(p+1)
        pred_word = tokenizer.decode(pred[p+1])
        s = s.replace('[MASK]',pred_word,1)
print(f"原始句子：{text}")
print(f"预测句子：{s}")


# pred_tokens =tokenizer.decode(pred[1:-1])
# pred_tokens1 =tokenizer.decode(pred1)
# print(tokenizer.decode(pred[11]))

# print(f"预测句子：{pred_tokens.replace(' ','')}")
# print(f"预测句子1：{pred_tokens1.replace(' ','')}")
