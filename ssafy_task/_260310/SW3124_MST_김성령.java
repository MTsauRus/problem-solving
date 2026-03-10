package ssafy_task._260310;

import java.util.*;
import java.io.*;

public class SW3124_MST_김성령 {
    static int V, E;
    static int[] parent, rank;
    static long ans;
    static Edge[] edges;
    
    static class Edge implements Comparable<Edge>{
        int s, e, w;
        public Edge(int s, int e, int w) {
            this.s = s;
            this.e = e;
            this.w = w;
        }
        @Override
        public int compareTo(Edge o) {
            return Integer.compare(this.w, o.w);
        }

        
    }
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            parent = new int[V+1];
            for (int i = 1; i <= V; i++) {
                parent[i] = i;
            }
            rank = new int[V+1];
            ans = 0;
            edges = new Edge[E];

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                int w = Integer.parseInt(st.nextToken());
                
                edges[i] = new Edge(s, e, w);
            }
            
            Arrays.sort(edges);
            int cnt = 0;
            for (Edge edge : edges) {
                if (union(edge.s, edge.e)) {
                    cnt++;
                    ans += edge.w;
                }
                if (cnt == V-1) break;
            }

            sb.append("#" + t + " " + ans + "\n");

        }
        System.out.println(sb);
    }    

    static int find(int a) {
        if (parent[a] == a) return a;
        return parent[a] = find(parent[a]);
    }

    static boolean union(int a, int b) {
        int ra = find(a);
        int rb = find(b);
        if (ra == rb) return false;

        if (rank[ra] > rank[rb]) {
            parent[rb] = ra;
        } else if (rank[ra] < rank[rb]) {
            parent[ra] = rb;
        } else {
            parent[rb] = ra;
            rank[ra]++;
        }

        return true;
    }
}
