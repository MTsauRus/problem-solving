package ssafy_task._260211;

import java.io.*;
import java.util.*;

public class SW1486_TopShelf_김성령 {
    static int N, ans, goal, num[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            goal = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            num = new int[N];
            for (int i = 0; i < N; i++) {
                num[i] = Integer.parseInt(st.nextToken());
            }

            ans = 200000;
            dfs(0, 0);
            sb.append("#" + t + " " + (ans-goal) + "\n");
        }
        System.out.println(sb);
    }

    static void dfs(int depth, int sum) {
        if (depth == N) {
            if (sum >= goal) {
                ans = Math.min(ans, sum);
            }
            return;
        }

        dfs(depth+1, sum);
        dfs(depth+1, sum+num[depth]);
    }
}
