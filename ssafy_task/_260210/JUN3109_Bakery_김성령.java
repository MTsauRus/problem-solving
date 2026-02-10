package ssafy_task._260210;

import java.util.*;
import java.io.*;

public class JUN3109_Bakery_김성령 {
    static int R, C;
    static char[][] board;
    static int ans;
    static boolean[][] visited;
    static int[] dr = {-1, 0, 1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new char[R][C];
        visited = new boolean[R][C];
        ans = 0;
        for (int r = 0; r < R; r++) {
            board[r] = br.readLine().toCharArray();
        }
        
        
        for (int r = 0; r < R; r++) {
            dfs(r, 0);
        }
        System.out.println(ans);
    }


    static boolean dfs(int r, int c) {
        if (c == C-1) {
            ans++;
            return true;
        }

        for (int i = 0; i < 3; i++) {
            int nr = r + dr[i];
            int nc = c + 1;

            if (0 <= nr && nr < R && 0 <= nc && nc < C && board[nr][nc] == '.') {
                if (visited[nr][nc]) continue;
                visited[nr][nc] = true;
                if (dfs(nr, nc)) return true; // 이전회차에서 이미 도달한 경우 그냥 트루 찍고 나옴
            }
        }
        return false;
    }
}
