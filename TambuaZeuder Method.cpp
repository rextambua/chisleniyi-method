// Студент: Тамбуа Рекс Тамиганг, НП301
#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;

bool converge(double *xk, double *xkp,double eps,int n)
{
    double norm = 0;
    for (int i = 0; i < n; i++)
        norm += (xk[i] - xkp[i])*(xk[i] - xkp[i]);
    return (sqrt(norm)<eps);
}

void Seider_method(double a[][3], double b[],int n,double eps){
double p[n],x[n];
for (int i = 0; i < n; i++)
        x[i] = 0;
do
{
    for (int i = 0; i < n; i++)
        p[i] = x[i];
    for (int i = 0; i < n; i++)
    {
        double var = 0;
        for (int j = 0; j < i; j++)
            var += (a[i][j] * x[j]);
        for (int j = i + 1; j < n; j++)
            var += (a[i][j] * p[j]);
        x[i] = (b[i] - var) / a[i][i];
    }
}
while (!converge(x,p,eps,n));

for(int i=0;i<n;i++){
    cout<<"x["<<i+1<<"] = "<<x[i]<<endl;
}
}

int main(){

	double A[3][3], B[3], eps = 0.001;
	A[0][0]=1; A[0][1]=-2; A[0][2]=-3;
	A[1][0]=2; A[1][1]= 1; A[1][2]= 3;
	A[2][0]=3; A[2][1]=-1; A[2][2]=-2;
	B[0]=0;B[1]=1;B[2]=3;

	Seider_method(A,B,3,eps);

	return 0;
}
