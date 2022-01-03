import java.util.*;

public class Pascal {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("정수를 입력 하세요.");

        int n = scan.nextInt();
        int arr[][];
        arr = new int[n+1][];
        int temp[] = {1};
        for (int i = 0; i <= n; i++) {
            arr[i] = new int[i + 1];
            for (int j = 0; j < arr[i].length; j++) {
                if (j < 1) {
                    arr[i][0] = 1;
                }
                else if(j == arr[i].length-1){
                    arr[i][j] = 1;
                } 
                else {
                    if(temp.length == 1){
                        arr[i][j] = 1;
                    }
                    else{
                        arr[i][j] = temp[j - 1] + temp[j];
                    }
                }
            }
            temp = arr[i];
        }
        for(int k=0; k<arr.length; k++){
            for(int p= 0; p< arr[k].length;p++){
                System.out.print(arr[k][p]);
                System.out.print("\t");
            }
            System.out.println();
        }
    }
}