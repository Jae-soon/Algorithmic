import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem10250 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int h = Integer.parseInt(st.nextToken()); // 층
            int w = Integer.parseInt(st.nextToken()); // 호
            int n = Integer.parseInt(st.nextToken()); // 손님
            int x = 1; // 층
            int y = 0; // 호

            if(n % h == 0) {
                x = h;
                y = n / h;
            } else {
                x = n % h;
                y = n / h + 1;
            }

            System.out.println((x * 100) + y);
        }
    }
}
