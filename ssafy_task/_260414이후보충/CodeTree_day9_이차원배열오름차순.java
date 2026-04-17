package ssafy_task._260414이후보충;

import java.io.*;
import java.util.*;

public class CodeTree_day9_이차원배열오름차순 {
    static long N, K;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Long.parseLong(br.readLine());
        K = Long.parseLong(br.readLine());

        long s = 1;
        long e = 1000000000;
        long ans = 0;

        while (s+1 < e) {
            long mid = (s + e) / 2;
            System.out.println("now mid: " + mid);
            long cnt = 0;

            for (int i = 1; i <= N; i++) {
                cnt += Math.min(N, mid/i);
            }

            if (cnt == K) {
                ans = mid;
                break;
            }
            else if (cnt < K) {
                s = mid;
            } else {
                e = mid;
            }

        }

        System.out.println(ans);



    }
}
