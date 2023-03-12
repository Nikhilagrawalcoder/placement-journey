#include<iostream>
using namespace std;
void fun(int x , int y,int z){
    cout<<x<<" "<<y<<" "<<z;
}
int main(){
int i=2;
fun(++i,++i,++i);
return 0;
}