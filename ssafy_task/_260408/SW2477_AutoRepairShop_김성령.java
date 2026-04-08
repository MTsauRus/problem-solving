package ssafy_task._260408;

import java.io.*;
import java.util.*;

public class SW2477_AutoRepairShop_김성령 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim());

        for (int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N   = Integer.parseInt(st.nextToken()); 
            int M   = Integer.parseInt(st.nextToken()); 
            int K   = Integer.parseInt(st.nextToken()); 
            int A   = Integer.parseInt(st.nextToken()) - 1; 
            int B   = Integer.parseInt(st.nextToken()) - 1; 
            int[] recepTime  = new int[N];
            int[] repairTime = new int[M];
            int[] arrival    = new int[K + 1]; 

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) recepTime[i]  = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) repairTime[i] = Integer.parseInt(st.nextToken());

            int[] tmp = new int[K];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < K; i++) tmp[i] = Integer.parseInt(st.nextToken());
            Arrays.sort(tmp);
            for (int i = 0; i < K; i++) arrival[i + 1] = tmp[i];

            int[] recepFree        = new int[N];
            int[] custRecepBooth   = new int[K + 1]; 
            int[] custRecepFinish  = new int[K + 1]; 

            for (int k = 1; k <= K; k++) {
                int best = 0;
                for (int i = 1; i < N; i++) {
                    if (recepFree[i] < recepFree[best]) best = i;
                }
                int start = Math.max(arrival[k], recepFree[best]);
                custRecepBooth[k]  = best;
                custRecepFinish[k] = start + recepTime[best];
                recepFree[best]    = custRecepFinish[k];
            }

            Integer[] order = new Integer[K];
            for (int i = 0; i < K; i++) order[i] = i + 1;
            Arrays.sort(order, (a, b) -> {
                if (custRecepFinish[a] != custRecepFinish[b])
                    return custRecepFinish[a] - custRecepFinish[b];
                return custRecepBooth[a] - custRecepBooth[b];
            });

            int[] repairFree      = new int[M];
            int[] custRepairBooth = new int[K + 1]; 

            for (int k : order) {
                int best = 0;
                for (int i = 1; i < M; i++) {
                    if (repairFree[i] < repairFree[best]) best = i;
                }
                int start = Math.max(custRecepFinish[k], repairFree[best]);
                custRepairBooth[k] = best;
                repairFree[best]   = start + repairTime[best];
            }

            int ans = 0;
            boolean found = false;
            for (int k = 1; k <= K; k++) {
                if (custRecepBooth[k] == A && custRepairBooth[k] == B) {
                    ans += k;
                    found = true;
                }
            }

            sb.append('#').append(t).append(' ').append(found ? ans : -1).append('\n');
        }

        System.out.print(sb);
    }
}