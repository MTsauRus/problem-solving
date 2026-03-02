package ssafy_task._260224이후보충;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class CodeTree_day10_등산로공사 {
    
    static int N, K, maxTop;
    static int[][] board;
    static int ans = 0;
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};
    static boolean[][] visited;

    static class Point {
        int r, c;
        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        List<Point> tops = new ArrayList<Point>();
        maxTop = 0;
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int next = Integer.parseInt(st.nextToken());
                board[i][j] = next;
                if (maxTop == next) {
                    tops.add(new Point(i, j));
                } else if (maxTop<next) {
                    maxTop = next;
                    tops.clear();
                    tops.add(new Point(i, j));
                }
            }
        }

        for (Point top : tops) {
            visited[top.r][top.c] = true;
            backtrack(top, 1);
            visited[top.r][top.c] = false;
        }

        System.out.println(ans);

    }

    static void backtrack(Point now, int localMax) {
        int nowHeight = board[now.r][now.c];
        // 사방 탐색 (이동 시 깎고 다시 원상복귀해야 함)
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            int nr = now.r + dr[i];
            int nc = now.c + dc[i];
            if (nr < 0 || nr >= N || nc < 0 || nc >= N || visited[nr][nc]) continue;
            if (board[nr][nc] == maxTop) continue;

            if (board[nr][nc] < nowHeight) {
                visited[nr][nc] = true;
                backtrack(new Point(nr, nc), localMax+1);
                visited[nr][nc] = false;
                cnt++;
            }
            // 나랑 같으면 하나 깎고 이동
            else if (board[nr][nc] == nowHeight) {
                if (K <= 0) continue;

                K--;
                board[nr][nc]--;
                visited[nr][nc] = true;
                backtrack(new Point(nr, nc), localMax+1); 
                K++;
                board[nr][nc]++;
                visited[nr][nc] = false;
                cnt++;
            }
            // 나보다 높으면 깎을 수 있는 만큼 깎고 이동
            else {
                int diff = board[nr][nc] - nowHeight + 1;
                if (diff > K) continue;
                K -= diff;
                board[nr][nc] -= diff;
                visited[nr][nc] = true;
                backtrack(new Point(nr, nc), localMax+1);
                K += diff;
                board[nr][nc] += diff;
                visited[nr][nc] = false;
                cnt++;
            }        
        }
        // 사방탐색 다 했는데 갈 곳이 없다면 맥스값 업데이트 후 리턴
        if (cnt == 0) {
            ans = Math.max(ans, localMax);
        }    
    }
}
