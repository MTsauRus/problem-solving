package ssafy_task._260309;

import java.io.*;
import java.util.*;

public class SW1868_MineGame_김성령 {

    static char[][] board;
    static boolean[][] visited;
    static int[][] starNums;
    
    static int[] dr = {-1, -1, -1, 0, 1, 1, 1, 0};
    static int[] dc = {-1, 0, 1, 1, 1, 0, -1, -1};

    static class Node {
        int r, c;
        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            int N = Integer.parseInt(br.readLine());
            board = new char[N][N];
            visited = new boolean[N][N];
            starNums = new int[N][N];

            for (int i = 0; i < N; i++) {
                board[i] = br.readLine().toCharArray();
            }


            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (board[i][j] == '*') {
                        visited[i][j] = true;
                        starNums[i][j] = -1;
                    } else {
                        int cnt = 0;
                        for (int k = 0; k < 8; k++) {
                            int nr = i + dr[k];
                            int nc = j + dc[k];

                            if (nr < 0|| nc < 0|| nr >= N || nc >= N) continue;
                            if (board[nr][nc] == '*') cnt++;
                        }
                        starNums[i][j] = cnt;
                    }
                }
            }

            int ans = 0;

            
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visited[i][j]) continue;
                    if (starNums[i][j] == 0) {
                        ans++;
                        Deque<Node> dq = new ArrayDeque<>();
                        dq.offer(new Node(i, j));
                        visited[i][j] = true;

                        while (!dq.isEmpty()) {
                            Node now = dq.pollFirst();

                            for (int k = 0; k < 8; k++) {
                                int nr = now.r + dr[k];
                                int nc = now.c + dc[k];

                                if (nr < 0 || nc < 0 || nr >= N || nc >= N || visited[nr][nc]) continue;
                                
                                visited[nr][nc] = true;
                                if (starNums[nr][nc] == 0) {
                                    dq.offer(new Node(nr, nc));
                                }
                            }
                        }
                    }
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visited[i][j]) continue;
                    ans++;
                }
            }

            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }
}