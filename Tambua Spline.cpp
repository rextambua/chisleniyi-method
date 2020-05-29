// Студент: Тамбуа Рекс Тамиганг, НП301
#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

double func(double x){
    return sqrt(x)*sin(x)+1;
}

double deriv_func(double x){
    return (func(x+0.0001)-func(x))/0.0001;
}

ofstream outfile1;
ofstream outfile2;

void interpolation(double  x[],int N){
    outfile1.open("Original.txt");
    outfile2.open("spline.txt");

    double f[N],df[N],a[N-1],b[N-1],c[N-1],d[N-1],y,delta;
    for(int i=0;i<N; i++){
        f[i] = func(x[i]);
        df[i] = deriv_func(x[i]);
    }
    for(int i =0; i<N-1; i++){
        delta = x[i+1] - x[i];
        a[i] =(2*(f[i]-f[i+1])+delta*(df[i]+df[i+1]))/pow(delta,3);
        b[i] =(3*(f[i+1]-f[i])-delta*(df[i+1]+2*df[i]))/pow(delta,2);
        c[i] = df[i];
        d[i] = f[i];

        double step = delta/20,s;
        s =x[i];
        while(s<=x[i+1]){
            y = a[i]*pow(s-x[i],3)+b[i]*pow(s-x[i],2)+c[i]*(s-x[i])+d[i];
            outfile1<<func(s)<<endl;
            outfile2<<y<<endl;

            s += step;
        }
    }

}


int main(){
    double h = M_PI/7;
    double x[9] = {0,1.5*h,2.5*h,3.5*h,4.5*h,6.5*h,7*h};
    interpolation(x,7);
    return 0;
}
