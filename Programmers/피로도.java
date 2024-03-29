public class 피로도 {
    int answer = -1;
    boolean[] visit;
    int[][] dungeons;

    public int solution(int k, int[][] dungeons) {
        this.dungeons = dungeons;
        visit = new boolean[dungeons.length];
        for(int i = 0; i < dungeons.length; i++) {
            if(k >= dungeons[i][0]) {
                dfs(i, k, 1);
            }
        }

        return answer;
    }

    private void dfs(int cur, int tired, int depth) {
        visit[cur] = true;
        tired -= dungeons[cur][1];
        for(int i = 0; i < dungeons.length; i++) {
            if(!visit[i] && dungeons[i][0] <= tired) {
                dfs(i, tired, depth + 1);
            }
        }
        answer = Math.max(answer, depth);
        visit[cur] = false;
    }
}
