package ssafy_task._260224이후보충;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class CodeTree_day8_조건에맞는조합 {
    static int k, n;
    static int[] selected;
    static StringBuilder sb = new StringBuilder(); 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        
        selected = new int[n];
        

        comb(0, 0, 0);

        System.out.print(sb);
    }

    static void comb(int depth, int bef1, int bef2) {
        if (depth == n) {
            for (int i = 0; i < n; i++) {
                sb.append(selected[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= k; i++) {
            if (i == bef1 && i == bef2) continue;
            selected[depth] = i;
            comb(depth + 1, i, bef1);
        }
    }
    
}
