package ssafy_task._260202;

import java.util.*;
import java.io.*;

public class SW2001_FlyRemoval_김성령 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder(); 

    public static void main(String[] args) throws IOException {

        int T = nextInt();

        for (int t = 1; t < T+1; t++) {
            int N = nextInt();
            int size = nextInt();
            int[][] map = new int[N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    map[i][j] = nextInt();
                }
            }
            int max = 0;

            for (int i = 0; i < N-size+1; i++) {
                for (int j = 0; j < N-size+1; j++) {
                    int tmpSum = 0;
                    for (int x = i; x < i+size; x++) {
                        for (int y = j; y < j+size; y++) {
                            tmpSum+=map[x][y];
                        }
                    }

                    max = Math.max(max, tmpSum);
                }
            }
            sb.append("#").append(t).append(" ");
            sb.append(max);
            sb.append("\n");
        }
        System.out.println(sb);
    }


    public static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            String line = br.readLine();
            if (line == null) return null;
            st = new StringTokenizer(line);
        }
        return st.nextToken();
    }
    public static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
}
