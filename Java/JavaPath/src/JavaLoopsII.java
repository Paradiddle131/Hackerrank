import java.util.*;
import java.io.*;


public class JavaLoopsII {
    int init = 0;
    public int series(int b, int n){
        return Integer.parseInt((Math.pow(2, 0) + series(2, init)));
    }
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
        int res = 0;
        for (int j = 0; j < n; j++) {
            res += a + Math.pow(2, j)*b;
        }
            System.out.println(res);
        }
        in.close();
    }
}
