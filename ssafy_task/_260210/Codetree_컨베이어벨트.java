package ssafy_task._260210;

import java.util.*;
import java.io.*;

public class Codetree_컨베이어벨트 {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        Deque<Integer> dq = new ArrayDeque<>();

        int N = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int[] num = new int[N*2];
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) 
            dq.offer(Integer.parseInt(st.nextToken()));
        st = new StringTokenizer(br.readLine());
        for (int i = N; i < 2*N; i++) 
            dq.offer(Integer.parseInt(st.nextToken()));

        T = T % (2*N);

        for (int t = 0; t < T; t++) {
            dq.offerFirst(dq.pollLast());
        }
        
        for (int i = 0; i < 2*N; i++) {
            sb.append(dq.pollFirst()).append(" ");
            if (i == N-1) sb.append("\n");
        }
        System.out.println(sb);
    }
}
