#include<iostream>
using namespace std;

int main(){
int x=10;
int &y=x;
cout<< y<<" ";
x=x+5;
cout<< y<<" ";
y=y+5;
cout<< x<<" ";
return 0;
}