package ssafy_task._260205;

import java.util.*;
import java.io.*;

public class SW8275_Hamster_김성령 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int N, X, M; // 우리 수, 최대 햄스터, 쿼리 수
    static List<Integer[]> query = new ArrayList<>();
    static int[] bestCage;
    static int maxHam;
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());    

        for (int t = 1; t < T+1; t++) {
            query.clear();
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            X = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            for (int m = 0; m < M; m++) {
                Integer[] q = new Integer[3];
                st = new StringTokenizer(br.readLine());
                q[0] = Integer.parseInt(st.nextToken());
                q[1] = Integer.parseInt(st.nextToken());
                q[2] = Integer.parseInt(st.nextToken());
                query.add(q);
            }

            bestCage = new int[N+1]; // 우리 수 배열, 1-based
            maxHam = -1; // 최대 햄스터 수 초기화
            perm(1, new int[N+1]);
            
            sb.append("#").append(t).append(" ");
            if (maxHam == -1) {
                sb.append(-1).append("\n");
            } else {
                for (int i = 1; i <= N; i++) {
                    sb.append(bestCage[i]).append(" ");
                } sb.append("\n");
            }
        }
        System.out.println(sb);
    }

    // xPIn을 구해야 함. x마리, 중복해서 우리 n개 선택 (n은 1-based)
    static void perm(int depth, int[] currCage) {
        if (depth == N+1) {
            check(currCage);
            return;
        }

        for (int x = 0; x <= X; x++) { // 최소 0마리 ~ 최대 X마리
            currCage[depth] = x; // depth는 1부터 N+1까지
            perm(depth+1, currCage);
        }

    }

    static void check(int[] currCage) {
        int localSum = 0;

        for (Integer[] q : query) { // 이번 회차의 모든 쪽지와 조건 비교
            int hamSum = 0;
            for (int i = 1; i <= N; i++) {
                localSum += currCage[i]; // 햄스터 수 다 더하고
                if (q[0] <= i && i <= q[1]) {
                    hamSum += currCage[i];
                }
            }
            if (q[2] != hamSum) { // 쪽지의 조건과 일치하지 않는다면 버림
                return;
            }
        }
        // 모든 조건 통과 후
        if (maxHam < localSum) { // 햄스터 수가 가장 많으면
            bestCage = currCage.clone(); // 현재 케이지를 저장하고
            maxHam = localSum; // 최대값을 갱신
        }
    }
}
