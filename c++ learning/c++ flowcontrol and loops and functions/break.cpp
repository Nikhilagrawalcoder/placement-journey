#include<iostream>
using namespace std;

int main(){
int n;
cout<<"enter a number"<<"\n";
cin>>n;
for(int i=2;i<=n;i++){
    if(n%i==0){
    cout<<i;
    break;}
}
return 0;
}