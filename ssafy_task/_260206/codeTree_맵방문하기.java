package ssafy_task._260206;

import java.util.*;
import java.io.*;

public class codeTree_맵방문하기 {
    static int R, C, cnt;
    static char[][] board;
    static int[][] visited; // 시간절약을 위한 int visited

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new char[R][C];
        visited = new int[R][C];

        for (int i = 0; i < R; i++) {
            board[i] = br.readLine().toCharArray();
        }

        int ans = 0;
        cnt = 0;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                ans = Math.max(ans, normalBfs(i, j));
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                int tmpInt = bfs(i, j);
                ans = Math.max(ans, tmpInt);
            }
        }
        System.out.println(ans);
    }

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static char[] magicKeyword = {'U', 'D', 'L', 'R'};
    
    static int normalBfs(int r, int c) {
        Deque<Integer[]> dq = new ArrayDeque<>();
        dq.offer(new Integer[]{r, c});
        int max = 0;
        cnt++;
        while (!dq.isEmpty()) {
            Integer[] now = dq.pollFirst();

            char nextDir = board[now[0]][now[1]]; // 현재 방향 체크
            int dir = 0;

            if (nextDir == 'U') dir = 0;
            else if(nextDir == 'D') dir = 1;
            else if (nextDir == 'L') dir = 2;
            else if (nextDir == 'R') dir = 3;
            
            int nr = now[0] + dr[dir];
            int nc = now[1] + dc[dir];

            if (nr < 0 || nr >= R || nc < 0 || nc >= C || (visited[nr][nc] == cnt)) continue;

            visited[nr][nc] = cnt;
            dq.offer(new Integer[] {nr, nc});
            max++;
        }
        return max;
    }
    

    static int bfs(int r, int c) {
        int max = 0;
        for (int i = 0; i < R+C+1; i++) { // 마법 부릴 행열번호
            int magic = i<R ? i : i-R;
            for (int j = 0; j < 4; j++) { // 0~3 각각 방향
                int localMax = 1;
                cnt++;

                Deque<Integer[]> dq = new ArrayDeque<>();
                dq.offer(new Integer[]{r, c});
                visited[r][c] = cnt;

                while (!dq.isEmpty()) {
                    Integer[] now = dq.pollFirst();
                    int dir = 0;
                    char nextDir = board[now[0]][now[1]]; // 현재 방향 체크

                    if (i < R && now[0] == magic) {
                        nextDir = magicKeyword[j];
                    } else if (i >= R && now[1] == magic) {
                        nextDir = magicKeyword[j];
                    }

                    if (nextDir == 'U') dir = 0;
                    else if(nextDir == 'D') dir = 1;
                    else if (nextDir == 'L') dir = 2;
                    else if (nextDir == 'R') dir = 3;
                    
                    int nr = now[0] + dr[dir];
                    int nc = now[1] + dc[dir];

                    if (nr < 0 || nr >= R || nc < 0 || nc >= C || (visited[nr][nc] == cnt)) continue;

                    visited[nr][nc] = cnt;
                    dq.offer(new Integer[] {nr, nc});
                    localMax++;
                    }
                    max = Math.max(max, localMax);
                }
            }
            

        return max;
    }
}
