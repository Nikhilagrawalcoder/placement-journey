#include<iostream>
using namespace std;

int main(){
int x=5;
int *p=&x;


cout<<*p;
x=x+40;
cout<<*p;
*p=*p+10;
cout<<x;
return 0;
}