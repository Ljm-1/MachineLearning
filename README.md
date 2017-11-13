# MachineLearning

##文件内容

这个库用于存储我在学习深度学习的实践代码。每种方法都编写为一个类，
有头文件和cpp文件。详细的使用方法会在头文件中说明。<br>
我也会在我的博客（https://www.cnblogs.com/sgdd123/ ）中记录我的学习心得。
希望和大家共同进步

##Kmeans聚类方法
这个方法用C++实现，头文件和源文件位置在./ML_CPP/ML_CPP/下。<br>
###使用方法:
```cpp
//声明
KMeans(double** data,int pointNum,int dimNum);
int* cluster(int clusterNum);
//使用
KMeans kmean(data,9,1);
int* clu=kmean.cluster(2);
```
data是二维数组，其行数和列数分别代表点数和维度，以data[2][3]为例，代表有两个点，每个点三个维度。<br>
使用时将数据给入，并说明点数和维度。注意：这里的data最好以动态分配的数组给出，否则会出问题。初始化类对象之后，调用cluster方法
参数代表分类结果中类的个数。例子中的2表示要分为两类。这个函数会返回int型一维数组，存储各个点对应的类别

##DBSCAN聚类方法
这个方法用C++实现，头文件和源文件位置在./ML_CPP/ML_CPP/下。<br>
###使用方法:
```cpp
//声明
DBSCAN(double** data,int pointNum,int dimNum);
int* cluster(double Eps,int Minpts);
//使用
DBSCAN dbs(data,13,2);
int *cluster=dbs.cluster(3,3);
```
data是二维数组，其行数和列数分别代表点数和维度，以data[2][3]为例，代表有两个点，每个点三个维度。<br>
使用时将数据给入，并说明点数和维度。注意：这里的data最好以动态分配的数组给出，否则会出问题。初始化类对象之后，调用cluster方法
参数Eps代表最大相关距离，Minpts代表簇中最小个体数量。这个函数会返回int型一维数组，存储各个点对应的类别

##感知机分类
这个方法用Python实现，文件路径为ML_Python/perceptron.py。这个方法应用*Gram*数组来减少计算量，并求解对偶问题。
这个文件可以直接运行。详细的使用方法可以参考`if __name__=='__main__':`下的代码

##特征处理
这个文件不是对特征处理的方法编写，而是练习应用sklearn库中对数据预处理的函数。我会在文件中加入注释，说明函数对应的方法。有兴趣的同学可以参考。文件位置为./ML_Python/FeatureProcess.py

##sklearn数据挖掘
测试sklearn中的并行处理，流水线处理，自动化调参，持久化。

##支持向量机SMO算法
根据李航老师的《统计学习方法》编写。应用SMO算法求解支持向量机的对偶问题。
###使用方法：
``` python
x=np.array([[1,2],[2,3],[3,3],[2,1],[3,2]])
y=np.array([1,1,1,-1,-1])
svm=SVM(1)
svm.fit(x,y)
kind=svm.transform([2,5])
```
x是变量，y事标签取值为1或者-1。首先由fit对样本集学习，在用transform对测试数据做测试，返回值也为1或者-1