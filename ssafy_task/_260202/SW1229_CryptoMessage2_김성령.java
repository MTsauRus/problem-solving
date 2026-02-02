package ssafy_task._260202;

import java.io.BufferedReader;
import java.io.*;
import java.util.*;

public class SW1229_CryptoMessage2_김성령 {
    static StringTokenizer st;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        for (int t = 1; t < 11; t++) {
            int len = nextInt();
            String[] crypt = br.readLine().split(" ");

            List<String> list = new ArrayList<>();
            for (String str : crypt) {
                list.add(str);
            }

            int query = nextInt();

            for (int i = 0; i < query; i++) {
                String cmd = next();
                if (cmd.equals("I")) {
                    int index = nextInt();
                    int iter = nextInt();
                    for (int j = 0; j < iter; j++) {
                        list.add(index+j, next());
                    }
                } else {
                    int index = nextInt();
                    int iter = nextInt();
                    for (int j = 0; j < iter; j++) {
                    list.remove(index);
                    }
                } 

            }
            
            sb.append("#").append(t).append(" ");
                
            for (int i = 0; i < 10; i++) {
                sb.append(list.get(i)).append(" ");                    
            } sb.append("\n");
        }
        System.out.println(sb);
        
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            String line = br.readLine();
            if (line == null) return null;
            st = new StringTokenizer(line);
        }
        return st.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
}
