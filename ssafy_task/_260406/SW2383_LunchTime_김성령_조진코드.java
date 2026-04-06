package ssafy_task._260406;

import java.io.*;
import java.util.*;

public class SW2383_LunchTime_김성령_조진코드 {
    static int N;
    static int board[][];
    static int[] zeroDist, oneDist;
    static int[] stairTime;
    static int ans;
    static int personCnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            board = new int[N][N];
            stairTime = new int[2];
            // 가지치기 -> 현재 최고 시간을 넘어가면 return

            int[] pr = new int[10];
            int[] pc = new int[10];
            int[] sr = new int[2];
            int[] sc = new int[2];
            personCnt = 0;
            int stairCnt = 0;

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int tmp = Integer.parseInt(st.nextToken());

                    board[i][j] = tmp;
                    if (tmp == 1) {
                        pr[personCnt] = i;
                        pc[personCnt++] = j;
                    } else if (tmp >= 2) {
                        stairTime[stairCnt] = tmp;
                        sr[stairCnt] = i;
                        sc[stairCnt++] = j;
                    }
                }
            }

            zeroDist = new int[personCnt];
            oneDist = new int[personCnt];
            
            // 거리: 4자리 수. abcd, ab: 해당 계단까지의 이동거리. d: 사람번호
            for (int i = 0; i < personCnt; i++) {
                zeroDist[i] = (Math.abs(pr[i]-sr[0]) + Math.abs(pc[i]-sc[0])) * 100 + i;
                oneDist[i] = (Math.abs(pr[i]-sr[1]) + Math.abs(pc[i]-sc[1])) * 100 + i;
            }
            ans = Integer.MAX_VALUE;
            dfs();

            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }

    static void dfs() {

        for (int i = 0; i < 2<<10; i++) {
            move(i);
        }

    }

    static void move(int flag) {
        int oneCnt = 0;
        
        int[] goZero = new int[10];
        int[] goOne = new int[10];
        int zeroTime = 0;
        int oneTime = 0;
        int zeroIdx = 0; int oneIdx = 0;

        for (int i = 0; i < personCnt; i++) {
            if ((flag & (1<<i)) == 1) {
                oneCnt++;
                goOne[oneIdx++] = oneDist[i];
            }  else {
                goZero[zeroIdx++] = zeroDist[i];
            }
        }

        Arrays.sort(goZero);
        Arrays.sort(goOne);

        int[] dpZero = new int[zeroIdx]; // dp는 delayTime
        if (zeroIdx < 3) {
            if (zeroIdx != 0) zeroTime = goZero[zeroIdx-1]/100 + 1 + stairTime[0];
        } else {
            dpZero[0] = 1; dpZero[1] = 1; dpZero[2] = 1;
            for (int i = 3; i < zeroIdx; i++) {
                dpZero[i] = dpZero[i-3] + stairTime[0] - goZero[zeroIdx-1]/100;
                if (dpZero[i] <= 0) dpZero[i] = 1;
            }
        }

        if (zeroIdx != 0) zeroTime = dpZero[zeroIdx-1] + goZero[zeroIdx-1]/100;

        int[] dpOne = new int[oneIdx]; // dp는 delayTime
        if (oneIdx < 3) {
            if (oneIdx != 0) oneTime = goOne[oneIdx-1]/100 + 1 + stairTime[1];
        } else {
            dpOne[0] = 1; dpOne[1] = 1; dpOne[2] = 1;
            for (int i = 3; i < oneIdx; i++) {
                dpOne[i] = dpOne[i-3] + stairTime[1] - goOne[oneIdx-1]/100;
                if (dpOne[i] <= 0) dpOne[i] = 1;
            }
        }

        if (oneIdx != 0) oneTime = dpOne[oneIdx-1] + goOne[oneIdx-1]/100;
        
        ans = Math.min(Math.max(zeroTime, oneTime), ans);
    }
}
