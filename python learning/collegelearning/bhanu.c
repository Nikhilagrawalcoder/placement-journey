#include <stdio.h>
#include <string.h>
int converter(char p[])
{
    int sum =0;
    int length = strlen(p);
    for(int i=0;i<length;i++)
    {
        sum = sum + p[i]-48;
    }
    return sum;
}
int main(){
    
char s[500];
scanf("%s",s);
int a[200] ={0};
char *p  = strtok(s,"+,-,/,*");
int i=0;
while(p!=NULL)
{
    a[i] = converter(p);
    p = strtok(NULL,"+-/*");
    i++;
}
for(int i=0;i<3;i++)
{
    printf("%d\n",a[i]);
}


return 0;
}