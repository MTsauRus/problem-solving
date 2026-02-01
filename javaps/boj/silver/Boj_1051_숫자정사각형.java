package javaps.boj.silver;

import java.util.*;
import java.io.*;

public class Boj_1051_숫자정사각형 {
    public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());

      int R = Integer.parseInt(st.nextToken());
      int C = Integer.parseInt(st.nextToken());
      int[][] map = new int[R][C];
      int ans = 1;

      for (int i = 0; i < R; i++) {
        char[] tmp = br.readLine().toCharArray();
        for (int j = 0; j < C; j++) {
          map[i][j] = tmp[j] - '0';
        }
      }

      for (int x = 0; x < R; x++) {
        for (int y = 0; y < C; y++) {
          for (int k = 1; k < Math.min(R-x, C-y); k++) {
            int px1 = x+k;
            int py1 = y;
            int px2 = x+k;
            int py2 = y+k;
            int px3 = x;
            int py3 = y+k;
            if (map[x][y] == map[px1][py1] && map[px1][py1] == map[px2][py2] && map[px2][py2] == map[px3][py3]) {
              ans = Math.max(ans, (int) Math.pow(k+1, 2));
            }
          }
        }
      }

      
      System.out.println(ans);

    }
}
