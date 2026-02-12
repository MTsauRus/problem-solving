package ssafy_task._260212;

import java.util.*;
import java.io.*;

public class CodeTree_숫자가더큰인접한곳으로이동 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken())-1;
        int c = Integer.parseInt(st.nextToken())-1;
        
        int[][] board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        sb.append(board[r][c] + " ");
        while (true) {
            boolean isBreak = true;
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (0 <= nr && nr < N && 0 <= nc && nc < N && board[nr][nc] > board[r][c]) {
                    r = nr;
                    c = nc;
                    sb.append(board[nr][nc] + " ");
                    isBreak = false;
                    break;
                }
            }
            if (isBreak) break;
        }
        
        System.out.println(sb);

    }    
}
