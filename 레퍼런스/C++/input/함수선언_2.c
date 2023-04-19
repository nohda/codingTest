/*************************
1.작성자 : 노다설
2. 작성일자 : 21-11-16
3. 작성내용 : 입력한 배열의 각 요소를 합하여 평균을 출력한다.
4. 파라미터 : 없음
5. 출력값 : 배열의 평균 값
6: 수식 : 26번째 함수 get_array_avg에서 배열의 각 요소의 누적값을 구한 후 평균을 구한다.
         36번째 함수 print_array는 배열의 각 요소를 출력한다.
*************************/

#include <stdio.h>
#define SIZE 5
double get_array_avg(int values[], int n);
void print_array(int values[], int n);

int main(void){    
    int i;
    int data[SIZE] = {10,20,30,40,50};
    double result;

    print_array(data,SIZE);
    result = get_array_avg(data,SIZE);
    printf("배열 원소들의 평균 = %f\n",result);

    return 0;
}
double get_array_avg(int values[], int n){
    
    double sum = 0.0;
    for(int i = 0; i<n; i++){
        sum += values[i];
    }
    return sum/n;
}

void print_array(int values[], int n){
    printf("[ ");
    for(int i = 0;i<n;i++){
        printf("%d ", values[i]);
    }
    printf("]\n");
}
