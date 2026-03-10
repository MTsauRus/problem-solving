package ssafy_task._260310;

import java.util.*;
import java.io.*;

public class JUN15686_ChickenDelivery_김성령 {

    static int N, M, ans;
    static int[][] board;
    static List<Node> homes, chicks;
    static int[] selected;

    static class Node {
        int r, c;
        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        homes = new ArrayList<>();
        chicks = new ArrayList<>();
        selected = new int[M];
        
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) homes.add(new Node(i, j));
                else if (board[i][j] == 2) chicks.add(new Node(i, j));
            }
        }
        
        ans = Integer.MAX_VALUE;
        comb(0, 0);

        System.out.println(ans);

    }

    static void comb(int depth, int start) {

        if (depth == M) {
            int tmpSum = 0;
            for (Node nowHome : homes) {
                int tmpMin = 100;
                for (int chickNum : selected) {
                    Node nowChick = chicks.get(chickNum);
                    tmpMin = Math.min(calcDist(nowChick, nowHome), tmpMin);
                }
                tmpSum += tmpMin;
            }

            ans = Math.min(tmpSum, ans);
            return;
        }

        for (int i = start; i < chicks.size(); i++) {
            selected[depth] = i;
            comb(depth+1, i+1);
        }
    }

    static int calcDist(Node a, Node b) {
        return (Math.abs(a.r-b.r) + Math.abs(a.c-b.c));
    }
}