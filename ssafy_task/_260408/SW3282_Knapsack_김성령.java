package ssafy_task._260408;

import java.io.*;
import java.util.*;

public class SW3282_Knapsack_김성령 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int[] weight = new int[N+1];
            int[] value = new int[N+1];
            for (int i = 1; i <= N; i++) {
                st = new StringTokenizer(br.readLine());
                weight[i] = Integer.parseInt(st.nextToken());
                value[i] = Integer.parseInt(st.nextToken());
            }

            int[] dp = new int[W+1];

            for (int i = 1; i <= N; i++) {
                for (int w = W; w-weight[i] >= 0; w--) {
                    dp[w] = Math.max(dp[w], dp[w-weight[i]] + value[i]);
                }
            }

            sb.append("#" + t + " " + dp[W] + "\n");
        }
        System.out.println(sb);
    }
}
