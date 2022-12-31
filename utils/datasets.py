import random


def split_train_dev_data(ratio=0.9):
    total_text = []
    with open('../data/mhy-audio-clear.txt','r') as f1:
        total_text.extend(f1.read().split('\n'))
    with open('../data/mhy-info-clear.txt','r') as f2:
        total_text.extend(f2.read().split('\n'))
    with open('../data/mhy-notice-clear.txt','r') as f3:
        total_text.extend(f3.read().split('\n'))
    # with open('../data/mhy-paimeng-clear.txt','r') as f4:
    #     total_text.extend(f4.read().split('\n'))
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
    # split_train_dev_data()

    l = [{'loss': 0.64020166015625, 'learning_rate': 4.814814814814815e-05, 'epoch': 2.2222222222222223},
{'loss': 0.494802978515625, 'learning_rate': 4.62962962962963e-05, 'epoch': 4.444444444444445},
{'loss': 0.4503475341796875, 'learning_rate': 4.4444444444444447e-05, 'epoch': 6.666666666666667},
{'loss': 0.4221873779296875, 'learning_rate': 4.259259259259259e-05, 'epoch': 8.88888888888889},
{'loss': 0.3992412109375, 'learning_rate': 4.074074074074074e-05, 'epoch': 11.11111111111111},
{'loss': 0.378136962890625, 'learning_rate': 3.888888888888889e-05, 'epoch': 13.333333333333334},
{'loss': 0.359121826171875, 'learning_rate': 3.7037037037037037e-05, 'epoch': 15.555555555555555},
{'loss': 0.3456416015625, 'learning_rate': 3.518518518518519e-05, 'epoch': 17.77777777777778},
{'loss': 0.34173046875, 'learning_rate': 3.3333333333333335e-05, 'epoch': 20.0},
{'loss': 0.31800927734375, 'learning_rate': 3.148148148148148e-05, 'epoch': 22.22222222222222},
{'loss': 0.3087744140625, 'learning_rate': 2.962962962962963e-05, 'epoch': 24.444444444444443},
{'loss': 0.3041279296875, 'learning_rate': 2.777777777777778e-05, 'epoch': 26.666666666666668},
{'loss': 0.2941435546875, 'learning_rate': 2.5925925925925925e-05, 'epoch': 28.88888888888889},
{'loss': 0.28655078125, 'learning_rate': 2.4074074074074074e-05, 'epoch': 31.11111111111111},
{'loss': 0.27787646484375, 'learning_rate': 2.2222222222222223e-05, 'epoch': 33.333333333333336},
{'loss': 0.266685546875, 'learning_rate': 2.037037037037037e-05, 'epoch': 35.55555555555556},
{'loss': 0.2641923828125, 'learning_rate': 1.8518518518518518e-05, 'epoch': 37.77777777777778},
{'loss': 0.255072265625, 'learning_rate': 1.6666666666666667e-05, 'epoch': 40.0},
{'loss': 0.2505537109375, 'learning_rate': 1.4814814814814815e-05, 'epoch': 42.22222222222222},
{'loss': 0.24792041015625, 'learning_rate': 1.2962962962962962e-05, 'epoch': 44.44444444444444},
{'loss': 0.23924609375, 'learning_rate': 1.1111111111111112e-05, 'epoch': 46.666666666666664},
{'loss': 0.23980810546875, 'learning_rate': 9.259259259259259e-06, 'epoch': 48.888888888888886},
{'loss': 0.233017578125, 'learning_rate': 7.4074074074074075e-06, 'epoch': 51.111111111111114},
{'loss': 0.2336591796875, 'learning_rate': 5.555555555555556e-06, 'epoch': 53.333333333333336},
{'loss': 0.22778955078125, 'learning_rate': 3.7037037037037037e-06, 'epoch': 55.55555555555556},
{'loss': 0.2268837890625, 'learning_rate': 1.8518518518518519e-06, 'epoch': 57.77777777777778},
{'loss': 0.225998046875, 'learning_rate': 0.0, 'epoch': 60.0}]
    from matplotlib import pyplot as plt



    # 设置x
    x = [i['epoch'] for i in l]
    # 设置y
    y = [i['loss'] for i in l]
    # plot函数需要两个参数，一个是x一个是y
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.size'] = '20'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig, ax = plt.subplots()
    # ax.plot(squares, linewidth=3)
    ax.set_title("平方数", fontsize=24)
    ax.set_xlabel("数值", fontsize=14)
    ax.set_ylabel("数值的平方", fontsize=14)
    ax.tick_params(axis='both', labelsize=14)

    plt.plot(x, y)
    plt.show()
