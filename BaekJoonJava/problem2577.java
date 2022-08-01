import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem2577 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 0 ~ 9까지 숫자 수
        int[] arr = new int[10];
        int result = Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine());
        
        while (result != 0) {
            arr[result % 10]++; // 1의자리 수 숫자
            result /= 10; // 계산된 1의자리 숫자를 제외한 나머지 숫자
        }

        for(int result_arr : arr) {
            System.out.println(result_arr);
        }
    }
}
