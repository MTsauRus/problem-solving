package ssafy_task._260209;

import java.util.*;
import java.io.*;

public class SW1767_ProcessorConnection_김성령 {
    static int N, maxCore, minLine, board[][]; // wallCore: 벽에 붙은 코어. dfs 시 종료 조건에 영향
    static List<Core> coreList;
    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};

    static class Core {
        int r, c;
        public Core(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            maxCore = 0;
            minLine = 145;

            board = new int[N][N];
            coreList = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int next = Integer.parseInt(st.nextToken());

                    if (next == 1) {
                        if (1 <= i && i <= N-2 && 1 <= j && j <= N-2)
                            coreList.add(new Core(i, j)); // 벽에 붙은 코어가 아닐 때에만 판별
                    }
                    board[i][j] = next;
                }
            }

            backTracking(0, 0, 0);

            sb.append('#').append(t).append(" ").append(minLine).append("\n");
        }
        System.out.println(sb);
    }

    static void backTracking(int depth, int localminLine, int localMaxCore) {
        if (depth == coreList.size()) {
            if (localMaxCore < maxCore) return; // 현재 코어 수가 글로벌 코어보다 작다면 볼 필요 없음
            else if (localMaxCore == maxCore) minLine = Math.min(localminLine, minLine); 
            else {
                maxCore = localMaxCore; // 최대 코어 수 업데이트
                minLine = localminLine;
            }
            return;
        }

        for (int i = 0; i < 4; i++) {
            Core now = coreList.get(depth);
            int r = now.r;
            int c = now.c;
            int nr = r + dr[i];
            int nc = c + dc[i];

            int iterLine = 0;
            while (0 <= nr && nr < N && 0 <= nc && nc < N && board[nr][nc] == 0) {
                //board[nr][nc] = 2; // 방문처리
                iterLine++;
                nr += dr[i];
                nc += dc[i];
            }

            if (nr == -1 || nr == N || nc == -1 || nc == N) {
                // 색칠하기
                for (int j = iterLine; j > 0; j--) {
                    nr -= dr[i];
                    nc -= dc[i];
                    board[nr][nc] = 2;
                }
                backTracking(depth+1, localminLine+iterLine, localMaxCore+1);
                for (int j = iterLine; j > 0; j--) {
                    board[nr][nc] = 0;
                    nr += dr[i];
                    nc += dc[i];
                }
            }
        }

        backTracking(depth+1, localminLine, localMaxCore);
        
    }
}
