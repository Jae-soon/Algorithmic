import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class 할인행사 {
    public static void main(String[] args) {
        String[] want = new String[]{"banana", "apple", "rice", "pork", "pot"};
        int[] number = new int[]{3, 2, 2, 2, 1};
        String[] discount = new String[]{"chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"};
    }

    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        for (int i = 0; i <= discount.length - 10; i++) {
            String[] salesDay = Arrays.copyOfRange(discount, i, i+10);
            int same_product = 0;

            for(int j = 0; j < want.length; j++) {
                int count = 0;
                for(String sale_product : salesDay) {
                    if(want[j].equals(sale_product)) {
                        count += 1;
                    }
                }
                if(count == number[j]) {
                    same_product += 1;
                }
            }

            if(same_product == 5) {
                answer += 1;
            }
        }

        return answer;
    }
}
