import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem11720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int sum = 0;
        String num_str = br.readLine();

        if(num_str.length() == n) {
            for(String num : num_str.split("")) {
                sum += Integer.parseInt(num);
            }
        }
        System.out.println(sum);
    }
}
