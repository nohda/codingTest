#include <stdio.h>
#define ARR 100000
int main(){
	int arr[ARR] = {0,};
	int i, j, temp, n;
	int count = 0;

	scanf("%d",&n);
	
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	for(i=0;i<n;++i){
		for(j=i+1;j<n;j++){
			if(arr[i]>arr[j]){
				temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
				count +=1;
			}
		}
	}
	printf("%d",count);
	return 0;
}