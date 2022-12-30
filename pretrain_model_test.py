from transformers import RobertaTokenizer, RobertaForMaskedLM,BertTokenizer,BertForMaskedLM
import torch


model_path = 'genshin-bert'
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForMaskedLM.from_pretrained(model_path)
model_org = BertForMaskedLM.from_pretrained('/Users/maoyufeng/slash/models/chinese-bert-wwm-ext')
text = '原[MASK]游戏中有一个城市叫做[MASK]月，里面有一位岩神，他的名字叫做[MASK]拉克斯，也叫做钟[MASK]。他曾经封印了[MASK]陀龙王'
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

pred_tokens =tokenizer.decode(pred[1:-1])
pred_tokens1 =tokenizer.decode(pred1)


print(f"原始句子：{text}")
print(f"预测句子：{pred_tokens.replace(' ','')}")
print(f"预测句子1：{pred_tokens1.replace(' ','')}")
