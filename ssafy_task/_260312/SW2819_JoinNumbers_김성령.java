package ssafy_task._260312;

import java.io.*;
import java.util.*;

public class SW2819_JoinNumbers_김성령 {
    static String[][] board;
    static HashSet<String> hSet;
    static int ans;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());        

        for (int t = 1; t < T+1; t++) {
            board = new String[4][4];
            ans = 0;
            hSet = new HashSet<>();

            for (int i = 0; i < 4; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 4; j++) {
                    board[i][j] = st.nextToken();
                }
            }

            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    backtrack(i, j, 0, new StringBuilder(board[i][j]));
                }
            }

            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }
    
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};
    static void backtrack(int r, int c, int depth, StringBuilder sb) {
        if (depth == 6) {
            if (hSet.add(sb.toString())) {
                ans++;
            }
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr<0||nc<0||nr>=4||nc>=4) continue;
            StringBuilder nextSb = new StringBuilder(sb.toString());
            nextSb.append(board[nr][nc]);
            backtrack(nr, nc, depth+1, nextSb);
        }
    }
}
