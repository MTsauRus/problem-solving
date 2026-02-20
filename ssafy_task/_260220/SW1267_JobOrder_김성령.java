package ssafy_task._260220;
import java.io.*;
import java.util.*;

public class SW1267_JobOrder_김성령 {
    static int V, E;
    static ArrayList<Integer>[] graph;
    static int[] indegree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        for (int t = 1; t < 11; t++) {
            st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            graph = new ArrayList[V+1];

            for (int i = 1; i <= V; i++) {
                graph[i] = new ArrayList<>();
            }
            indegree = new int[V+1];
            
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                graph[s].add(e);
                indegree[e]++;
            }
            sb.append("#"+t+" "+topologicalSort()+"\n");
        }
        System.out.println(sb);
    }

    static String topologicalSort() {
        Deque<Integer> dq = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= V; i++) {
            if (indegree[i] == 0) dq.offer(i);
        }

        while (!dq.isEmpty()) {
            int now = dq.pollFirst();
            sb.append(now+" ");
            for (int next : graph[now]) {
                if (--indegree[next]==0) {
                    dq.offer(next);
                }
            }
        }
        return sb.toString();
    }
}