import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class problem2562 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> arr = new ArrayList<>();

        for(int i = 0; i < 9; i++) {
            int n = Integer.parseInt(br.readLine());
            arr.add(n);
        }

        int max = Collections.max(arr);
        int index = arr.indexOf(max) + 1;

        System.out.println(max + "\n" + index);
    }
}
