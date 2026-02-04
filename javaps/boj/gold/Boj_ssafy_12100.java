package javaps.boj.gold;

import java.util.*;
import java.io.*;

public class Boj_ssafy_12100 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N;
    static int[][] board;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    
    // d {0: up, 1: down, 2: left, 3: right}
    public int[][] moveUp(int[][] pastBoard, int d) {
        for (int r = 1; r < N; r++) {
            for (int c = 0; c < N; c++) {
                for (int k = r; k > 0; k--) {
                    
                }
            }
        } 
    }
}
