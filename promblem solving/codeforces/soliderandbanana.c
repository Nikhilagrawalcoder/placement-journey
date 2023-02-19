#include <stdio.h>

int main(){
int k,n,w;
scanf("%d %d %d",&k,&n,&w);
int amount=0;
for(int i=1;i<=w;i++){
    amount=amount+i*k;
}
if(n<amount){
    printf("%d",amount-n);

}
else{
    printf("0");
}
return 0;
}