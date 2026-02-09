package ssafy_task._260209;

import java.util.*;
import java.io.*;

public class SW1767_ProcessorConnection_김성령 {
    static int N, ans, cores;
    //static int[][] board;
    static List<Core> coreList;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static class Core {
        int r, c;
        Core(int r, int c) {
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
            int[][] board = new int[N][N];
            ans = 145;
            cores = 0;
            coreList = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int tmpNum = Integer.parseInt(st.nextToken());
                    if (tmpNum == 1) {
                        cores++;
                        coreList.add(new Core(i, j));
                    } 
                    board[i][j] = tmpNum;
                }
            }
            solve(0, 0, copyMap(board));

            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }
    static int[][] copyMap(int[][] prev) {
        int[][] resMap = new int[N][N];
        for (int i = 0; i < N; i++) {
            resMap[i] = prev[i].clone();
        }
        return resMap;
    } 

    static void solve(int depth, int len, int[][] localMap) {
        if (depth == cores) {
            ans = Math.min(len, ans);
            return;
        }

        Core core = coreList.get(depth);

        if (core.r == 0 || core.c == 0) {
            solve(depth+1, len, copyMap(localMap));
            return;
        }

        
        for (int dir = 0; dir < 4; dir++) {
            boolean breakFlag = false;
            int r = core.r;
            int c = core.c;
            int cnt = 0;
            int nr = dr[dir] + r;
            int nc = dc[dir] + c;

            int[][] tmpMap = copyMap(localMap);

            while (0 <= nr && nr < N && 0 <= nc && nc < N && tmpMap[nr][nc] == 0) {
                if (tmpMap[nr][nc] == 2) {
                    breakFlag = true;
                    break;
                }
                tmpMap[nr][nc] = 2;
                r = nr;
                c = nc;
                cnt++;
            }
            if (breakFlag == true) continue;
            solve(depth+1, len+cnt, copyMap(tmpMap));
        }
    }
}
