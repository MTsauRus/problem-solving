package ssafy_task._260219;

import java.util.*;
import java.io.*;

public class SW7733_CheeseThief_김성령 {
    static int N, ans, localPiece;
    static int[][] board;
    static boolean[][] visited;

    static class Point{
        int r, c;
        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            board = new int[N][N];

            for (int i = 0; i < N; i++) {
                board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }

            ans = 1;

            for (int i = 1; i <= 100; i++) {
                localPiece = 0;
                visited = new boolean[N][N];

                for (int r = 0; r < N; r++) {
                    for (int c = 0; c < N; c++) {
                        if (visited[r][c]) continue;
                        if (board[r][c] <= i) continue;
                        bfs(i, r, c);
                    }
                }
                ans = Math.max(ans, localPiece);
            }
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }

    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    static void bfs(int lv, int r, int c) {
        Deque<Point> dq = new ArrayDeque<>();
        visited[r][c] = true;
        dq.offer(new Point(r, c));
        localPiece++;

        while (!dq.isEmpty()) {
            Point now = dq.pollFirst();
            
            for (int i = 0; i < 4; i++) {
                int nr = now.r + dr[i];
                int nc = now.c + dc[i];
                if (nr < 0 || nr >= N || nc < 0 || nc >= N || visited[nr][nc]) continue;
                if (board[nr][nc] <= lv) continue;
                visited[nr][nc] = true;
                dq.offer(new Point(nr, nc));
            }
        }
    }
}