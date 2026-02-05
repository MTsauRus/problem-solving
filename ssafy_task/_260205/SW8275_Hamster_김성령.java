package ssafy_task._260205;

import java.util.*;
import java.io.*;

public class SW8275_Hamster_김성령 {
    static List<Integer[]> query = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            query.clear();
            int N = Integer.parseInt(br.readLine()); // 우리 수
            int R = Integer.parseInt(br.readLine()); // 햄스터 최대 수
            int M = Integer.parseInt(br.readLine()); // 기록 수

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                int l = Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());
                int s = Integer.parseInt(st.nextToken());
                Integer[] q = {l, r, s};
                query.add(q);
            }
        }
    }



    public static perm(int N, int R, int depth, List<Integer> arr) {
        if (depth == R) {
            for (Integer[] q : query) {
                int tmpSum = 0;
                for (int i = q[0]; i <= q[1]; i++) {
                    tmpSum += arr.get(i);
                }
            }
        }
        for (int i = 0; i < N; i++) {
            arr.add(i);
            perm(N, R, depth+1, )
        }
    }
}
