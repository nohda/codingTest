/*************************
1.작성자 : 노다설
2. 작성일자 : 21-11-23
3. 작성내용 : 정해진 문자열을 섞어서 원래의 값을 맞추는 게임
4. 파라미터 : 없음
5. 출력값 : 추측한 문자열
6: 수식 : rand 함수를 사용해 원래 정해진 문자열의 값이 무엇인지 맞춘다.
*************************/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SOL "apple"

int main(void){

    char s[100] = SOL;
    char ans[100];
    int i, len;

    len = strlen(s);

    for(i=0;i<len;i++){
        int pos1 = rand()%len;
        int pos2 = rand()%len;
        char tmp = s[pos1];
        s[pos1] = s[pos2];
        s[pos2] = tmp;
    }
    do{
        printf("%s의 원래단어를 맞춰보세요 : ",s);
        scanf("%s",ans);
    }while(strcmp(ans,SOL) != 0);

    printf("축하합니다.\n");
    return 0;
}