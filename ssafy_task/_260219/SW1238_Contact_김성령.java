package ssafy_task._260219;

import java.util.*;
import java.io.*;

public class SW1238_Contact_김성령 {
    static List<Integer>[] graph;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        for (int t = 1; t < 11; t++) {
            graph = new ArrayList[101];

            for (int i = 1; i <= 100; i++) {
                graph[i] = new ArrayList<>();
            }

            visited = new boolean[101]; 

            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());
            

            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {

                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());

                graph[s].add(e);
            }

            sb.append("#"+t+" "+bfs(start)+"\n");
        }
        System.out.println(sb);
    }    

    static int bfs(int start) {
        Deque<Integer> dq = new ArrayDeque<>();
        dq.offer(start);
        visited[start] = true;

        int localMax = 0;
        int returnMax = 0;

        while (!dq.isEmpty()) {
            returnMax = localMax;
            localMax = 0;
            int dqSize = dq.size();
            
            while (dqSize-->0) {
                int now = dq.pollFirst();
                for (int next : graph[now]) {
                    if (visited[next]) continue;

                    visited[next] = true;
                    localMax = Math.max(localMax, next);
                    dq.offer(next);
                }
            }
        }

        return returnMax;
    }
}
