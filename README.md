### 1、项目介绍

第一个基于《原神》游戏训练的大型语言模型，我暂且称之为GenshinBert。该模型目前可以理解原神游戏中的常见人名、地名、活动名等基本要素。目前还未在实体识别、文本分类、关系抽取等下游任务中进行finetune，主要还是无法获取到相关的数据集，也希望旅行者们可以加入一起完成这个项目。

### 2、项目进行

1.基于原神游戏语料的继续预训练。✅

2.下游任务数据集构建。❎

3.基于GenshinBert的下游任务finetune。❎



### 3、模型对比（第一阶段）

| model        | sentence                                                     |
| ------------ | ------------------------------------------------------------ |
| 原始句子     | 翠绿<u>**猎**</u>人的<u>**笃**</u>定：猎人曾经随身携带的奇妙仪器，永远指向自己的<u>**猎**</u>物。 |
| genshin-bert | 翠绿<u>**猎**</u>人的<u>**命**</u>定：猎人曾经随身携带的奇妙仪器，永远指向自己的<u>**猎**</u>物。 |
| bert-wwm-ext | 翠绿<u>**猎**</u>人的<u>**决**</u>定：猎人曾经随身携带的奇妙仪器，永远指向自己的<u>**猎**</u>物。 |
|              |                                                              |
| 原始句子     | 申<u>**鹤**</u>五岁时，母亲因<u>**病**</u>去世，父亲爱<u>**妻**</u>情切，难以承受此中苦痛。 |
| genshin-bert | 申<u>**鹤**</u>五岁时，母亲因<u>**病**</u>去世，父亲爱<u>**民**</u>情切，难以承受此中苦痛。 |
| bert-wwm-ext | 申<u>**[ U N K ]**</u>五岁时，母亲因<u>**病**</u>去世，父亲爱<u>**子**</u>情切，难以承受此中苦痛。 |
|              |                                                              |
| 原始句子     | 所以，不仅仅是遵守<u>**摩**</u>拉克斯的神<u>**谕**</u>，更是为了让璃<u>**月**</u>港时刻保持活力，璃月<u>**七**</u>星对所有违反律法的人绝不姑息。 |
| genshin-bert | 所以，不仅仅是遵守<u>**摩**</u>拉克斯的神<u>**谕**</u>，更是为了让璃<u>**月**</u>港时刻保持活力，璃月<u>**七**</u>星对所有违反律法的人绝不姑息。 |
| bert-wwm-ext | 所以，不仅仅是遵守<u>**克**</u>拉克斯的神<u>**谕**</u>，更是为了让璃<u>**月**</u>港时刻保持活力，璃月<u>**之**</u>星对所有违反律法的人绝不姑息。 |
|              |                                                              |
| 原始句子     | 那个<u>**坎**</u>蒂丝是是真正的<u>**赤**</u>王后裔。在须弥城的酒馆中，一位狼狈不堪的镀<u>**金旅**</u>团成员哆嗦着说道。 |
| genshin-bert | 那个<u>**坎**</u>蒂丝是是真正的<u>**赤**</u>王后裔。在须弥城的酒馆中，一位狼狈不堪的镀<u>**金旅**</u>团成员哆嗦着说道。 |
| bert-wwm-ext | 那个<u>**丝**</u>蒂丝是是真正的<u>**国**</u>王后裔。在须弥城的酒馆中，一位狼狈不堪的镀<u>**金军**</u>团成员哆嗦着说道。 |
|              |                                                              |
| 原始句子     | 一旁的万<u>**叶**</u>又陷入了回忆。“他曾是我的<u>**挚**</u>友，那天他向我问起，可曾听说过无<u>**想**</u>的一刀，我说自然。 |
| genshin-bert | 一旁的万<u>**叶**</u>又陷入了回忆。“他曾是我的<u>**朋**</u>友，那天他向我问起，可曾听说过无<u>**想**</u>的一刀，我说自然。 |
| bert-wwm-ext | 一旁的万<u>**里**</u>又陷入了回忆。“他曾是我的<u>**朋**</u>友，那天他向我问起，可曾听说过无<u>**情**</u>的一刀，我说自然。 |
|              |                                                              |
| 原始句子     | 璃月的宫司大人其实就是<u>**八重**</u>神<u>**子**</u>啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。 |
| genshin-bert | 璃月的宫司大人其实就是<u>**八重**</u>神<u>**子**</u>啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。 |
| bert-wwm-ext | 璃月的宫司大人其实就是<u>**转月**</u>神<u>**社**</u>啦！在八重堂举办的转生成为八重宫司征文活动中，诞生了不少优秀的作品。 |

### 4、训练过程

模型采用从米游社获取而来的数据，大约是2.8w的文本数据，已经经过数据清洗和去重，每条训练语料长度在20-256左右；在2块3090上训练60个epoch，并未完全训练到收敛。

<img src="/Users/maoyufeng/slash/project/GenshinBert/src/3F50B7F8-AAEF-4429-8D11-D8D7AEFA7CBE.png" alt="3F50B7F8-AAEF-4429-8D11-D8D7AEFA7CBE" style="zoom:50%;" />

