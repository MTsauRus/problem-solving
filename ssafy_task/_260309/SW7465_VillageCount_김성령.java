package ssafy_task._260309;

import java.io.*;
import java.util.*;

public class SW7465_VillageCount_김성령 {
    static int[] parent, rank;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            parent = new int[N+1];
            for (int i = 1; i <= N; i++) {
                parent[i] = i;
            }
            rank = new int[N+1];


            for (int m = 0; m < M; m++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                
                union(a, b);
            }

            int ans = 0;
            for (int i = 1; i <= N; i++) {
                if (parent[i] == i) ans++;
            }

           sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }    

    static int find(int a) {
        if (parent[a] == a) return a;

        return parent[a] = find(parent[a]);
    }

    static void union(int a, int b) {
        int rA = find(a);
        int rB = find(b);

        if (rA == rB) return;

        if (rank[rA]>rank[rB]) {
            parent[rB] = rA;
        } else if (rank[rA] < rank[rB]) {
            parent[rA] = rB;
        } else {
            parent[rB] = rA;
            rank[rA]++;
        }
        return;
    }
    
}
