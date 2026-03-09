package ssafy_task._260309;

import java.io.*;
import java.util.*;

public class SW7465_VillageCount_김성령 {
    static int[] parent, rank;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            for (int m = 0; m < M; m++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                
                union(a, b);
            }

            Set<Integer> hSet = new HashSet<>();
            for (int next : parent) {
                hSet.add(next);
            }
           sb.append("#" + t + " " + hSet.size() + "\n");
        }
        System.out.println(sb);
    }    
    
}
