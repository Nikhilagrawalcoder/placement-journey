#include<iostream>
using namespace std;

int main(){
int n;
cout<<"enter size ";
cin>>n;
int a[n];
for(int i=0;i<n;i++){
    cin>>a[i];
}
int s=0;
for(int i=0;i<n;i++){
    s=s+a[i];
}
cout<<"sum of array is "<<s;

return 0;
}