package ssafy_task._260210;

import java.util.*;
import java.io.*;

public class SW2806_Nqueen_김성령 {
    
    static boolean[] col, slash, bSlash;
    static int ans, N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            ans = 0;
            col = new boolean[N+1]; // one-based
            slash = new boolean[2*N+1]; // last idx: (N, N)
            bSlash = new boolean[2*N]; // (1, 4) ~ (4, 1) -> -3 ~ 3 (+4) -> 1~7
        
            dfs(1);
            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }    


    static void dfs(int r) {
        if (r == N+1) {
            ans++;
            return;
        }

        for (int c = 1; c <= N; c++) {
            if (col[c]||slash[r+c]||bSlash[(r-c)+N]) continue;
            col[c] = slash[r+c] = bSlash[(r-c)+N] = true;
            dfs(r+1);
            col[c] = slash[r+c] = bSlash[(r-c)+N] = false;
        }
    }
}
