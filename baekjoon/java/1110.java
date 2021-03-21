import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        int newNumber = n;
        int count = 0;
  
        while(true){
            newNumber = (newNumber%10)*10 + ((newNumber/10) + (newNumber%10))%10;
            count++;

            if(newNumber == n){
                break;
            }
        }  
        System.out.println(count);
        scan.close();
    }
    
}
