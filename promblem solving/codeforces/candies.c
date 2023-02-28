#include <stdio.h>

int main(){
int t;
scanf("%d",&t);
while(t--){
    long long  n;
    scanf("%lld\n",&n);
    long long a,b;
    long long c=0;
    for(long long  i=1;i<n;i++){
  a=i;
  
  b=n-i;
  if(a>0&& b>0 && a+b==n && a>b){
    c=c+1;
  }
    }
  if(c>0)
  printf("%lld\n",c);
  else
  printf("0\n");
    
}
return 0;
}