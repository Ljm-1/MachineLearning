#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""特征处理方法"""

import numpy as np
import sklearn as sk
from sklearn.datasets import load_iris
from sklearn.preprocessing import *
from sklearn.feature_selection import *
from scipy.stats import pearsonr,chisquare


class Feature(object):

    def __init__(self):
        data=load_iris()
        self.data=data['data']
        self.target=data['target']

    def dataPreProcessing(self,x):
        '''数据预处理方法'''
        if x==0:
            #标准化,对每一列数据做标准化，即乘以z-score算子，使得该列的方差为1，均值为0
            data = StandardScaler().fit_transform(self.data)
            #求均值，0代表对列，1代表对行
            print(np.mean(data,axis=0))
            #cov求协方差，默认每一列为一个样本，每一行为一个维度
            #var对矩阵中的所有数据求方差
            print(np.cov(data.T))
            print(np.var(data))
        elif x==1:
            #区间缩放法
            data= MinMaxScaler(feature_range=(2,3)).fit_transform(self.data)
            print(np.min(data))
            print(np.max(data))

            #归一化,实质是将每一行（每一个样本）缩放为单位向量
            data=Normalizer().fit_transform(self.data)
            print(np.sum(data[2,:]**2))

            #二值化，大于阈值的赋值为1，小于等于阈值的赋值为0
            data=Binarizer(threshold=3).fit_transform(self.data)
            print(data)
        elif x==2:
            #独热编码，将定性数据转换为0-1数据,这样做的目的是使得类型之间的距离更加合理
            #这里使用自己的数据更能说明问题
            data=np.array([[1,0,3.25],
                           [0,0,5.2],
                           [2,1,3.6]])
            enc=OneHotEncoder(categorical_features=np.array([0,1]),n_values=[3,2])
            enc.fit(data)
            data=enc.transform(data).toarray()
            print(data)
        elif x==3:
            #缺失值计算
            data=np.array([[1,0,3.25],
                           [0,0,5.2],
                           [2,1,3.6]])

            data=np.row_stack((np.array([np.nan,np.nan,np.nan]),data))
            data=Imputer().fit_transform(data)
            print(data)
        elif x==4:
            #多项式变换
            data = np.array([[1, 0, 3.25],
                             [0, 0, 5.2],
                             [2, 1, 3.6]])
            data=PolynomialFeatures(degree=2).fit_transform(data)
            print(data)

        elif x==5:
            #函数变换
            data = np.array([[1, 0, 3.25],
                             [0, 0, 5.2],
                             [2, 1, 3.6]])
            def func(x):
                return x+1
            data=FunctionTransformer(func).fit_transform(data)
            print(data)

    def featureSelect(self,x):
        """特征选择"""
        if x==0:
            #方差选择法，方差大于门限值的列作为特征
            data=self.data
            data=VarianceThreshold(threshold=3).fit_transform(data)
            print(data.shape)
        elif x==1:
            #相关系数法，根据相关系数的大小来选取特征
            data = np.array([[1, 0, 3.25],
                             [0, 0, 5.2],
                             [2, 1, 3.6]])
            target=np.array([6,10,7])
            def func(x,y):
                ans=np.zeros((x.shape[1],2))
                for i in range(x.shape[1]):
                    ans[i,:]=pearsonr(x[:,i],y)
                return ans[:,0]

            #SelectKBest函数根据func函数返回的结果选择特征，要求返回值必须是一维数组，值越大特征越好
            data=SelectKBest(func,k=2).fit_transform(data,target)
            print(data.shape)

        elif x==2:
            #卡方检验,这个方法有问题，卡方检验统计量越小两者相关性越高，使用SelectKBest函数只能选择最大值
            data=self.data
            target=self.target
            print(chi2(data, target))
            data=SelectKBest(chi2,k=2).fit_transform(data,target)

            print(data.shape)





if __name__=='__main__':

    f=Feature()
    # f.dataPreProcessing(5)
    f.featureSelect(2)
