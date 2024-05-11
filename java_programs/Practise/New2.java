import java.util.*;

public class New2 {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter name of student");
        String s = scn.nextLine();
        System.out.println("Enter marks");
        int m = scn.nextInt();
        String s1 = (m >= 91) ? "Extraordinary"
                : (m >= 81) ? "Very good" : (m >= 71) ? "good" : (m >= 61) ? "fair" : (m >= 51) ? "moderate" : "fail";
        System.out.println(s1);
    }
}