/*************************
1.작성자 : 노다설
2. 작성일자 : 21-11-23
3. 작성내용 : 3차원 문자 배열을 이용하여 한영사전을 구현한다.
4. 파라미터 : 없음
5. 출력값 : 입력한 영어의 한글
6: 수식 : 1. 영어 단어를 dic에 저장하여 사전을 만든다.
         2. 입력한 영어가 배열에 있다면 한글을 출력한다.
*************************/

#include <stdio.h>
#include <string.h>

#define WORDS 5
int main(void)
{

    int i, index;
    char dic[WORDS][2][30] = {
        {"book", "책"},
        {"boy", "소년"},
        {"computer", "컴퓨터"},
        {"laguage", "언어"},
        {"rain", "비"}};
    char word[30];
    printf("단어를 입력하시오:");
    scanf("%s", word);
    index = 0;
    for (i = 0; i < WORDS; i++){
        if (strcmp(dic[index][0], word) == 0){
            printf("%s: %s\n", word, dic[index][1]);
            return 0;
        }
        index++;
    }
    printf("사전에서 발견되지 않았습니다.\n");
    return 0;
}