import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem15596 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Test t = new Test();

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        long result = t.sum(arr);

        System.out.println(result);
    }
}

class Test {
    long sum(int[] a) {
        long sum = 0;

        for(int i = 0; i < a.length; i++) {
            sum += a[i];
        }

        return sum;
    }
}