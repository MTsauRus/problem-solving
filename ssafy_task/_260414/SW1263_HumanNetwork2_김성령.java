package ssafy_task._260414;

import java.io.*;
import java.util.*;

public class SW1263_HumanNetwork2_김성령 {
    static int MAX_VAL = 1000001;
    static int N;
    static int[][] dist;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            dist = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    int tmp = Integer.parseInt(st.nextToken());
                    if (i == j) dist[i][j] = 0;
                    else {
                        if (tmp == 0) dist[i][j] = MAX_VAL;
                        else dist[i][j] = tmp;
                    }
                }
            }
            

            for (int k = 0; k < N; k++) {
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }


            int ans = MAX_VAL;
            for (int i = 0; i < N; i++) {
                int tmp = 0;
                for (int j = 0; j < N; j++) {
                    if (dist[i][j] == MAX_VAL) continue;
                    tmp += dist[i][j];
                }
                ans = Math.min(ans, tmp);
            }

            sb.append("#" + t + " " + ans + "\n");
        }

        System.out.println(sb);
    }    
}
