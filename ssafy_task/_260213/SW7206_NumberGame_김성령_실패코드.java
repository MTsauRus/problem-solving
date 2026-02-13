package ssafy_task._260213;

import java.util.*;
import java.io.*;
public class SW7206_NumberGame_김성령_실패코드 {
    
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            String n = br.readLine();
            ans = 0;
            touch(0, n);
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }

    static void touch(int depth, String n) {
        if (n.length() <= 1) {
            ans = Math.max(ans, depth);
            return;
        }

        for (int flag = 1; flag < 1<<n.length()-1; flag++) {
            List<String> subStrings = new ArrayList<>();
            int start = 0; 
            for (int j = 0; j < n.length()-1; j++) {
                if ((flag&(1<<j)) != 0) {
                    subStrings.add(n.substring(start, j+1));
                    start = j+1;
                }
            }
            subStrings.add(n.substring(start));
            
            int mult = 1;
            for (String next : subStrings) {
                mult *= Integer.parseInt(next);
            }
            touch(depth + 1, String.valueOf(mult));
        }
    }
}
