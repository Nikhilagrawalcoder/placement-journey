#include<iostream>
using namespace std;
int arrdistinct(int arr[],int n){
    int count=0;
    bool isdistinct=true;
    for(int i=0;i<n;i++){
        isdistinct =true;

        for(int j=i-1;j>=0;j--){
            if(arr[i]==arr[j]){
            isdistinct=false;
            break;
        }
    }
    if(isdistinct==true)
    count++;
    }
return count;
}
int main(){
int n;
cout<<"enter size";
cin>>n;
int arr[n];
for(int i=0;i<n;i++){
    cin>>arr[n];
}
cout<<arrdistinct(arr,n);
return 0;
}