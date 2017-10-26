
#include"KMeans.h"


Point::Point(double* data,int dimNum){
	this->data=new double[dimNum];
	for(int i=0;i<dimNum;i++){
		this->data[i]=data[i];
	}
	this->dimension=dimNum;
	this->clusterIndex=0;
}

Point::~Point(){
	delete [] data;
}

double Point::distance(Point* pt){
	double L=0;
	for(int i=0;i<this->dimension;i++){
		L+=pow(this->data[i]-pt->data[i],2);
	}
	return sqrt(L);
}


KMeans::KMeans(double** data,int pointNum,int dimNum){
	points.reserve(50);
	Point* pt;
	for(int i=0;i<pointNum;i++){
		pt=new Point(data[i],dimNum);
		this->points.push_back(pt);
	}
}

int* KMeans::cluster(int clusterNum){
	vector<Point*> cluCore;
	cluCore.reserve(clusterNum);
	for(int i=0;i<clusterNum;i++){
		Point *pt=new Point(this->points.at(i)->data,this->points.at(i)->dimension);
		cluCore.push_back(pt);
	}
	double *distance=new double[this->points.at(0)->dimension];
	int index=-1;

	for(int i=0;i<this->points.size();i++){
		for(int j=0;j<this->points.at(0)->dimension;j++){
			distance[j]=
		}

	}
}
