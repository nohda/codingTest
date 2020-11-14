#include <iostream>
#include <sstream>

using namespace std;

int solution(int day, int width, int **blocks)
{
    // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
    int first_block = 0;
    int first_block_lo = 0;
    int second_block = 0;
    int second_block_lo = 0;
    int temp_block = 0;
    int max= 0;
    int max_block = 0;

    for (int i = 0; i < day; i++)
    {
        first_block = blocks[i][0];
        for (int j = 0; j <= width; j++)
        {
            if (first_block <= blocks[i][j+1]){ 
                second_block_lo = first_block_lo;
                second_block = first_block;
                first_block=blocks[i][j+1];
                first_block_lo= j;
                if(j+1 != width && blocks[i][j++] >first_block){
                    break;
                }
                else{
                    for(int l= second_block_lo+1; second_block_lo < first_block_lo ; second_block_lo++){
                        max = first_block - second_block;
                        max_block += max - blocks[i][l];

                    }
                }
            }
            else {
                temp_block=blocks[i][j];
            }

        }
    }
    return max_block;
}

struct input_data
{
    int day = 2;
    int width = 6;
    int **blocks[day][width] = {{1,2,3,4,5,6},{1,2,3,4,5,6}};
};

void process_stdin(struct input_data &inputData)
{
    string line;
    istringstream iss;

    getline(cin, line);
    iss.str(line);
    iss >> inputData.day;

    getline(cin, line);
    iss.clear();
    iss.str(line);
    iss >> inputData.width;

    inputData.blocks = new int *[inputData.day];
    for (int i = 0; i < inputData.day; i++)
    {
        getline(cin, line);
        iss.clear();
        iss.str(line);
        inputData.blocks[i] = new int[inputData.width];
        for (int j = 0; j < inputData.width; j++)
        {
            iss >> inputData.blocks[i][j];
        }
    }
}

int main()
{
    struct input_data inputData;
    process_stdin(inputData);

    solution(inputData.day, inputData.width, inputData.blocks);
    return 0;
}