import java.io.*;

public class problem1110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int n1 = n / 10;
        int n2 = n % 10;
        int result = n1 + n2;
        int count = 0;

        while(true) {
            n1 = n2 % 10;
            n2 = result % 10;
            result = n1 + n2;
            count += 1;
            String total = n1 + Integer.toString(n2);

            if(n == Integer.parseInt(total)) {
                break;
            }
        }

        System.out.println(count);
    }
}
