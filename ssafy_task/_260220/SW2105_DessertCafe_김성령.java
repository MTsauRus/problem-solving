package ssafy_task._260220;

import java.io.*;
import java.util.*;
import java.awt.Point;

public class SW2105_DessertCafe_김성령 {
    static int N, board[][], ans;
    static boolean[] visited;
    static int[] dr = {-1, 1, 1, -1};
    static int[] dc = {1, 1, -1, -1};
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            board = new int[N][N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            ans = -1;     
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    visited = new boolean[101];       
                    backtrack(new Point(i, j), new Point(i, j), 0, 0);
                }
            }
            sb.append("#"+t+" "+ans+"\n");
        }   
        System.out.println(sb);
    }    

    static void backtrack(Point first, Point now, int dir, int localMax) {
        if (dir == 4) return;
        if (dir == 3 && now.x == first.x && now.y == first.y) {
            ans = Math.max(ans, localMax);
            return;
        }
        if (now.x < 0 || now.x >= N || now.y < 0 || now.y >= N || visited[board[now.x][now.y]])
            return;

        if (dir == 3 && now.x == first.x) { // x는 같은데 y가 다르다면 마름모를 만들 수 없음
            return;
        }

        visited[board[now.x][now.y]] = true;
        // 현재 진행방향 그대로
        backtrack(first, new Point(now.x+dr[dir], now.y+dc[dir]), dir, localMax+1);
        
        // 방향 전환 (3이면 직진만 해야 함)
        if (dir <= 2)
            backtrack(first, new Point(now.x+dr[dir+1], now.y+dc[dir+1]), dir+1, localMax+1);
        
        // 백트래킹
        visited[board[now.x][now.y]] = false;
    }
}
