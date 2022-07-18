import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem2588 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        System.out.println(n * (m % 10));
        System.out.println(n * (m % 100 / 10));
        System.out.println(n * (m / 100));
        System.out.println(n * m);
    }
}
