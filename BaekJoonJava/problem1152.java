import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem1152 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String n = br.readLine();
        String n_trim = n.trim();
        int count = 0;

        for(String word : n_trim.split(" ")) {
            count++;
        }

        System.out.println(count);
    }
}
 