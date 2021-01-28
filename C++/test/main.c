#include <stdio.h>

int rec(int n, int *res){
    int result =0;
    static int count = 0;

    if (n<2)
    return result;
    if (n%3==0){
        result=rec(n-1,res) +n;
        count++;
    }
    else
        result=rec(n-1,res);
    *res = result + count;
    return result;
}

int main(){
    int result=0,sum;
    sum=rec(5, &result);
    printf("1) %d,%d\n",sum,result);

    sum = rec(6,&result);
    printf("2) %d, %d\n",sum,result);
}