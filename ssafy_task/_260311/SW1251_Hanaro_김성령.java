package ssafy_task._260311;

import java.io.*;
import java.util.*;

public class SW1251_Hanaro_김성령 {
    static int N;
    static int[] xPos, yPos;
    static List<Node>[] graph;
    static boolean[] visited;
    static double[] dist;
    
    static class Node implements Comparable<Node> {
        int v;
        double w;
        public Node(int v, double w) {
            this.v = v;
            this.w = w;
        }

        @Override
        public int compareTo(Node o) {
            return Double.compare(this.w, o.w);
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            xPos = new int[N];
            yPos = new int[N];
            graph = new ArrayList[N];
            for (int i = 0; i < N; i++) {
                graph[i] = new ArrayList<>();
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                xPos[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                yPos[i] = Integer.parseInt(st.nextToken());
            }
            double feeRate = Double.parseDouble(br.readLine());
            
            for (int i = 0; i < N-1; i++) {
                for (int j = i+1; j < N; j++) {
                    double fee = (Math.pow(xPos[i]-xPos[j], 2)+Math.pow(yPos[i]-yPos[j], 2))*feeRate;
                    graph[i].add(new Node(j, fee));
                    graph[j].add(new Node(i, fee));
                }
            }
            
            visited = new boolean[N];
            dist = new double[N];
            Arrays.fill(dist, Double.MAX_VALUE);
            PriorityQueue<Node> pq = new PriorityQueue<>();
            pq.offer(new Node(0, 0.0));
            dist[0] = 0.0;
            double ans = 0.0;
            int nodeCnt = 0;

            while (!pq.isEmpty()) {
                Node now = pq.poll();
                if (visited[now.v]) continue;
                visited[now.v] = true;
                ans += now.w;
                nodeCnt++;
                if (nodeCnt == N) break;                    

                for (Node next : graph[now.v]) {
                    if (!visited[next.v] && dist[next.v] > next.w) {
                        dist[next.v] = next.w;
                        pq.offer(next);
                    }
                }
            }

            sb.append("#" + t + " " + Math.round(ans) + "\n");
        }

        System.out.println(sb);

    }    
}
