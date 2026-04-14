package ssafy_task._260414이후보충;

import java.io.*;
import java.util.*;

public class CodeTree_day4_빙하 {
    static class Node {
        int r, c;
        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    
    static int R, C, ans;
    static int lastIceCnt = -1;
    static int[][] board;
    static boolean[][] visited, melting;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new int[R][C];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (!end()) {
            visited = new boolean[R][C];
            melting = new boolean[R][C];
            
            // for (int i = 0; i < R; i++) {
            //     for (int j = 0; j < C; j++) {
            //         if (visited[i][j]) continue;
                    
            //         if (board[i][j] == 0) {
            //             visited[i][j] = true;
            //             bfs(new Node(i, j));
            //         }
            //     }
            // }
            bfs(new Node(0, 0));
            
            lastIceCnt = 0;
            ans++;
            melt();
        }


        System.out.println(ans + " " + lastIceCnt);
    }

    static boolean end() {

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] == 1) return false;
            }
        }

        return true;
    }

    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};
    static void bfs(Node start) {
        Deque<Node> dq = new ArrayDeque<>();
        dq.offer(start);

        while (!dq.isEmpty()) {
            Node now = dq.pollFirst();
            int nowCnt = 0;

            // 0 기준, 주변 빙하 탐색. 
            for (int i = 0; i < 4; i++) {
                int nr = dr[i] + now.r;
                int nc = dc[i] + now.c; 

                if (nr < 0 || nc < 0 || nr >= R || nc >= C) break;
                
                if (board[nr][nc] == 1) nowCnt++;
            }

            // nowCnt == 4인 경우: 빙하를 못녹임
            for (int i = 0; i < 4; i++) {
                
                int nr = dr[i] + now.r;
                int nc = dc[i] + now.c; 
                
                if (nr < 0 || nc < 0 || nr >= R || nc >= C || visited[nr][nc]) continue;
                
                visited[nr][nc] = true;
                if (board[nr][nc] == 1 && nowCnt < 4) {
                    melting[nr][nc] = true;
                }   

                else if (board[nr][nc] == 0) {
                    dq.offer(new Node(nr, nc));
                }
            }
        }
    }

    static void melt() {
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] == 1) {
                    lastIceCnt++;
                }
                if (melting[i][j]) {
                    board[i][j] = 0;
                }
            }
        }
    }
}

