#include<iostream>
using namespace std;

int main(){
int n;
cin>>n;
if(n%2==0){
    if(n>0){
        cout<<"positive even";
    }
    else if (n==0)
    cout<<"zero ";
    else
    cout<<"negative even";
}
else{
    if(n>0){
        cout<<"positive odd";
    }
    
    else
    cout<<"negative odd";
}
return 0;
}