#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""支持向量机模型"""

import numpy as np
import matplotlib.pyplot as plt


class SVM(object):

    def __init__(self,C,kernal=None):
        """kernal为核函数，如果不输入默认为欧式空间内积计算方法
        C是误分类惩罚因子"""
        self.C=C
        if(kernal is None):
            self.Kernal=lambda x,y:np.sum(x*y)
        else:
            self.Kernal=kernal

    def fit(self,x,y):
        row = x.shape[0]
        Gram = np.zeros((row, row))
        for i in range(row):
            for j in range(i, row):
                if i == j:
                    Gram[i, j] = self.Kernal(x[i, :], x[j, :])
                else:
                    Gram[i, j] = self.Kernal(x[i, :], x[j, :])
                    Gram[j, i] = Gram[i, j]
        self.Gram=Gram
        col=x.shape[1]
        self.w=np.zeros(col)
        self.b=0
        self.x=x
        self.y=y
        self.alpha = np.zeros(row)
        self.E=np.zeros(row)
        for i in range(row):
            self.E[i]=self.g(i)-self.y[i]

        self.SMO()

    def transform(self,x):
        y=np.sum(self.w*x)+self.b
        if y>0:
            return 1
        else:
            return -1

    def SMO(self):
        self.aim=[]
        self.variable=[]
        while(not self.canStop()):

            i1,i2=self.getVariableIndex()
            self.variable.append([i1,i2])
            K11=self.Gram[i1,i1]
            K22=self.Gram[i2,i2]
            K12=self.Gram[i1,i2]
            eta=K11+K22-2*K12
            alpha1_old=self.alpha[i1]
            alpha2_old=self.alpha[i2]
            y1=self.y[i1]
            y2=self.y[i2]
            if(y1==y2):
                L=np.max([0,alpha2_old+alpha1_old-self.C])
                H=np.min([self.C,alpha2_old+alpha1_old])
            else:
                L=np.max([0,alpha2_old-alpha1_old])
                H=np.min([self.C,self.C+alpha2_old-alpha1_old])
            E1=self.E[i1]
            E2=self.E[i2]
            alpha2_new=alpha2_old+y2*(E1-E2)/eta
            if alpha2_new>H:
                alpha2_new=H
            elif alpha2_new<L:
                alpha2_new=L
            alpha1_new=alpha1_old+y1*y2*(alpha2_old-alpha2_new)
            self.alpha[i1]=alpha1_new
            self.alpha[i2]=alpha2_new
            b1_new=-E1-y1*K11*(alpha1_new-alpha1_old)-y2*K12*(alpha2_new-alpha2_old)+self.b
            b2_new=-E2-y1*K12*(alpha1_new-alpha1_old)-y2*K22*(alpha2_new-alpha2_old)+self.b
            self.b=(b1_new+b2_new)/2
            for i in range(self.x.shape[0]):
                self.E[i]=self.g(i)-self.y[i]
            aim = 0
            for i in range(self.x.shape[0]):
                for j in range(self.x.shape[0]):
                    aim += self.alpha[i] * self.alpha[j] * self.y[i] * self.y[j] * self.Gram[i, j]
            aim -= np.sum(self.alpha)
            self.aim.append(aim)
        for i in range(self.x.shape[1]):
            self.w[i]=np.sum(self.alpha*self.y*self.x[:,i])

    def canStop(self):
        """SMO算法的终止条件"""
        if np.sum(self.alpha*self.y)!=0:
            return False
        kkt=np.zeros((self.x.shape[0]))
        for i in range(self.x.shape[0]):
            kkt[i]=self.KKT(i)
        if np.sum(np.abs(kkt))>0.00001:
            return False
        return True

    def g(self,i):
        return np.sum(self.alpha*self.y*self.Gram[:,i])+self.b

    def getVariableIndex(self):
        """选择两个变量"""
        isOK=False
        k=0
        while not isOK:

            row=self.x.shape[0]
            kkt=np.zeros(row)
            for i in range(row):
                kkt[i]=self.KKT(i)
            kktSorted=np.sort(kkt)
            index1=np.where(kkt==kktSorted[row-k//row-1])[0][0]

            E=np.sort(self.E)
            e1=self.E[index1]
            if e1>0:
                index2=np.where(E[k%row]==self.E)[0][0]
                if index2==index1:
                    index2=np.where(E[(k+1)%row]==self.E)[0][0]
            else:
                index2=np.where(E[row-1-k%row]==self.E)[0][0]
                if index2==index1:
                    index2=np.where(E[row-1-(k+1)%row]==self.E)[0][0]
            isOK=True
            num=len(self.aim)
            if num>0:
                aim=self.aim[num-1]
                for i in range(num-1,-1,-1):
                    if(aim==self.aim[i]):
                        if self.variable[i][0]==index1 and self.variable[i][1]==index2:
                            isOK=False
                            break
                    else:
                        break
            k += 1

            # if num>=2:
            #     if self.aim[num-1]==self.aim[num-2]:
            #         if self.variable[num-1][0]==self.variable[num-2][0] \
            #                 and self.variable[num-2][0]==index1\
            #                 and self.variable[num-1][1]==self.variable[num-2][1] \
            #                 and self.variable[num-2][1]==index2:
            #             isOK=False
            #         else:
            #             isOK=True
            #     else:
            #         isOK=True
            # else:
            #     isOK=True

        return index1,index2

    def KKT(self,i):
        """检验变量是否满足KKT条件，若不满足返回与标准值（1）之差的绝对值，否则返回0"""
        alpha=self.alpha[i]
        y=self.y[i]
        g=self.g(i)
        if(alpha==0):
            if(y*g>=1):
                return 0
            else:
                return 1-y*g
        elif(alpha==self.C):
            if(y*g<=1):
                return 0
            else:
                return y*g-1
        else:
            if(y*g==1):
                return 0
            else:
                #优先选择在间隔边界上的点，所以给这些值的偏差乘以1000，
                #以确保可以优先选择
                return np.abs(y*g-1)*1000

if __name__=="__main__":
    x=np.array([[1,2],[2,3],[3,3],[2,1],[3,2]])
    y=np.array([1,1,1,-1,-1])
    svm=SVM(1)
    svm.fit(x,y)
    plt.scatter(x[:,0],x[:,1])
    x=np.linspace(0,4,100)
    y=(svm.w[0]*x+svm.b)/-svm.w[1]
    plt.plot(x,y)
    plt.show()



