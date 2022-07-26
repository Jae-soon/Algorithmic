import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem2525 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int time = Integer.parseInt(br.readLine());


        int a = h * 60 + m + time;
        h = a / 60;
        m = a % 60;

        if(h >= 24) {
            h -= 24;
        }
        System.out.println(h + " " + m);
    }
}
