import random


def split_train_dev_data(ratio=0.9):
    total_text = []
    with open('../data/mhy-audio-clear.txt','r') as f1:
        total_text.extend(f1.read().split('\n'))
    with open('../data/mhy-info-clear.txt','r') as f2:
        total_text.extend(f2.read().split('\n'))
    with open('../data/mhy-notice-clear.txt','r') as f3:
        total_text.extend(f3.read().split('\n'))
    with open('../data/mhy-paimeng-clear.txt','r') as f4:
        total_text.extend(f4.read().split('\n'))
    with open('../data/hmy-story-clear.txt','r') as f7:
        total_text.extend(f7.read().split('\n'))

    total_text = list(set(total_text))
    random.shuffle(total_text)
    print(total_text)
    print(len(total_text))

    train_text = total_text[:int(len(total_text)*ratio)]
    val_text= total_text[int(len(total_text)*ratio):]
    with open('../dataset/train.txt','w') as f5:
        [f5.write(i+'\n\n') for i in train_text]

    with open('../dataset/eval.txt','w') as f6:
        [f6.write(i+'\n\n') for i in val_text]


if __name__ == '__main__':
    split_train_dev_data()