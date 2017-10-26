
#include"KMeans.h"


Point::Point(double* data,int dimNum){
	this->data=new double[dimNum];
	for(int i=0;i<dimNum;i++){
		this->data[i]=data[i];
	}
	this->dimension=dimNum;
	this->clusterIndex=-1;
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
	double *distance=new double[clusterNum];
	double *x=new double[this->points.at(0)->dimension];
	int index=-1;
	double min;

	bool isChange=true;
	while(isChange){
		isChange=false;
		for(int i=0;i<this->points.size();i++){
			for(int j=0;j<clusterNum;j++){
				distance[j]=this->points.at(i)->distance(cluCore.at(j));
			}
			min=distance[0];
			index=0;
			for(int j=1;j<clusterNum;j++){
				if(min>distance[j]){
					min=distance[j];
					index=j;
				}
			}
			if(this->points.at(i)->clusterIndex!=index){
				this->points.at(i)->clusterIndex=index;
				isChange=true;
			}
			
		}

		
		int num=0;

		for(int i=0;i<clusterNum;i++){
			for(int k=0;k<this->points.at(0)->dimension;k++){
				x[k]=0;
			}
			num=0;
			for(int j=0;j<this->points.size();j++){
				if(this->points.at(j)->clusterIndex==i){
					for(int k=0;k<this->points.at(i)->dimension;k++){
						x[k]+=this->points.at(j)->data[k];
					}
					num++;
				}
			}
			for(int k=0;k<this->points.at(i)->dimension;k++){
				cluCore.at(i)->data[k]=x[k]/num;
			}
		}
		
	}

	int* clu=new int[this->points.size()];
	for(int i=0;i<this->points.size();i++)
		clu[i]=this->points.at(i)->clusterIndex;

	delete [] distance;
	delete [] x;

	return clu;
}
