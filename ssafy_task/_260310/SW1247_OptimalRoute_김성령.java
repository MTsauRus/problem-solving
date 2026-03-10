package ssafy_task._260310;

import java.io.*;
import java.util.*;

public class SW1247_OptimalRoute_김성령 {
    static int N, ans;
    static Node comp, home;
    static Node[] nodes;
    static boolean[] visited;

    static class Node {
        int x, y;
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            comp = new Node(
                Integer.parseInt(st.nextToken()), 
                Integer.parseInt(st.nextToken()));
            home = new Node(
                Integer.parseInt(st.nextToken()), 
                Integer.parseInt(st.nextToken()));

            nodes = new Node[N+2];
            visited = new boolean[N+1];

            nodes[0] = comp;
            nodes[N+1] = home;
            ans = Integer.MAX_VALUE;

            for (int i = 1; i <= N; i++) {
                nodes[i] = new Node(
                    Integer.parseInt(st.nextToken()), 
                    Integer.parseInt(st.nextToken()));
            }

            perm(0, 0, nodes[0]);

            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }

    static void perm(int depth, int nowDist, Node bef) {
        if (nowDist > ans) return; // 더 볼 필요가 없음
        if (depth == N) {
            nowDist += getDist(bef, nodes[N+1]);
            ans = Math.min(ans, nowDist);
            return;
        }
    
        for (int i = 1; i <= N; i++) {
            if (visited[i]) continue;
            visited[i] = true;

            int dist = getDist(nodes[i], bef);
            perm(depth+1, nowDist+dist, nodes[i]);

            visited[i] = false;
        }
    }

    static int getDist(Node a, Node b) {
        return (Math.abs(a.x-b.x) + Math.abs(a.y-b.y));
    }
}
