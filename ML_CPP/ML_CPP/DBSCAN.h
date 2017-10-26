#include"stdafx.h"

#define COREPOINT 1
#define BORDERPOINT 2
#define NOISEPOINT 3


//个体类，不直接使用
class Ind{
public:
	Ind(double* data,int dimNum);
	int dimension;
	vector<Ind*> neighbour;
	//计算距离
	double distance(Ind* ind);
	double *data;
	~Ind();
	/*0:未分类
	1：核心点
	2：边界点
	3：噪音点*/
	int kind;
	/*0:没有分配簇编号
	-1：噪音点的簇编号
	除此以外的所有值均为簇编号*/
	int cluster;
	//递归调用，将邻居节点划归为同一类
	void setCluster(int cluster);

};


class DBSCAN{
public:
	//data为数据，每一行是一个个体（点），每一列是一个维度
	DBSCAN(double** data,int pointNum,int dimNum);
	~DBSCAN();
	vector<Ind*> points;
	double** distance;
	//设定同类间距Eps和簇中最小个体数目Minpts，函数返回Int* 类型数组，维度是data行数，每个值对应
	//各点的簇编号
	int* cluster(double Eps,int Minpts);
};

