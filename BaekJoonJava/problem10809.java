import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem10809 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String n = br.readLine();
        int[] alphabet_arr = new int[26];

        for(int i = 0; i < alphabet_arr.length; i++) {
            alphabet_arr[i] = -1;
        }

        for(int i = 0; i < n.length(); i++) {
            char ch = n.charAt(i);

            if(alphabet_arr[ch - 'a'] == -1) {
                alphabet_arr[ch - 'a'] = i;
            }
        }

        for(int alphabet_index : alphabet_arr) {
            System.out.print(alphabet_index + " ");
        }
    }
}
