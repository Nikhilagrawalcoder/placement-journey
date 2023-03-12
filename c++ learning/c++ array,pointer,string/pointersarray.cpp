#include<iostream>
using namespace std;

int main(){
int arr[]={10,20,30};
int *p=arr;
int(*p1)[3]=&arr;
// cout<<sizeof(arr);
// cout<<sizeof(p);
// cout<<*(arr+1);
// cout<<p[2]; 
cout<<*p;
cout<<sizeof(*p1);
return 0;
}