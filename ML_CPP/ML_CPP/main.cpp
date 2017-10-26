#include"stdafx.h"
#include"DBSCAN.h"
int main(){
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
	return 0;
}