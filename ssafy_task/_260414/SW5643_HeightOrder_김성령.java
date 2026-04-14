package ssafy_task._260414;

import java.io.*;
import java.util.*;

public class SW5643_HeightOrder_김성령 {
    static int V, E;
    static int[][] dist;
    static int INF = 1000001;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
    
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            V = Integer.parseInt(br.readLine());
            E = Integer.parseInt(br.readLine());

            dist = new int[V+1][V+1];
            for (int i = 0; i < V+1; i++) {
                Arrays.fill(dist[i], INF);
            }
            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                dist[a][b] = 1;
            }

            for (int k = 1; k <= V; k++) {
                for (int i = 1; i <= V; i++) {
                    for (int j = 1; j <= V; j++) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }

            int ans = 0;
            for (int i = 1; i <= V; i++) {
                boolean add = true;
                List<Integer> list = new ArrayList<>();
                for (int j = 1; j <= V; j++) {
                    if (i == j) continue;
                    if (dist[i][j] == INF) list.add(j);
                }

                for (int candidate : list) {
                    if (dist[candidate][i] == INF) {
                        add = false;
                        break;
                    }
                }

                if (add) ans++;
            }
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }
}
