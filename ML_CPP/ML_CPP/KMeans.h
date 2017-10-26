#include"stdafx.h"



class Point{
public:
	Point(double* data,int dimNum);
	double *data;
	int dimension;
	int clusterIndex;
	double distance(Point* pt);

};

class KMeans{
public:
	KMeans(double** data,int pointNum,int dimNum);
	vector<Point*> points;

};