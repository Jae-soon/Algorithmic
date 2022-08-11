import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem25304 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int total_pay = Integer.parseInt(br.readLine());
        int total_object = Integer.parseInt(br.readLine());
        int pay_sum = 0;

        for(int i = 0; i < total_object; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int pay = Integer.parseInt(st.nextToken());
            int object = Integer.parseInt(st.nextToken());

            pay_sum += (pay * object);
        }

        if(pay_sum == total_pay) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
