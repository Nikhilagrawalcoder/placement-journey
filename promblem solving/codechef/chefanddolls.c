/*#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,c;
	    scanf("%d",&n);
	    int a[n],i,j;
	    for(i=0;i<n;i++)
	    {
	        scanf("%d\n",&a[i]);
	    }
	    for(i=0;i<n;i++)
	    {
	        c=0;
	        for(j=0;j<n;j++)
	        {
	            if(a[i]==a[j])
	                c++;
	        }
	        if(c%2!=0)
	            break;
	    }
	    printf("%d\n",a[i]);
	    
    }
	return 0;
}*/
#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    int n,i;
	    scanf("%d",&n);
	    int a[n],b[100000]={0};
	    for(i=0;i<n;i++)
	    {
	        scanf("%d\n",&a[i]);
	    }
	    int max=a[0];
	    for(i=1;i<n;i++)
	    {
	        if(a[i]>max)
	            max=a[i];
	    }
	    for(i=0;i<n;i++)
	    {
	        b[a[i]]++;
	    }
	    for(i=0;i<=max;i++)
	    {
	        if(b[i]%2!=0)
	           break;
	    }
	    printf("%d\n",i);
	    
     }
	return 0;
}

