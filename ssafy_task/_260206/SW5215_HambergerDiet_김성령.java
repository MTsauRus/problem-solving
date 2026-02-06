package ssafy_task._260206;

import java.util.*;
import java.io.*;

// 부분집합 풀이
public class SW5215_HambergerDiet_김성령 {
    static boolean[] visited;
    static int N, L;
    static List<Integer[]> foodList = new ArrayList<>();
    static int ans;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            foodList.clear();
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());
            ans = 0;
            visited = new boolean[N];
            for (int n = 0; n < N; n++) {
                st = new StringTokenizer(br.readLine());
                int value = Integer.parseInt(st.nextToken());
                int weight = Integer.parseInt(st.nextToken());
                foodList.add(new Integer[] {value, weight});
            }

            makeSubSet(0);
            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }

    static void makeSubSet(int depth) {
        if (depth == N) {   
            int localValue = 0;
            int localWeight = 0;

            for (int i = 0; i < N; i++) {
                if (visited[i]) {
                    Integer[] nowFood = foodList.get(i);
                    localValue+=nowFood[0];
                    localWeight+=nowFood[1];
                }
            }
            if (localWeight <= L) {
                ans = Math.max(ans, localValue);
            }
            return;
        }

        visited[depth] = true;
        makeSubSet(depth+1);
        visited[depth] = false;
        makeSubSet(depth+1);
    }
}
