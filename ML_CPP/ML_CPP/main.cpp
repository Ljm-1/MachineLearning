#include"stdafx.h"
#include"DBSCAN.h"
#include"KMeans.h"

void DBSCAN_test(){
	double **data=new double*[13];
	for(int i=0;i<13;i++){
		data[i]=new double[2];
	}
	
	double data1[13][2]={{1,2},{2,1},{2,4},{4,3},{5,8},{6,7},{6,9},{7,9},{9,5},{1,12},{3,12},{5,12},{3,3}};
	for(int i=0;i<13;i++)
		for(int j=0;j<2;j++)
			data[i][j]=data1[i][j];
	DBSCAN dbs(data,13,2);
	int *cluster=dbs.cluster(3,3);
	for(int i=0;i<13;i++){
		printf("%d\n",cluster[i]);
	}
}

void KMeans_test(){
	double** data=new double*[9];
	for(int i=0;i<9;i++){
		data[i]=new double[1];
	}
	data[0][0]=80.0;
	data[1][0]=80.1;
	data[2][0]=80.2;
	data[3][0]=80.3;
	data[4][0]=80.4;
	data[5][0]=90.0;
	data[6][0]=80.6;
	data[7][0]=80.7;
	data[8][0]=80.8;

	KMeans kmean(data,9,1);
	int* clu=kmean.cluster(2);
	for(int i=0;i<9;i++){
		printf("%d\n",clu[i]);
	}








}

int main(){
	KMeans_test();
	return 0;
}

