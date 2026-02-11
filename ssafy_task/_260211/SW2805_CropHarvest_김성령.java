package ssafy_task._260211;

import java.util.*;
import java.io.*;

public class SW2805_CropHarvest_김성령 {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            int N = Integer.parseInt(br.readLine());
            char[][] board = new char[N][N];
            for (int i = 0; i < N; i++) {
                board[i] = br.readLine().toCharArray();
            }
            int ans = 0;
            int mid = N/2;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if ((Math.abs(mid - i) + Math.abs(mid - j)) <= mid) {
                        ans += board[i][j]-'0';
                    }
                }
            }

            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }
}
