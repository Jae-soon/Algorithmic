import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class problem3003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        List<Integer> chess = new ArrayList<>();

        for(int i = 0; i < 6; i++) {
            chess.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> basic_chess = new ArrayList<>(Arrays.asList(1, 1, 2, 2, 2, 8));

        for(int i = 0; i < 6; i++) {
            int result = basic_chess.get(i) - chess.get(i);
            System.out.print(result + " ");
        }
    }
}
