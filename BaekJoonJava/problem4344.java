import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem4344 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] score_arr;

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int score_num = Integer.parseInt(st.nextToken());
            double sum = 0;
            score_arr = new int[score_num];
            for(int j = 0; j < score_num; j++) {
                int val = Integer.parseInt(st.nextToken());
                sum += val;
                score_arr[j] = val;
            }

            double avg = sum / score_num;
            double count = 0;

            for(int j = 0; j < score_num; j++) {
                if(score_arr[j] > avg) {
                    count++;
                }
            }

            double result = count / score_num;
            System.out.printf("%.3f%%\n", result * 100);
        }
    }
}
