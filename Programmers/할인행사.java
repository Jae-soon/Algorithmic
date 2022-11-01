import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class 할인행사 {

    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        Map<String, Integer> wantMap = new HashMap<>();

        for(int i = 0; i < want.length; i++) {
            String s = want[i];
            int count = number[i];

            wantMap.put(s, count);
        }

        Map<String, Integer> discountMap = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            String addItem = discount[i];
            discountMap.put(addItem, discountMap.getOrDefault(addItem, 0) + 1);
        }

        if(isEqual(wantMap, discountMap)) {
            answer++;
        }

        for(int i = 1; i <= discount.length - 10; i++) {
            String deleteItem = discount[i - 1];
            discountMap.put(deleteItem, discountMap.get(deleteItem) - 1);

            String addItem = discount[i - 1 + 10];
            discountMap.put(addItem, discountMap.getOrDefault(addItem, 0) + 1);

            if(isEqual(wantMap, discountMap)) {
                answer++;
            }
        }

//        for (int i = 0; i <= discount.length - 10; i++) {
//            String[] salesDay = Arrays.copyOfRange(discount, i, i+10);
//            int same_product = 0;
//
//            for(int j = 0; j < want.length; j++) {
//                int count = 0;
//                for(String sale_product : salesDay) {
//                    if(want[j].equals(sale_product)) {
//                        count += 1;
//                    }
//                }
//                if(count == number[j]) {
//                    same_product += 1;
//                }
//            }
//it
//            if(same_product == 5) {
//                answer += 1;
//            }
//        }

        return answer;
    }

    public boolean isEqual(Map<String, Integer> wantMap, Map<String, Integer> discountMap) {
        for(String key : wantMap.keySet()) {
            if(!discountMap.containsKey(key) || wantMap.get(key) != discountMap.get(key)) {
                return false;
            }
        }
        return true;
    }
}
