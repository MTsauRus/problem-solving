package ssafy_task._260213;

import java.io.*;
import java.util.*;

public class SW5644_WirelessRecharge_김성령 {

    static class BC {
        int x, y, c, p;

        public BC(int x, int y, int c, int p) {
            this.x = x;
            this.y = y;
            this.c = c;
            this.p = p;
        }
    }

    static int M, A;
    static int[] moveA, moveB;
    static BC[] chargers;
    static int[] dx = {0, 0, 1, 0, -1};
    static int[] dy = {0, -1, 0, 1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            A = Integer.parseInt(st.nextToken());

            moveA = new int[M + 1];
            moveB = new int[M + 1];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                moveA[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                moveB[i] = Integer.parseInt(st.nextToken());
            }

            chargers = new BC[A];
            for (int i = 0; i < A; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int p = Integer.parseInt(st.nextToken());
                chargers[i] = new BC(x, y, c, p);
            }

            sb.append("#").append(t).append(" ").append(solve()).append("\n");
        }
        System.out.println(sb);
    }

    static int solve() {
        int ax = 1, ay = 1;
        int bx = 10, by = 10;
        int totalSum = 0;

        for (int time = 0; time <= M; time++) {
            ArrayList<Integer> validA = getValidChargers(ax, ay);
            ArrayList<Integer> validB = getValidChargers(bx, by);

            if (validA.isEmpty()) validA.add(-1);
            if (validB.isEmpty()) validB.add(-1);

            int maxScore = 0;

            for (int idxA : validA) {
                for (int idxB : validB) {
                    int score = 0;
                    int pA = (idxA == -1) ? 0 : chargers[idxA].p;
                    int pB = (idxB == -1) ? 0 : chargers[idxB].p;

                    if (idxA != -1 && idxA == idxB) {
                        score = pA;
                    } else {
                        score = pA + pB;
                    }
                    maxScore = Math.max(maxScore, score);
                }
            }

            totalSum += maxScore;

            if (time < M) {
                ax += dx[moveA[time]];
                ay += dy[moveA[time]];
                bx += dx[moveB[time]];
                by += dy[moveB[time]];
            }
        }
        return totalSum;
    }

    static ArrayList<Integer> getValidChargers(int x, int y) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < A; i++) {
            int dist = Math.abs(chargers[i].x - x) + Math.abs(chargers[i].y - y);
            if (dist <= chargers[i].c) {
                list.add(i);
            }
        }
        return list;
    }
}