import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class problem1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Double> score = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            score.add(Double.parseDouble(st.nextToken()));
        }

        double m = Collections.max(score);
        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += ((score.get(i) / m) * 100);
        }

        System.out.println(sum / n);
    }
}
