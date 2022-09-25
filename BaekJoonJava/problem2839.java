import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem2839 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int sum = 0;

        if(n % 5 == 0) {
            for(int i = 0; i < n / 5; i++) {
                sum += 1;
            }
            System.out.println(sum);
        } else {
//            if((n % 5) % 3 == 0) {
            if(n % 5 == 1) {
                for(int i = 0; i < (n / 5) - 1; i++) {
                    sum += 1;
                }

                for(int i = 0; i < ((n % 5) / 3) + 2; i++) {
                    sum += 1;
                }
                System.out.println(sum);
            } else if(n % 5 == 4) {
                for(int i = 0; i < (n / 5) - 2; i++) {
                    sum += 1;
                }

                for(int i = 0; i < (n % 5) / 3 + 3; i++) {
                    sum += 1;
                }
                System.out.println(sum);

            } else if(n % 3 == 0) {
				for(int i = 0; i < n / 3; i++) {
                    sum += 1;
                }
				System.out.println(sum);
			} else {
                System.out.println(-1);
            }
        }
    }
}