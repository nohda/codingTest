/*************************
1.작성자 : 노다설
2. 작성일자 : 21-11-30
3. 작성내용 : 구조체를 선언하여, 다른 방법으로 구조체를 출력한다.
4. 파라미터 : 없음
5. 출력값 : 구조체 내부 요소 값
6: 수식 : 
*************************/

#include <stdio.h>
struct student
{
    int number;
    char name[20];
    double grade;
};

int main(void){
    struct student s = {20213090,"노다설",4.5};
    struct student *p;

    p = &s;
    printf("학번=%d 이름=%s 학점=%f\n",s.number,s.name,s.grade);
    printf("학번=%d 이름=%s 학점=%f\n",(*p).number,(*p).name,(*p).grade);
    printf("학번=%d 이름=%s 학점=%f\n",p->number,p->name,p->grade);
    return 0;
}