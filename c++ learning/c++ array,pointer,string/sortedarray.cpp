#include<iostream>
using namespace std;

int main(){
int n;
cout<<"enter size";
cin>>n;
int arr[n];
for(int i=0;i<n;i++){
    cin>>arr[i];
}
int f=0;
for(int i=0;i<n;i++)
{
    if(arr[i]>arr[i+1])
    f=1;
}
if(f)
cout<<"NO";
else
cout<<"Yes";

return 0;
}