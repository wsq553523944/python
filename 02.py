# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import random
import os


def detect_txt():
    filename='Activation_code.txt'

    if os.path.exists(filename):
        os.remove(filename)

def Activation_code(num,length):


    f=open('Activation_code.txt','w')
    f.write('%s activation code below:'%num +'\n\n')
    f.close()

    for i in range(num):

        code=''

        for j in range(length):

            code+=str(random.choice([random.randrange(10), chr(random.randrange(97,123)), chr(random.randrange(65,91))]))

        f=open('Activation_code.txt','a')
        f.write('%s' %code+'\n')
        f.close()

    print('%s activation code created'%num)

if __name__=='__main__':
    num=200
    length=10
    detect_txt()
    Activation_code(num,length)


