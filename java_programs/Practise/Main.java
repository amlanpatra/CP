import java.io.*;
import java.util.*;

// Sumeet sir's video explanation is helpful : using euler path
public class Main {

    public static void main(String[] args) throws Exception {
        Scanner scn = new Scanner(System.in);
        int num = scn.nextInt();
        pzz(num);
    }

    public static void pzz(int n) {
        if (n == 0)
            return;
        System.out.print(n + " ");
        pzz(n - 1);
        System.out.print(n + " ");
        pzz(n - 1);
        System.out.print(n + " ");
    }

}