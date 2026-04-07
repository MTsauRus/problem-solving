package ssafy_task._260406;

import java.io.*;
import java.util.*;

public class SW2383_LunchTime_김성령 {
    static int N;
    static int[] zeroDist, oneDist;
    static int[] stairTime;
    static int ans;
    static int personCnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T + 1; t++) {
            N = Integer.parseInt(br.readLine());
            stairTime = new int[2];

            int[] pr = new int[10], pc = new int[10];
            int[] sr = new int[2],  sc = new int[2];
            personCnt = 0;
            int stairCnt = 0;

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int tmp = Integer.parseInt(st.nextToken());
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
            oneDist  = new int[personCnt];

            // dist * 100 + personIdx 인코딩 (sort 후 dist 추출용)
            for (int i = 0; i < personCnt; i++) {
                zeroDist[i] = (Math.abs(pr[i] - sr[0]) + Math.abs(pc[i] - sc[0])) * 100 + i;
                oneDist[i]  = (Math.abs(pr[i] - sr[1]) + Math.abs(pc[i] - sc[1])) * 100 + i;
            }

            ans = Integer.MAX_VALUE;

            for (int mask = 0; mask < (1 << personCnt); mask++) {
                move(mask);
            }

            sb.append('#').append(t).append(' ').append(ans).append('\n');
        }
        System.out.print(sb);
    }

    static void move(int flag) {
        int[] goZero = new int[personCnt];
        int[] goOne  = new int[personCnt];
        int zeroIdx = 0, oneIdx = 0;

        for (int i = 0; i < personCnt; i++) {
            if ((flag & (1 << i)) != 0) goOne[oneIdx++] = oneDist[i];
            else goZero[zeroIdx++] = zeroDist[i];
        }

        Arrays.sort(goZero, 0, zeroIdx);
        Arrays.sort(goOne,  0, oneIdx);

        int zeroTime = simulate(goZero, zeroIdx, stairTime[0]);
        int oneTime  = simulate(goOne, oneIdx, stairTime[1]);

        ans = Math.min(ans, Math.max(zeroTime, oneTime));
    }

    static int simulate(int[] arr, int size, int K) {
        if (size == 0) return 0;

        int[] finish = new int[size];
        for (int i = 0; i < size; i++) {
            int arrival = arr[i] / 100;
            if (i < 3) {
                finish[i] = arrival + 1 + K;
            } else {
                finish[i] = Math.max(arrival + 1, finish[i - 3]) + K;
            }
        }
        return finish[size - 1];
    }
}