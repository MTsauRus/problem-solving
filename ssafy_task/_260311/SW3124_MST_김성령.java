package ssafy_task._260311;

import java.io.*;
import java.util.*;

// PRIM 풀이법
public class SW3124_MST_김성령 {
    static int V, E;
    static List<Node>[] graph;
    static boolean[] visited;
    static int[] dist; // mst를 구성하지 않는 노드 ~ mst까지의 최단거리

    static class Node implements Comparable<Node> {
        int v, w;
        public Node(int v, int w) {
            this.v = v;
            this.w = w;
        }

        @Override
        public int compareTo(Node o) {
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
            
            graph = new ArrayList[V+1];
            for (int i = 1; i <= V; i++) {
                graph[i] = new ArrayList<Node>();
            }
            visited = new boolean[V+1];
            dist = new int[V+1];
            Arrays.fill(dist, Integer.MAX_VALUE);

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                int w = Integer.parseInt(st.nextToken());
                
                graph[s].add(new Node(e, w));
                graph[e].add(new Node(s, w));
            }

            dist[1] = 0;

            PriorityQueue<Node> pq = new PriorityQueue<>();
            pq.offer(new Node(1, 0));

            long ans = 0;
            int nodeCnt = 0;

            while (!pq.isEmpty()) {
                Node now = pq.poll();
                if (visited[now.v]) continue;
                visited[now.v] = true;
                ans += now.w;
                nodeCnt++;

                if (nodeCnt == V) break;

                for (Node next : graph[now.v]) {
                    if (!visited[next.v] && dist[next.v] > next.w) {
                        dist[next.v] = next.w;
                        pq.offer(new Node(next.v, next.w));
                    }
                }

            }
            sb.append("#" + t + " " + ans + "\n");
        }   
        System.out.println(sb);
    }
}
