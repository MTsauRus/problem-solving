package ssafy_task._260205;

import java.util.*;
import java.io.*;
public class JUN15649_NandM_김성령 {

    static int N, R;
    static int[] ans;
    static StringBuilder sb = new StringBuilder();
    static boolean[] visited;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        
        ans = new int[R];
        visited = new boolean[N+1];
        perm(0);
        System.out.println(sb);

    }


    static void perm(int depth) {
        if (depth == R) {
            for (int i : ans) {
                sb.append(i).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            ans[depth] = i;
            perm(depth+1);
            visited[i] = false;
        }
    }
}
