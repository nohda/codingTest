/*************************
1.작성자 : 노다설
2. 작성일자 : 21-11-30
3. 작성내용 : 구조체를 선언하여, 구조체 요소들을 각각 더한다.
4. 파라미터 : 없음
5. 출력값 : 구조체 내부 요소의 합
6: 수식 : 
*************************/

#include <stdio.h>

typedef struct point{
    int x;
    int y;
}POINT;

POINT translate(POINT p,POINT delta);

int main(void){
    POINT p = {2,3};
    POINT delta = {10,10};
    POINT result;

    result = translate(p,delta);

    printf("(%d %d)+(%d %d)->(%d %d)\n",p.x,p.y,delta.x,delta.y,result.x,result.y);

    return 0;
}

POINT translate(POINT p, POINT delta) {
    POINT new_p;
    new_p.x = p.x + delta.x; new_p.y = p.y + delta.y;
    return new_p; 
}