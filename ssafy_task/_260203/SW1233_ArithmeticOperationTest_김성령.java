package ssafy_task._260203;

import java.util.*;
import java.io.*;

public class SW1233_ArithmeticOperationTest_김성령 {
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {

        for (int t = 1; t < 11; t++) {
            int N = Integer.parseInt(br.readLine());
            int ans = 1;
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int idx = Integer.parseInt(st.nextToken());
                String str = st.nextToken();
                if (st.hasMoreTokens())
                    continue;
                if (str.equals("-") || str.equals("+") ||str.equals("/") ||str.equals("*")) {
                    ans = 0;
                }
            }
            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }
}