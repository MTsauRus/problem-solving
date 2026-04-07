package ssafy_task._260407;

import java.io.*;
import java.util.*;

public class SW2117_HomeSecurity_김성령 {
    static int N, K;
    static int[][] board;
    static int ans;
    static List<Node> houses;

    static class Node {
        int r, c;
        Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            board = new int[N][N];
            ans = 0;
            houses = new ArrayList<>();
            
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int next = Integer.parseInt(st.nextToken());
                    if (next == 1) {
                        houses.add(new Node(i, j));
                    }
                    board[i][j] = next;
                }
            }

            // 맨하탄 범위 N+1까지 커버
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    for (int k = 1; k <= N+1; k++) {
                        cover(new Node(i, j), k);
                    }
                }
            }        

            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }

    static int calcDist(Node from, Node to) {
        return Math.abs(from.r - to.r) + Math.abs(from.c - to.c);
    }

    static void cover(Node now, int cov) {
        int cost = cov * cov + (cov-1) * (cov-1);
        int homeCnt = 0;

        for (Node next : houses) {
            if (calcDist(now, next) <= cov - 1) {
                homeCnt++;
            }
        }

        if (cost <= homeCnt * K) {
            ans = Math.max(ans, homeCnt);
        }
        return;
    }
}
