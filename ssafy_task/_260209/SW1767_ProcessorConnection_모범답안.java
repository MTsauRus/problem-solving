package ssafy_task._260209;

import java.util.*;
import java.io.*;

public class SW1767_ProcessorConnection_모범답안 {
    static int N, max, totalCnt, min; // wallCore: 벽에 붙은 코어. dfs 시 종료 조건에 영향
    static List<int[]> list;
    static int[][] map;
    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int TC = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= TC; tc++) {
            N = Integer.parseInt(br.readLine());
            map = new int[N][N];
            list = new ArrayList<>();
            max = 0;
            min = Integer.MAX_VALUE;
            totalCnt = 0;
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                    if ((i==0 || j==0 || i==N-1 || j==N-1) && map[i][j] == 1) continue;
                    if (map[i][j] == 1) {
                        list.add(new int[] {i, j});

                    }
                }
            }
            totalCnt = list.size(); // 가장자리가 아닌 코어의 개수

            setPower(0, 0, 0);
            System.out.println("#"+tc+" "+min);
        }
    }

    static void setPower(int index, int coreCnt, int lineCnt) {
        
        if (totalCnt-index+coreCnt<max) return; // 남은 코어 수 + 현재 코어 수 다 해도 max보다 작다면 리턴

        if (index == totalCnt) {
            if (max < coreCnt) {
                max = coreCnt;
                min = lineCnt;
            } else if (max == coreCnt) {
                min = Math.min(min, lineCnt);
            }
            return;
        }

        int[] cur = list.get(index);
        int r = cur[0];
        int c = cur[1];
        // 해당 코어의 4방향으로 전선 놓기
        for (int d = 0; d < 4; d++) {
            // 해당 코어를 d방향으로 놓는 것이 가능한지 체크
            if (!isAvailable(r, c, d)) continue;
            // 해당 코어 d방향으로 전선 놓기
            int cnt = setStatus(r, c, d, 2);
            // 다음 코어로 넘어가기
            setPower(index+1, coreCnt+1, lineCnt+cnt);
            // 해당 코어 d방향으로 놓은 전선 지우기
            setStatus(r, c, d, 0);
        }
        // 전선 안놓기
        setPower(index+1, coreCnt, lineCnt);
    }

    private static int setStatus(int r, int c, int d, int s) {
        int nr = r, nc = c, cnt = 0;
        while (true) {
            nr += dr[d];
            nc += dc[d];
            if (nr < 0 || nc >= N || nc < 0 || nc >= N) break;
            map[nr][nc] = s;
            cnt++;
        }
        return cnt;
    }

    private static boolean isAvailable(int r, int c, int d) {
        int nr = r, nc = c;
        while (true) {
            nr += dr[d];
            nc += dc[d];
            if (nr < 0 || nc >= N || nc < 0 || nc >= N) break;
            if (map[nr][nc] != 0) return false;
        }
        return true;
    }
}