#include<iostream>
using namespace std;
int firstdigit(int j){
    while(j>10)

    j=j/10;

return j;
}

int main(){
int n;
cout<<"enter number";
cin>>n;
cout<<firstdigit(n);







return 0;
}