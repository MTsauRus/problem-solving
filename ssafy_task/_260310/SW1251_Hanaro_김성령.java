package ssafy_task._260310;

import java.io.*;
import java.util.*;


public class SW1251_Hanaro_김성령 {
    static int V;
    static int[] xPos, yPos;
    static int[] parent, rank;
    static List<Edge> edges;
    
    public static class Edge implements Comparable<Edge> {
        int x, y;
        double dist;
        
        public Edge(int x, int y, double dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        @Override
        public int compareTo(Edge o) {
            return Double.compare(this.dist, o.dist);
        }

        @Override
        public String toString() {
            return "[x: " + x + ", y: " + y + ", dist: " + dist + "]"; 
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
    
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            V = Integer.parseInt(br.readLine());
            parent = new int[V+1];
            for (int i = 1; i <= V; i++) {
                parent[i] = i;
            }
            rank = new int[V+1];
            xPos = new int[V];
            yPos = new int[V];


            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < V; i++) {
                xPos[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < V; i++) {
                yPos[i] = Integer.parseInt(st.nextToken());
            }

            double num = Double.parseDouble(br.readLine());
            edges = new ArrayList<>();
            for (int i = 0; i < V-1; i++) {
                for (int j = i; j < V; j++) {
                    double tmpDist = 
                        (Math.pow((xPos[i] - xPos[j]), 2) + 
                        Math.pow((yPos[i] - yPos[j]), 2)) * num;
                    edges.add(new Edge(i, j, tmpDist));
                }
            }

            // System.out.println(edges);
            Collections.sort(edges);

            
            double ans = 0.0;
            int cnt = 0;
            for (Edge edge : edges) {
                if (union(edge.x, edge.y)) {
                    ans += edge.dist;
                    cnt++;
                }
                if (cnt == V-1) break;
            }

            long lans = Math.round(ans);

            sb.append("#" + t + " " + lans + "\n");
        }
        System.out.println(sb);
    }

    static int find(int a) {
        if (parent[a] == a) return a;
        return parent[a] = find(parent[a]);
    }

    static boolean union(int a, int b) {
        int aa = find(a);
        int bb = find(b);
        if (aa == bb) return false;

        if (rank[aa] > rank[bb]) {
            parent[bb] = aa;
        } else if (rank[aa] < rank[bb]) {
            parent[aa] = bb;

        } else {
            parent[bb] =aa;
            rank[aa]++;
        }
        return true;
    }

}
