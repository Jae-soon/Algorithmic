class 문자열압축_main {
    public static void main(String[] args) {
        문자열압축 a = new 문자열압축();
        System.out.println(a.solution("aabbaccc"));
    }
}

public class 문자열압축 {
    public int solution(String s) {
        int answer = s.length(); // 8

        for(int i = 1; i <= s.length() / 2; i++) { // 1 2 3 4
            int count = 1;
            String word = s.substring(0, i); // a aa aab aabb
            String diff = "";
            StringBuilder sb = new StringBuilder();

            for(int j = i; j <= s.length(); j += i) { // 1 2 3 4 5 6 7 8 , 2 4 6 8 , 3 6, 4 8
                if(j + i >= s.length()) {
                    diff = s.substring(j, s.length());
                }
                else {
                    diff = s.substring(j, j + i);
                }

                if(diff.equals(word)) {
                    count++;
                } else if(count == 1){
                    sb.append(word);
                    word = diff;
                } else {
                    sb.append(count).append(word);
                    word = diff;
                    count = 1;
                }
            }

            if(i != word.length()) sb.append(word);
            answer = Math.min(answer, sb.toString().length());
        }

        return answer;
    }
}
