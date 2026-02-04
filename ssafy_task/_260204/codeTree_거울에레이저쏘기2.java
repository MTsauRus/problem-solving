package ssafy_task._260204;

import java.util.*;
import java.io.*;

public class codeTree_거울에레이저쏘기2 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int N = nextInt();
        char[][] grid = new char[N][N]; // padding
        for (int i = 0; i < N; i++) {
            String s = next();
            for (int j = 0; j < N; j++) {
                grid[i][j] = s.charAt(j);
            }
        }
        int start = nextInt()-1;
        int nr = 0;
        int nc = 0;
        int direction = 0; // 상 -> 우 -> 하 -> 좌
        if (start / N == 0) {
            nc = start%N;
            nr = 0;
            direction = 2;
        } else if (start / N == 1) {
            nc = N-1;
            nr = start%N;
            direction = 3;
        } else if (start / N == 2) {
            nc = N-(start%N)-1;
            nr = N-1;
            direction = 0;
        } else {
            nc = 0;
            nr = N-(start%N)-1;
            direction = 1;
        }

        int[][] DLUR = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}}; // / 모양
        int[][] ULDR = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}}; // \ 모양

        int ans = 0;
        while (0 <= nr && nr < N && 0 <= nc && nc < N) {
            if (grid[nr][nc] == '/') {
                nr += DLUR[direction][0];
                nc += DLUR[direction][1];
                direction^=1;
            } else {
                nr += ULDR[direction][0];
                nc += ULDR[direction][1];
                direction^=3;
            }
            ans++;
        }
        System.out.println(ans);
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            String line = br.readLine();
            if (line == null) return null;
            st = new StringTokenizer(line);
        } return st.nextToken();
    }
    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
}
