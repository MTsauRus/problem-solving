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
    static int[][] map;

    static int[][] copyMap(int[][] prev, int R, int C) {
        int[][] copiedMap = new int[R][C];
        for (int i = 0; i < R; i++) {
            copiedMap[i] = prev[i].clone();
        } return copiedMap;
    }

    public static void main(String[] args) throws IOException {
        R = nextInt();
        C = nextInt();
        K = nextInt();

        List<int[][]> stickers = new ArrayList<>();

        for (int k = 0; k < K; k++) {
            int SR = nextInt();
            int SC = nextInt();
            int[][] sticker = new int[SR][SC];
            for (int sr = 0; sr < SR; sr++) {
                for (int sc = 0; sc < SC; sc++) {
                    sticker[sr][sc] = nextInt();
                }
            }
            stickers.add(sticker);
        }

        map = new int[R][C];

        for (int[][] sticker : stickers) {
            putSticker(sticker, 0);
        }

        int ans = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == 1) {
                    ans++;
                } 
            }
        }
        System.out.println(ans);
    }

    static void putSticker(int[][] sticker, int depth) {
        if (depth == 4) return;
        for (int dr = 0; dr <= R - sticker.length; dr++) { // dr + sr = 맵 인덱스
            for (int dc = 0; dc <= C - sticker[0].length; dc++) {
                boolean breakIter = false;
                for (int sr = 0; sr < sticker.length; sr++) {
                    for (int sc = 0; sc < sticker[0].length; sc++) {
                        if (map[dr+sr][dc+sc] + sticker[sr][sc] == 2)
                            breakIter = true; // 실패, 옆칸으로
                    }
                }
                if (breakIter) continue;
                else {
                    for (int sr = 0; sr < sticker.length; sr++) {
                        for (int sc = 0; sc < sticker[0].length; sc++) {
                            map[dr+sr][dc+sc] += sticker[sr][sc];
                        }
                    }
                    return;
                }
            }
        }
        putSticker(rotate(sticker), depth+1);
    }

    static int[][] rotate(int[][] sticker) {
        int newR = sticker[0].length;
        int newC = sticker.length;

        int[][] returnSticker = new int[newR][newC];

        for (int r = 0; r < sticker.length; r++) {
            for (int c = 0; c < sticker[0].length; c++) {
                returnSticker[c][sticker.length-r-1] = sticker[r][c];
            }
        }
        return returnSticker;
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
