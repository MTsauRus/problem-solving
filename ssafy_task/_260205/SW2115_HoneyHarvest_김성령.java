package ssafy_task._260205;

import java.util.*;
import java.io.*;

public class SW2115_HoneyHarvest_김성령 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int ans, N, M, limit;
    static List<Result> ansList = new ArrayList<>();

    static class Result {
        int r, c1, c2, res;

        public Result(int r, int c1, int c2, int res) {
            this.r = r;
            this.c1 = c1;
            this.c2 = c2;
            this.res = res;
        }
    }

    static int calcProfit(int[] honeyPot, int idx, int sum, int profit) {
        if (sum > limit) return 0;
        if (idx == M) return profit;

        int pick = calcProfit(honeyPot, idx+1, sum + honeyPot[idx], profit + honeyPot[idx] * honeyPot[idx]);
        int pass = calcProfit(honeyPot, idx+1, sum, profit);

        return Math.max(pick, pass);
    }

    public static void main(String[] args) throws IOException{
        int T = nextInt();  

        for (int t = 1; t < T+1; t++) {
            ansList.clear();
            N = nextInt();
            M = nextInt();
            limit = nextInt();
            ans = 0;

            int[][] board = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    board[i][j] = nextInt();
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j <= N-M; j++) {
                    //PriorityQueue<Integer> tmpPq = new PriorityQueue<>(Collections.reverseOrder());
                    int[] honeyPot = new int[M];
                    
                    for (int k = 0; k < M; k++) {
                        honeyPot[k] = board[i][j+k];
                    }
                    int tmpMultSum = calcProfit(honeyPot, 0, 0, 0);
                    
                    // 그리디식 접근 오답 -> 제곱수의 합은 그리디로 못구함
                    // while (tmpSum < limit && !tmpPq.isEmpty()) {
                    //     int nextNum = tmpPq.poll();
                    //     tmpSum += nextNum;
                    //     tmpMultSum += nextNum*nextNum;
                    // }
                    ansList.add(new Result(i, j, j+M-1, tmpMultSum));
                }
            }

            for (int i = 0; i < ansList.size()-1; i++) {
                for (int j = i+1; j < ansList.size(); j++) {
                    Result r1 = ansList.get(i);
                    Result r2 = ansList.get(j);

                    if (r1.r == r2.r && !(r1.c2 < r2.c1 || r1.c1 > r2.c2)) // 겹치는 경우
                        continue;
                    
                    ans = Math.max(ans, r1.res + r2.res);
                }
            }

            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            String line = br.readLine();
            if (line == null) return line;
            st = new StringTokenizer(line);
        } return st.nextToken();
    }
    
    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
}
