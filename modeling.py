from transformers import BertModel,BertTokenizer,BertForMaskedLM
import torch.nn as nn


class GenshinBert(nn.Module):

    def __init__(self):
        super().__init__()
        self.bert = BertModel.fro


