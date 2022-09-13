import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem2775 {
    public static int apt[][] = new int[15][15];

    public static void main(String[] args) throws IOException {

        newApt();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for(int i = 0; i < t; i++) {
            int k = Integer.parseInt(br.readLine()); // 층
            int n = Integer.parseInt(br.readLine()); // 호
            System.out.println(apt[k][n]);
        }

    }

    public static void newApt() {
        for (int i = 0; i < 15; i++) {
            apt[i][1] = 1;
            apt[0][i] = i;
        }

        for(int i = 1; i < 15; i++) {
            for(int j = 2; j < 15; j++) {
                apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
            }
        }
    }
}
