#include <stdio.h>
int factorial(int n){
    int l;
    if(n==1 || n==0)
    l= 1;
    else{
        l= n*factorial(n-1);
    }
    return l;
}
int main(){
int k=factorial(5);
printf("%d",k);
return 0;
}