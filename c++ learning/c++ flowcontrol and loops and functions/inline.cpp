#include<iostream>
using namespace std;
int mymax(int x,int y){
    return(x>y)?x:y;
}
int mymax(int x,int y,int z){
    return mymax(mymax(x,y),z);
}
int main(){
int a=10,b=30,c=5;
cout<<mymax(a,b)<<"\n";
cout<<mymax(a,b,c)<<"\n";

return 0;
}