#include<iostream>

using namespace std;

int main(){
int x=10;
auto y=x++;
auto z=x++;
auto k=++x;
cout<<y<<z<<k<<x;

return 0;
}