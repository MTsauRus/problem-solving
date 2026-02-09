package ssafy_task._260209;

import java.util.*;
import java.io.*;

public class SW4008_MakingNumber_김성령 {
    static int localMax, localMin, N;
    static int ans;
    static int[] nums;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            ans = 0;
            localMax = -100000001;
            localMin = 100000002;
            
            N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int[] opsCnt = new int[4];
            for (int i = 0; i < 4; i++) {
                opsCnt[i] = Integer.parseInt(st.nextToken());
            }
            nums = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                nums[i] = Integer.parseInt(st.nextToken());
            }

            operation(0, opsCnt[0], opsCnt[1], opsCnt[2], opsCnt[3], nums[0]);
            sb.append('#').append(t).append(" ").append(localMax-localMin).append("\n");
        }
        System.out.println(sb);
    }

    static void operation(int depth, int plus, int minus, int mult, int div, int res) { 
        if (depth == N-1) {
            localMax = Math.max(localMax, res);
            localMin = Math.min(localMin, res);
            return;
        }
        
        if (plus > 0) operation(depth+1, plus-1, minus, mult, div, res+nums[depth+1]);
        if (minus > 0) operation(depth+1, plus, minus-1, mult, div, res-nums[depth+1]);
        if (mult > 0) operation(depth+1, plus, minus, mult-1, div, res*nums[depth+1]);
        if (div > 0) operation(depth+1, plus, minus, mult, div-1, res/nums[depth+1]);
        
    }
}