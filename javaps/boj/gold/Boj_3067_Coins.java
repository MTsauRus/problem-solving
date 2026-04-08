package javaps.boj.gold;

import java.io.*;
import java.util.*;

public class Boj_3067_Coins {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            int N = Integer.parseInt(br.readLine());
            int[] coins = new int[N+1];
            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= N; i++) {
                coins[i] = Integer.parseInt(st.nextToken());
            }

            int goal = Integer.parseInt(br.readLine());

            int[] dp = new int[goal+1];
            dp[0] = 1;

            for (int i = 1; i <= N; i++) {
                for (int w = 1; w <= goal; w++) {
                    if (w-coins[i] >= 0) 
                        dp[w] += dp[w-coins[i]];
                }
            }

            sb.append(dp[goal]).append("\n");
        }

        System.out.println(sb);
    }    
}
