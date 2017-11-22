#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""这个程序用于实现单隐层的BP算法"""

import numpy as np
import matplotlib.pyplot as plt

class NN(object):
    """单隐层神经网络"""
    def __init__(self,l,q,d):
        """l:输出层神经元个数
        q:隐藏层神经元数目
        d：输入层神经元数目"""
        #隐层-输出层链接矩阵
        self.w=np.random.uniform(size=(q,l))
        #输入层-隐层链接矩阵
        self.v=np.random.uniform(size=(d,q))
        #输出层阈值
        self.theta=np.zeros(l)
        #隐层阈值
        self.gamma=np.zeros(q)


    def fit(self,x,y):
        """学习样本，学习算法是累积BP算法
        x,样本特征n*d，n是样本数目，d是样本维度，与输入层神经元数目对应
        y,样本对应的标签n*l，n是样本数目，l与输出层神经元数目对应"""
        # 修正步长
        eta = 0.1
        sampleNum=x.shape[0]
        maxGen=10000
        gen=0
        while True:
            gen+=1
            #计算神经元输出
            alpha=np.dot(x,self.v)
            b=self.Activation(alpha-self.gamma)
            beta=np.dot(b,self.w)
            y_1=self.Activation(beta-self.theta)
            #计算累积误差
            E=np.sum(((y_1>0.5)-y)**2)
            # if(gen==200):
            #     E=E
            if E<0.0001 or gen>maxGen:
                break

            temp=np.zeros(y.shape)+1
            g=y_1*(temp-y_1)*(y-y_1)
            e=b*(1-b)*np.dot(g,self.w.T)

            #计算系数的调整值
            delta_w=eta*np.dot(b.T,g)
            delta_theta=-eta*np.sum(g,axis=0)/sampleNum
            delta_v=eta*np.dot(x.T,e)
            delta_gamma=-eta*np.sum(e,axis=0)/sampleNum

            self.w=self.w+delta_w
            self.theta=self.theta+delta_theta
            self.v=self.v+delta_v
            self.gamma=self.gamma+delta_gamma
        print(E)


    def transform(self,x):
        alpha = np.dot(x, self.v)
        b = self.Activation(alpha)
        beta = np.dot(b, self.w)
        y_1 = self.Activation(beta)
        return y_1


    def Activation(self,x):
        """激活函数：sigmoid函数"""
        return 1/(1+np.exp(-x))


if __name__=='__main__':
    nn=NN(1,5,2)
    x=np.array([[0.697,0.460],
                [0.774,0.376],
                [0.634,0.264],
                [0.608,0.318],
                [0.556,0.215],
                [0.403,0.237],
                [0.481,0.149],
                [0.437,0.211],
                [0.666,0.091],
                [0.243,0.267],
                [0.245,0.057],
                [0.343,0.099],
                [0.639,0.161],
                [0.657,0.198],
                [0.36,0.37],
                [0.593,0.042],
                [0.719,0.103]
                ])
    y=np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
    y=y.reshape((17,1))
    # plt.scatter(x[0:8,0],x[0:8,1])
    # plt.scatter(x[8:17, 0], x[8:17, 1])
    # plt.show()
    nn.fit(x,y)
