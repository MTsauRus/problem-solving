package ssafy_task._260415;

import java.io.*;
import java.util.*;

public class SW1494_LoveCounselor_김성령 {
    static int[] xpos, ypos;
    static int[] A, B; // A집단, B집단
    static int N;
    static long ans;
    static boolean[] selected;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            xpos = new int[N];
            ypos = new int[N];
            A = new int[N/2];
            B = new int[N/2];
            ans = Long.MAX_VALUE;
            selected = new boolean[N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                xpos[i] = Integer.parseInt(st.nextToken());
                ypos[i] = Integer.parseInt(st.nextToken());
            }

            comb(0, 0);
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }    

    static void comb(int start, int depth) {
        if (depth == N/2) {
            int tmpIdx = 0;
            for (int i = 0; i < N; i++) {
                if (!selected[i]) {
                    B[tmpIdx++] = i;
                }
            }
            //System.out.println(Arrays.toString(A) + " " + Arrays.toString(B));

            long localVec = calculate();
            ans = Math.min(ans, localVec);
            return;
        }

        for (int i = start; i < N; i++) {
            A[depth] = i;
            selected[i] = true;
            comb(i+1, depth+1);
            selected[i] = false;
        }
    }

    static long calculate() {
        long xA = 0;
        long xB = 0;
        long yA = 0;
        long yB = 0;
    
        for (int i = 0; i < N/2; i++) {
            xA += xpos[A[i]];
            xB += xpos[B[i]];
            yA += ypos[A[i]];
            yB += ypos[B[i]];
        }

        return (xA - xB) * (xA - xB) + (yA - yB) * (yA - yB);
    }
}
