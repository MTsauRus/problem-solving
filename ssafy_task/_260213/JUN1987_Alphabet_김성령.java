package ssafy_task._260213;

import java.util.*;
import java.io.*;

public class JUN1987_Alphabet_김성령 {
    static int R, C;
    static char[][] board;
    static boolean[] visited = new boolean[26];
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
    
        for (int i = 0; i < R; i++) {
            board[i] = br.readLine().toCharArray();
        }


    }   
    
    static void backtrack(int r, int c) {
        
    }
}
