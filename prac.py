#include <iostream>
using namespace std;

int main() 
{
    int n;
    cin>>n;
    int flag;
    int store;
    int x,y,z;
    int arr[100];
    int count;
    for(int i=0;i<n;i++)
    {
        flag=0;
        cin>>x>>y>>z;
        for(int j=0;j<x;j++)
        {
            cin>>arr[j];
        }
        if(z>y)
        cout<<"YES"<<endl;
        else
        {count=0;
        for(int i=0;i<n-1;i++)
        {for(int j=i;j<n;j++)
        {
            if(arr[i]==arr[j])
            count+=1;
        }
        if(count%2==0)
        {store=z+count*arr[i];
        if    
        }
            
        }
    }
    }
    }
	// your code goes here
	return 0;
}
