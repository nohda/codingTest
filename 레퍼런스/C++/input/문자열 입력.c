#include <stdio.h>
#include <string.h>

#define MAX_STR_SIZE 100

int main(){

    /* 정해진 크기 문자열 입력 받을때 */
    char str_read[MAX_STR_SIZE];
    fgets(str_read, MAX_STR_SIZE, stdin);
    printf("읽어들인 문자열 : %s \n", str_read);

    /* 정해지지 않은 문자열, 엔터치면 그만 입력 받은 */
    char input[10];
    int size = 0;
    while(1){
        fgets(input, 10, stdin);
        size = strlen(input);
        if(input[size-1] == '\n'){
            break;
        }
    }
    printf("%s",input);

}