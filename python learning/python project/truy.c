#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	  int n,x;
	  scanf("%d %d",&n,&x);
	 int cnt=1;
	 if((x>n+1) || (x<0 && abs(x)>=n)) 
     printf("-1\n");
     else{
         if(x>0){
             for(int i=0;i<n;i++){
                 if(cnt!=x){
                     printf("+");
                     cnt++;
                     continue;
                 }
                 printf("*");
             }
             printf("\n");
         }
         else{
             for(int i=0;i<n;i++){
                 if(cnt!=x){
                     printf("-");
                     cnt--;
                     continue;
                 }
                 printf("*");
             }
             printf("\n");
         }
	  
	}
	return 0;
}

