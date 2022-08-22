import java.util.LinkedList;
import java.util.Queue;

class SameQueue {
    public static int solution(int[] queue1, int[] queue2) {
        Queue<Long> q1 = new LinkedList<>();
        Queue<Long> q2 = new LinkedList<>();
        int count = 0;
        long q1_sum = 0;
        long q2_sum = 0;

        for(int i = 0; i < queue1.length; i++) {
            q1_sum += queue1[i];
            q1.add((long) queue1[i]);
        }
        for(int i = 0; i < queue2.length; i++) {
            q2_sum += queue2[i];
            q2.add((long) queue2[i]);
        }

        long mean = (q1_sum + q2_sum) / 2;

        while(true) {
            if(count > queue1.length * 3) return -1;

            if(q1_sum > q2_sum) {
                count++;
                q1_sum -= q1.peek();
                q2_sum += q1.peek();
                q2.add(q1.poll());
            } else if(q1_sum < q2_sum) {
                count++;
                q1_sum += q2.peek();
                q2_sum -= q2.peek();
                q1.add(q2.poll());
            } else {
                if (q1_sum == mean) {
                    return count;
                }
                break;
            }
        }

        return count;
    }
}
