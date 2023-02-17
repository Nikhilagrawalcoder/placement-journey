#include <stdio.h>

int main(){
    
int a,b;
char c;
printf("Enter Expression:");
scanf("%d %c %d",&a,&c,&b);
switch(c){
    case'+':printf("your ans is : %d",a+b); break;
    case'-':printf("your ans is : %d",a-b); break;
    case'*':printf("your ans is : %d",a*b); break;
    case'/':printf("your ans is : %.2f",(float)a/b); break;
    case'%':printf("your ans is : %d",a%b); break;
    default: printf("your input is wrong");
    

}
return 0;
}