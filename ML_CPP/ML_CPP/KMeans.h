#include"stdafx.h"



class Point{
public:
	Point(double* data,int dimNum);
	~Point();
	double *data;
	int dimension;
	/*0:未分配簇编号
	其他大于0的值，代表相应的簇编号，这个值始终大于0*/
	int clusterIndex;
	double distance(Point* pt);

};

class KMeans{
public:
	KMeans(double** data,int pointNum,int dimNum);
	vector<Point*> points;
	int* cluster(int clusterNum);

};