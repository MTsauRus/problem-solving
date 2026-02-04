package ssafy_task._260204;

import java.util.*;
import java.io.*;

public class SW1210_Ladder1_김성령 {
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int[] dr = {1, 0, 0};
    static int[] dc = {0, -1, 1}; // 아래, 왼쪽, 오른쪽

    public static void main(String[] args) throws IOException {
        for (int t = 1; t < 11; t++) {
            sb.append("#").append(t).append(" ");
            String foo = br.readLine();
            int[][] ladder = new int[100][100];
            
            for (int i = 0; i < 100; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    ladder[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int i = 0; i < 100; i++) {
                if (ladder[0][i] == 1) {
                    if (move(i, copyMap(ladder))) {
                        sb.append(i).append("\n");
                        break;
                    }
                }
            }
        }    
        System.out.println(sb);
    }
    static boolean isValid(int r, int c) {
        return (0 <= r && r < 100 && 0 <= c && c < 100);
    }


    static class Point {
        int r, c;
        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static int[][] copyMap(int[][] map) {
        int[][] returnMap = new int[100][100];
        for (int i = 0; i < 100; i++) {
            returnMap[i] = map[i].clone();
        }
        return returnMap;
    }

    static boolean move(int c, int[][] ladder) {
        Deque<Point> dq = new ArrayDeque<>();
        dq.offer(new Point(0, c));
        ladder[0][c] = 0;
        while (!dq.isEmpty()) {
            Point now = dq.pollLast();
            boolean isTurn = false; // 이번 회차에서 턴했는지 판단

            for (int i = 1; i < 3; i++) { // 왼쪽, 오른쪽 방향전환
                int nr = now.r + dr[i];
                int nc = now.c + dc[i];
                if (isValid(nr, nc) && ladder[nr][nc] == 1) {
                    ladder[nr][nc] = 0; // 방문처리
                    isTurn = true;
                    dq.offer(new Point(nr, nc));
                }
            }
            if (!isTurn) { // 안돌았으면 아래로 내려감
                int nr = now.r + dr[0];
                int nc = now.c + dc[0];
                if (isValid(nr, nc)) { // 유효성 검사하고
                    if (ladder[nr][nc] == 2) // 정답이면
                        return true;
                    ladder[nr][nc] = 0; // 정답이 아니면 방문처리
                    dq.offer(new Point(nr, nc));
                }
            }
        }
        return false; // 모두 탐색했는데 2를 못만나면 false
    }
}
