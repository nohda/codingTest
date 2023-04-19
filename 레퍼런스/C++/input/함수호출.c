/*************************
1.작성자 : 노다설
2. 작성일자 : 21-11-16
3. 작성내용 : swap함수를 이용해서 두 입력값을 바꾼다.
4. 파라미터 : 없음
5. 출력값 : int a, int b
6: 수식 : 25번째 줄에서 포인터 px의 값을 tmp에 저장한다.
         포인터 py의 값을 포인터 px에 저장한다. 
         tmp의 값을 포인터 py에 저장한다.
*************************/

#include <stdio.h>
void swap(int *px, int *py);

int main(void){    

    int a = 100, b = 200;
    printf("swap() 호출 전 a = %d b = %d\n",a,b);

    swap(&a,&b);
    printf("swap() 호출 후 a = %d b = %d\n",a,b);
    return 0;
}
void swap(int *px, int *py){
    int tmp;

    tmp = *px;
    *px = *py;
    *py = tmp;
}