package javaps.boj.gold;

/*
    knapsack 응용 문제
    2차원 냅색 먼저 떠올리고 -> 1차원으로 바꾸는 생각
    1차원 버전은 Boj_3067에 풀이함
    금액 == weight, 코인종류 == 보석종류
    values == 경우의 수
    
    현재 i번째 코인으로 대체할 수 있는 경우
    dp[i][j] = (i번째 동전을 사용하지 않고 무게 j를 만들 수 있는 경우) 
             + (i번째 동전을 사용하는 경우 == 
                무게 j-cost[i]의 경우의 수에 cost[i]를 얹어주는 것과 동일)
*/


import java.io.*;
import java.util.*;

public class Boj_9084_동전 {
    public static void main(String[] args) throws IOException {
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
            
            int[][] dp = new int[N+1][goal+1];
            for (int i = 0; i <= N; i++) {
                dp[i][0] = 1;
            }

            for (int i = 1; i <= N; i++) { // i번째 동전
                for (int j = 1; j <= goal; j++) { // 현재 금액 j까지 채우기
                    if (j-coins[i] >= 0) {
                        dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j];
                    } else {
                        dp[i][j] = dp[i-1][j];
                    }
                }
            }
            sb.append(dp[N][goal]).append("\n");
        }
        System.out.println(sb);
    }
}