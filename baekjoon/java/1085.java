import java.util.*;

public class Main {
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int x, y, w, h;
    x = sc.nextInt();
    y = sc.nextInt();
    w = sc.nextInt();
    h = sc.nextInt();

    int hori = Math.min(w - x,x);
    int verti = Math.min(h - y,y);

    System.out.println(Math.min(hori,verti));
  }
}