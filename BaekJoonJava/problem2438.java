import java.util.Scanner;

public class problem2438 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.println("*".repeat(i+1));
        }
    }
}
