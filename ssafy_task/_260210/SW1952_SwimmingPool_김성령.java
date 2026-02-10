package ssafy_task._260210;

import java.util.*;
import java.io.*;

public class SW1952_SwimmingPool_김성령 { 
    static int[] tollArr, monthArr;
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            tollArr = new int[4];
            monthArr = new int[12];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 4; i++) {
                tollArr[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 12; i++) {
                monthArr[i] = Integer.parseInt(st.nextToken());
            }
            ans = tollArr[3]; // 1년 요금이 현재 최저

            dfs(0, 0);

            sb.append('#').append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }

    static void dfs(int depth, int totalFee) {
        if (depth >= 12) {
            ans = Math.min(totalFee, ans);
            return;
        }

        dfs(depth+1, totalFee + monthArr[depth]*tollArr[0]); // 일요금
        dfs(depth+1, totalFee + tollArr[1]); // 월요금
        dfs(depth+3, totalFee + tollArr[2]); // 3달요금
    }
}