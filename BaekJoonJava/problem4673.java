import java.util.ArrayList;
import java.util.List;

public class problem4673 {
    public static void main(String[] args) {
        int n = 1;
        int result = 0;
        List<Integer> arr = new ArrayList<>(); // 1 ~ 10000까지 있는 List
        List<Integer> self_arr = new ArrayList<>(); // 생성자가 있는 수를 담을 List

        for(int i = 1; i <= 10000; i++) {
            arr.add(i);
        }

        while(n < 10000) {
            result = self_number(n);
            self_arr.add(result);
            n++;
        }

        for(int i = 0; i < self_arr.size(); i++) {
            arr.remove(self_arr.get(i));
        }

        for(int i = 0; i < arr.size(); i++) {
            System.out.println(arr.get(i));
        }
    }

    // 생성자가 있는 함수 만들기
    static int self_number(int n) {
        int n_1000 = n / 1000;
        int n_100 = (n/100) % 10;
        int n_10 = (n/10) % 10;
        int n_1 = n % 10;

        int result = n + n_1000 + n_100 + n_10 + n_1;

        return result;
    }
}
