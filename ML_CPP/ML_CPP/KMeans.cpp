
#include"KMeans.h"


Point::Point(double* data,int dimNum){
	this->data=new double[dimNum];
	for(int i=0;i<dimNum;i++){
		this->data[i]=data[i];
	}
}


class Point1{
	Point1(double* data,int dimNum);
	double *data;
	int dimension;
	int clusterIndex;
	double distance(Point* pt);

}

class KMeans{
	KMeans(double** data,int pointNum,int dimNum);
	vector<Point*> points;

}