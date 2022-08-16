import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem2675 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int iter = Integer.parseInt(st.nextToken());
            String words = st.nextToken();

            for(String word : words.split("")) {
                System.out.print(word.repeat(iter));
            }
            System.out.println();
        }
    }
}
