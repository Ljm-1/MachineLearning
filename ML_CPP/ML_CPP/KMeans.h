#include"stdafx.h"



class Point{
public:
	Point(double* data,int dimNum);
	~Point();
	double *data;
	int dimension;
	/*-1:δ����ر��
	������ֵ��������Ӧ�Ĵر�ţ����ֵʼ�մ��ڵ���0*/
	int clusterIndex;
	double distance(Point* pt);

};

class KMeans{
public:
	KMeans(double** data,int pointNum,int dimNum);
	vector<Point*> points;
	int* cluster(int clusterNum);

};