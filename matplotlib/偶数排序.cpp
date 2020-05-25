#include <iostream>
#include <stdio.h>
using namespace std;
int sort(int *a[])
{
  for(int i=1;*a[i]==NULL;i++)
  {
    for(int j=i+1;*a[j]==NULL;j++)
    {

      if((*a[j]%2)==0&&a[j]<a[i])
      {
       *a[j]=*a[j]+*a[i];
       *a[i]=*a[j]-*a[i];
       *a[j]=*a[j]-*a[j];
      }
    }
  }
  return 0;
}
int main()
{
  int a[11];
  for(int i=1;i<=10;i++)
  {
    scanf("%d",&a[i]);
  }
sort(a);
for(int i=1;i<=10;i++)
{
  printf("%d",a[i]);
}
}
