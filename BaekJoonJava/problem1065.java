import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class problem1065 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        List<Integer> han = hansu(n);

        System.out.println(han.size());
    }

    static List<Integer> hansu(int n) {
        List<Integer> han = new ArrayList<>();
        int[] arr = new int[3];

        for(int i = 1; i <= n; i++) {
            if(i < 100) {
                han.add(i);
            } else if(i == 1000) {
                break;
            }
            else {
                int han_num = i;
                int k = 0;
                while (han_num > 0) {
                    arr[k] = han_num % 10;
                    han_num /= 10;
                    k++;
                }
                if(arr[0] - arr[1] == arr[1] - arr[2]) {
                    han.add(han_num);
                }
            }
        }
        return han;
    }
}
