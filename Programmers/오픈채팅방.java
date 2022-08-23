import java.util.*;

class 오픈채팅방_main {
    public static void main(String[] args) {
        오픈채팅방 a = new 오픈채팅방();
        String[] arr = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
        for(int i = 0; i < arr.length; i++) {
            System.out.println(a.solution(arr)[i]);
        }
    }
}

public class 오픈채팅방 {
    public String[] solution(String[] record) {
        List<String> chat_log = new ArrayList<>();
        Map<String, String> usr_map = new HashMap<>();

        for(int i = 0; i < record.length; i++) {
            StringTokenizer st = new StringTokenizer(record[i]);
            String entrance = st.nextToken();
            String uid = st.nextToken();
            String name = "";

            if(!entrance.equals("Leave")) {
                name = st.nextToken();
            }

            if (entrance.equals("Enter")) {
                usr_map.put(uid, name);
                chat_log.add(uid + "님이 들어왔습니다.");
            } else if (entrance.equals("Leave")) {
                chat_log.add(uid + "님이 나갔습니다.");
            } else {
                usr_map.put(uid, name);
            }
        }

        String[] answer = new String[chat_log.size()];
        int index = 0;

        for(String chat : chat_log) {
            int uid_index = chat.indexOf("님");
            String uid = chat.substring(0, uid_index);

            String str2 = chat.replace(uid, usr_map.get(uid));

            answer[index++] = str2;

        }

        return answer;
    }
}
