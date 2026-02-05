package ssafy_task._260205;

import java.util.*;
import java.io.*;

public class SW5215_HambergerDiet_김성령 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            
            HashMap<Integer, int[]> foods = new HashMap<>();

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int[] food = new int[2];
                food[0] = Integer.parseInt(st.nextToken());
                food[1] = Integer.parseInt(st.nextToken());
                
                foods.put(i, food);
            }

            int[] dp = new int[W+1];
            for (int i = 0; i < N; i++) {
                int[] food = foods.get(i);
                for (int w = W; w >= food[1]; w--) {
                    dp[w] = Math.max(dp[w], dp[w-food[1]] + food[0]);
                }
            }

            sb.append("#").append(t).append(" ").append(dp[W]).append("\n");
        }
        System.out.println(sb);
    }
}
