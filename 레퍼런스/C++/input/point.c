/*************************
1.작성자 : 노다설
2. 작성일자 : 21-11-30
3. 작성내용 : 점의 좌표를 입력하여 각각 다른 좌표를 한 구조체를 사용하여 출력한다.
4. 파라미터 : 없음
5. 출력값 : 구조체 내부 요소 값
6: 수식 : 
*************************/

#include <stdio.h>
#include <math.h>

typedef struct point
{
    int x;
    int y;
};

int main(void){
    struct point p1, p2;

    double xdiff,ydiff;
    double dist;

    printf("점의 좌표를 입력하시오.(x y) : ");
    scanf("%d %d",&p1.x,&p1.y);

    printf("점의 좌표를 입력하시오.(x y) : ");
    scanf("%d %d",&p2.x,&p2.y);

    xdiff = p1.x-p2.x;
    ydiff = p1.y-p2.y;

    dist = sqrt(xdiff*xdiff+ydiff*ydiff);
    printf("두 점사이의 거리는 %f입니다.\n",dist);

    return 0;
}