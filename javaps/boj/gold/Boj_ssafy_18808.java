package javaps.boj.gold;

import java.util.*;
import java.io.*;

// 260203
// ssafy 스터디 문제
// 스티커 붙이기 (G3)
// 시뮬레이션
public class Boj_ssafy_18808 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int R, C, K;

    static int[][] copyMap(int[][] prev, int R, int C) {
        int[][] copiedMap = new int[R][C];
        for (int i = 0; i < R; i++) {
            copiedMap[i] = prev[i].clone();
        } return copiedMap;
    }

    static void fillMap(int[][] map, )





    public static void main(String[] args) throws IOException {
        



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
