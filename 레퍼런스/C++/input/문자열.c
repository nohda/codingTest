/*************************
1.작성자 : 노다설
2. 작성일자 : 21-11-23
3. 작성내용 : 빈칸으로 구성된 문자열을 선언하고, 이 문자열에 들어갈 글자들을 하나씩 추측해서 맞추는 게임이다.
4. 파라미터 : 없음
5. 출력값 : 추측한 문자열
6: 수식 : 
*************************/

#include <stdio.h>
#include <string.h>


int main(void){
    char solution[100] = "meet at midnight";
    char answer[100] = "____ __ ________";
    char ch;
    int i;

    while (1){

        printf("\n문자열을 입력하시오: %s \n", answer);
        printf("글자를 추측하시오: ");

        ch = getch();
        for (i = 0; solution[i] != NULL; i++){
            if (solution[i] == ch) answer[i] = ch;
        }
        if(strcmp(solution,answer) == 0) break;
    }
    return 0;
}