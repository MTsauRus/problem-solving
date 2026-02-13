package ssafy_task._260213;

import java.util.*;
import java.io.*;

public class SW6782_SquareRootGame_김성령 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            long n = Long.parseLong(br.readLine());
            long ans = 0;

            while (n > 2) {
                long next = (long) Math.sqrt(n);
                if (next * next == n) { // 제곱근 가능
                    ans += 1;
                    n = next;
                } else {
                    ans += ((next+1) * (next+1)) - n + 1;
                    n = next+1;
                }
            }
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }
}
