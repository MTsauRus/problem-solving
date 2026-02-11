package ssafy_task._260211;

import java.util.*;
import java.io.*;

public class JUN2839_SugarDelivery_김성령 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[5001];
        dp[3] = dp[5] = 1;
        dp[1] = dp[2] = dp[4] = 10000; // 불가능
        for (int i = 6; i <= N; i++) {
            dp[i] = Math.min(dp[i-3] + 1, dp[i-5] + 1);
        }

        if (dp[N] >= 10000) System.out.println(-1);
        else System.out.println(dp[N]);
    }
}