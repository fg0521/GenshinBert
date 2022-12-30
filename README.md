第一个基于《原神》游戏训练的大型语言模型，我暂且称之为GenshinBertV1，由2w+的训练数据在chinese-bert-wwm-ext上继续预训练得到。</br>
下面是对比原始的bert：</br>
原始句子：翠绿猎人的笃定：猎人曾经随身携带的奇妙仪器，永远指向自己的猎物。</br>
MASK句子：翠绿[MASK]人的[MASK]定：猎人曾经随身携带的奇妙仪器，永远指向自己的[MASK]物。</br>
genshin-bert：翠绿猎人的命定：猎人曾经随身携带的奇妙仪器，永远指向自己的猎物。</br>
bert-wwm-ext：翠绿猎人的决定：猎人曾经随身携带的奇妙仪器，永远指向自己的猎物。</br>
</br>
原始句子：申鹤五岁时，母亲因病去世，父亲爱妻情切，难以承受此中苦痛。</br>
MASK句子：申[MASK]五岁时，母亲因[MASK]去世，父亲爱[MASK]情切，难以承受此中苦痛。</br>
genshin-bert：申鹤五岁时，母亲因病去世，父亲爱民情切，难以承受此中苦痛。</br>
bert-wwm-ext：申[ U N K ]五岁时，母亲因病去世，父亲爱子情切，难以承受此中苦痛。</br>
</br>
原始句子：所以，不仅仅是遵守摩拉克斯的神谕，更是为了让璃月港时刻保持活力，璃月七星对所有违反律法的人绝不姑息。</br>
MASK句子：所以，不仅仅是遵守[MASK]拉克斯的神[MASK]，更是为了让璃[MASK]港时刻保持活力，璃月[MASK]星对所有违反律法的人绝不姑息。</br>
genshin-bert：所以，不仅仅是遵守摩拉克斯的神谕，更是为了让璃月港时刻保持活力，璃月七星对所有违反律法的人绝不姑息。</br>
bert-wwm-ext：所以，不仅仅是遵守克拉克斯的神谕，更是为了让璃月港时刻保持活力，璃月之星对所有违反律法的人绝不姑息。</br>
</br>
原始句子：提纳里初至化城郭时还只是巡林队中的普通一员，与其他巡林官别无二致。</br>
MASK句子：提[MASK]里初至[MASK]城[MASK]时还只是巡[MASK]队中的普通一员，与其他巡林官别无二致。</br>
genshin-bert：提纳里初至阿城郭时还只是巡林队中的普通一员，与其他巡林官别无二致。</br>
bert-wwm-ext：提阿里初至长城府时还只是巡林队中的普通一员，与其他巡林官别无二致。</br>
</br>
原始句子：那个坎蒂丝是是真正的赤王后裔。在须弥城的酒馆中，一位狼狈不堪的镀金旅团成员哆嗦着说道。</br>
MASK句子：那个[MASK]蒂丝是是真正的[MASK]王后裔。在须[MASK]城的酒馆中，一位狼狈不堪的镀[MASK][MASK]团成员哆嗦着说道。</br>
genshin-bert：那个坎蒂丝是是真正的赤王后裔。在须弥城的酒馆中，一位狼狈不堪的镀金旅团成员哆嗦着说道。</br>
bert-wwm-ext：那个丝蒂丝是是真正的国王后裔。在须弥城的酒馆中，一位狼狈不堪的镀金军团成员哆嗦着说道。</br>
</br>
原始句子：一旁的万叶又陷入了回忆。“他曾是我的挚友，那天他向我问起，可曾听说过无想的一刀，我说自然。</br>
MASK句子：一旁的万[MASK]又陷入了回忆。“他曾是我的[MASK]友，那天他向我问起，可曾听说过无[MASK]的一刀，我说自然。</br>
genshin-bert：一旁的万叶又陷入了回忆。“他曾是我的朋友，那天他向我问起，可曾听说过无想的一刀，我说自然。</br>
bert-wwm-ext：一旁的万里又陷入了回忆。“他曾是我的朋友，那天他向我问起，可曾听说过无情的一刀，我说自然。</br>
</br>
第一章第一幕完成浮世浮生千岩间好了，他找到的那个人不会是帝君大人吧？看着屏幕上眼熟的“钱包”，一群人想到了之前说的公子是帝君的钱包？</br>
MASK句子：第一章第一幕完成浮世浮生千[MASK]间好了，他找到的那个人不会是帝[MASK]大人吧？看着屏幕上眼熟的“钱包”，一群人想到了之前说的[MASK][MASK]是帝君的钱包？</br>
genshin-bert：第一章第一幕完成浮世浮生千岩间好了，他找到的那个人不会是帝君大人吧？看着屏幕上眼熟的“钱包”，一群人想到了之前说的：就是帝君的钱包？</br>
bert-wwm-ext：第一章第一幕完成浮世浮生千年间好了，他找到的那个人不会是帝君大人吧？看着屏幕上眼熟的“钱包”，一群人想到了之前说的难不是帝君的钱包？</br>
</br>
原始句子：“如果我没记错的话，据史料记载，丘丘人千年前就有了。而坎瑞亚的覆灭是500年前。”“也是500年前，丘丘人增加了很多...”</br>
MASK句子：“如果我没记错的话，据史料记载，[MASK][MASK]人千年前就有了。而坎[MASK]亚的覆灭是500年前。”“也是500年前，丘丘人增加了很多...”</br>
genshin-bert：“如果我没记错的话，据史料记载，丘丘人千年前就有了。而坎瑞亚的覆灭是500年前。”“也是500年前，丘丘人增加了很多...”</br>
bert-wwm-ext：“如果我没记错的话，据史料记载，丘丘人千年前就有了。而坎比亚的覆灭是500年前。”“也是500年前，丘丘人增加了很多...”</br>
</br>
原始句子：璃月的宫司大人其实就是八重神子啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。</br>
MASK句子：璃月的宫司大人其实就是[MASK][MASK]神[MASK]啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。</br>
genshin-bert：璃月的宫司大人其实就是八重神子啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。</br>
bert-wwm-ext：璃月的宫司大人其实就是转月神社啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。</br>