package ssafy_task._260212;

import java.util.*;
import java.io.*;

public class JUN1074_Z_김성령 {
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());        
        
        int N = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int ans = 0;
        for (int i = N; i >= 1; i--) {
            int thisMult = (int) Math.pow(2, i-1);
            if (R < thisMult) {
                if (C < Math.pow(2, i-1)) { // 1사분면
                    continue;
                } 
                else { // 2사분면
                    ans += thisMult * thisMult;
                    C -= thisMult;
                }
            } else {
                if (C < thisMult) {
                    ans += 2 * thisMult * thisMult;
                    R -= thisMult;
                } else {
                    ans += 3 * thisMult * thisMult;
                    R -= thisMult;
                    C -= thisMult;
                }
            }
        }
        System.out.println(ans);
    }
}
