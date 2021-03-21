import java.util.Scanner;

public class MM20213090 {
    // static int count = 0;
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("정수를 입력 하세요.");
        int m = scan.nextInt();
        int n = scan.nextInt();
        int r = scan.nextInt();

        //2차원 배열에 학번 저장.
        int arr[][];
        int arr_[][];

        arr=makeArray(n,r);
        arr_=makeArray(m,n);

        // for문 돌면서 행렬 더하기
        int answerArray[][];
        answerArray = new int [m][r];
        int answer =0;
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < m; k++) {
                for (int i = 0; i < n; i++) {
                    answer += arr[i][k] * arr_[j][i];
                }
                answerArray[j][k] = answer;
                answer=0;
            }
        }

        for(int a=0; a< answerArray.length; a++){
            for(int b =0; b< answerArray[a].length; b++){
                System.out.print(answerArray[a][b]);
                System.out.print("\t");
            }
            System.out.println();
        }
    }

    static int[][] makeArray(int row, int column) {
        int arr[][];
        int count = 0;
        
        //행렬에 들어가는 숫자
        int inputNumber[] = {20,21,30,90};
        arr = new int[row][column];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                arr[i][j] = inputNumber[count];
                count++;
                if (count == 4) {
                    count = 0;
                }
            }
        }
        return arr;
    }
}
