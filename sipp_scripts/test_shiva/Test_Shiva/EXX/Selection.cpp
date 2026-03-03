#include<iostream>
#include<cstdio>
using namespace std;

void swap(int *a,int *b)
{
int temp = *a;
    *a=*b;
    *b=temp;
}

void selectionSort(int arr[],int  n) 
{
int min;
	for(int i=0;i<n;i++)
	{
	 for(int j=1;arr[j]<arr[i];j++)
	 {
           min=j;
	   cout<<"\n val="<<arr[j];
	 }
	cout<<"\n aa ="<<min;
        swap(&arr[min],&arr[i]);
	}
}

void printArray(int arr[],int size)
{
for(int i=0;i<size;i++)
cout<<" "<<arr[i];
}

int main()
{
int arr[]={12,11,13,5,7,6};
int n=sizeof(arr)/sizeof(arr[0]);
selectionSort(arr, n); 
cout << "Sorted array: \n";
printArray(arr, n);  
return 0;  
}
