package ssafy_task._260406;

import java.io.*;
import java.util.*;

public class SW1952_SwimmingPool_김성령 {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));   
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        
        for (int t = 1; t < T+1; t++) {
            int[] prices = new int[4];
            int[] plan = new int[12];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 4; i++) {
                prices[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 12; i++) {
                plan[i] = Integer.parseInt(st.nextToken());
            }

            int[] dp = new int[13];
            dp[0] = 0;


            for (int i = 1; i <= 12; i++) {
                if (i >= 3) {
                    dp[i] = Math.min(dp[i-3] + prices[2], Math.min(dp[i-1] + prices[1], dp[i-1] + prices[0]*plan[i-1]));
                } else {
                    dp[i] = Math.min(dp[i-1] + prices[1], dp[i-1] + prices[0]*plan[i-1]);
                }
            }

            dp[12] = Math.min(dp[12], prices[3]);
            
            sb.append("#" + t + " " + dp[12] + "\n");

        }

        System.out.println(sb);
    
    }
}
