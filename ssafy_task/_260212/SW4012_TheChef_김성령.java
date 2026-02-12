package ssafy_task._260212;

import java.io.*;
import java.util.*;

public class SW4012_TheChef_김성령 {
    static int N, minDiff, ans;
    static int[][] table;
    static int[] selectedFood;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            table = new int[N][N];
            selectedFood = new int[N/2];
            ans = Integer.MAX_VALUE;

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    table[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            // 조합 구하고 점수 계산
            comb(0, 0);
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }    

    static void comb(int depth, int start) {
        if (depth == N/2) {
            calculateDiff();
            return;
        }

        for (int i = start; i < N; i++) {
            selectedFood[depth] = i;
            comb(depth+1, i+1);
        }
    }

    static void calculateDiff() {
        boolean[] selected = new boolean[N];
        for (int i : selectedFood) selected[i] = true;
        int[] notSelectedFood = new int[N/2];
        int idx = 0;
        for (int i = 0; i < N; i++) {
            if (!selected[i]) notSelectedFood[idx++] = i;
        }
        // System.out.println(Arrays.toString(selectedFood));
        // System.out.println(Arrays.toString(notSelectedFood));
        // System.out.println();
        // 점수 계산
        int selectedScore = 0;
        for (int now : selectedFood) {
            for (int i = 0; i < N; i++) {
                if (selected[i]) {
                    selectedScore += table[now][i];
                }
            }
        }
        int notSelectedScore = 0;
        for (int now : notSelectedFood) {
            for (int i = 0; i < N; i++) {
                if (!selected[i])
                    notSelectedScore += table[now][i];
            }
        }
        ans = Math.min(ans, Math.abs(selectedScore - notSelectedScore));
    }

}
