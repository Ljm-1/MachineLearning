#include"stdafx.h"



class Point{
public:
	Point(double* data,int dimNum);
	~Point();
	double *data;
	int dimension;
	/*0:δ����ر��
	��������0��ֵ��������Ӧ�Ĵر�ţ����ֵʼ�մ���0*/
	int clusterIndex;
	double distance(Point* pt);

};

class KMeans{
public:
	KMeans(double** data,int pointNum,int dimNum);
	vector<Point*> points;
	int* cluster(int clusterNum);

};