package ssafy_task._260213;

import java.util.*;
import java.io.*;
public class SW7206_NumberGame_김성령 {
    
    static int ans;
    static int[] memo = new int[100000];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            String n = br.readLine();
            
            ans = touch(n);
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }

    static int touch(String n) {
        if (memo[Integer.parseInt(n)] != 0) {
            return memo[Integer.parseInt(n)];
        }

        if (n.length() <= 1) {
            return 0;
        }

        int localMax = 0;
        for (int flag = 1; flag < 1<<n.length()-1; flag++) {

            int start = 0; 
            int mult = 1;
            for (int j = 0; j < n.length()-1; j++) {
                if ((flag&(1<<j)) != 0) {
                    mult *= Integer.parseInt(n.substring(start, j+1));
                    start = j+1;
                }
            }
            mult *= Integer.parseInt(n.substring(start));
            
            localMax = Math.max(localMax, touch(String.valueOf(mult)));
        }
        memo[Integer.parseInt(n)] = localMax+1;
        return memo[Integer.parseInt(n)];
    }
}
