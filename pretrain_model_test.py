import copy

from transformers import BertTokenizer,BertForMaskedLM
import torch



if __name__ == '__main__':
    model_path = 'genshin-bert'
    tokenizer = BertTokenizer.from_pretrained(model_path)
    genshin_bert = BertForMaskedLM.from_pretrained(model_path)
    wwm_bert = BertForMaskedLM.from_pretrained('/Users/maoyufeng/slash/models/chinese-bert-wwm-ext')
    text = ['翠绿[MASK]人的[MASK]定：猎人曾经随身携带的奇妙仪器，永远指向自己的[MASK]物。',
            '申[MASK]五岁时，母亲因[MASK]去世，父亲爱[MASK]情切，难以承受此中苦痛。',
            '所以，不仅仅是遵守[MASK]拉克斯的神[MASK]，更是为了让璃[MASK]港时刻保持活力，璃月[MASK]星对所有违反律法的人绝不姑息。',
            '提[MASK]里初至[MASK]城[MASK]时还只是巡[MASK]队中的普通一员，与其他巡林官别无二致。',
            '那个[MASK]蒂丝是是真正的[MASK]王后裔。在须[MASK]城的酒馆中，一位狼狈不堪的镀[MASK][MASK]团成员哆嗦着说道。',
            '一旁的万[MASK]又陷入了回忆。“他曾是我的[MASK]友，那天他向我问起，可曾听说过无[MASK]的一刀，我说自然。',
            '第一章第一幕完成浮世浮生千[MASK]间好了，他找到的那个人不会是帝[MASK]大人吧？看着屏幕上眼熟的“钱包”，一群人想到了之前说的[MASK][MASK]是帝君的钱包？',
            '“如果我没记错的话，据史料记载，[MASK][MASK]人千年前就有了。而坎[MASK]亚的覆灭是500年前。”“也是500年前，丘丘人增加了很多...”',
            '璃月的宫司大人其实就是[MASK][MASK]神[MASK]啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。']
    res = ['翠绿猎人的笃定：猎人曾经随身携带的奇妙仪器，永远指向自己的猎物。',
           '申鹤五岁时，母亲因病去世，父亲爱妻情切，难以承受此中苦痛。',
           '所以，不仅仅是遵守摩拉克斯的神谕，更是为了让璃月港时刻保持活力，璃月七星对所有违反律法的人绝不姑息。',
           '提纳里初至化城郭时还只是巡林队中的普通一员，与其他巡林官别无二致。',
           '那个坎蒂丝是是真正的赤王后裔。在须弥城的酒馆中，一位狼狈不堪的镀金旅团成员哆嗦着说道。',
           '一旁的万叶又陷入了回忆。“他曾是我的挚友，那天他向我问起，可曾听说过无想的一刀，我说自然。',
           '第一章第一幕完成浮世浮生千岩间好了，他找到的那个人不会是帝君大人吧？看着屏幕上眼熟的“钱包”，一群人想到了之前说的公子是帝君的钱包？',
           '“如果我没记错的话，据史料记载，丘丘人千年前就有了。而坎瑞亚的覆灭是500年前。”“也是500年前，丘丘人增加了很多...”',
           '璃月的宫司大人其实就是八重神子啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。']
    for i in range(len(text)):
        text_tokens = tokenizer(text[i], add_special_tokens=True, padding=True, return_tensors='pt')
        genshin_outputs = genshin_bert(**text_tokens, return_dict=True, output_hidden_states=True)
        wwm_outputs = wwm_bert(**text_tokens, return_dict=True, output_hidden_states=True)

        genshin_pred = torch.argmax(genshin_outputs.logits, dim=-1).cpu().numpy().tolist()[0]
        wwm_pred = torch.argmax(wwm_outputs.logits, dim=-1).cpu().numpy().tolist()[0]

        s1 = copy.deepcopy(text[i])
        s2 = copy.deepcopy(text[i])
        while '[MASK]' in s1:
            p = s1.find('[MASK]')
            if p != -1:
                pred_word1 = tokenizer.decode(genshin_pred[p+1])
                pred_word2 = tokenizer.decode(wwm_pred[p+1])
                s1 = s1.replace('[MASK]',pred_word1,1)
                s2 = s2.replace('[MASK]', pred_word2, 1)
        print(f"{res[i]}")
        print(f"MASK句子：{text[i]}")
        print(f"genshin-bert 预测句子：{s1}")
        print(f"bert-wwm-ext 预测句子：{s2}\n")

