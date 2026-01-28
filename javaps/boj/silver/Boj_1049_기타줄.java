package javaps.boj.silver;

import java.util.*;
import java.io.*;

// 1049. 기타줄(S4)
// 정렬, 구현
public class Boj_1049_기타줄 {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int need = Integer.parseInt(st.nextToken());
    int brand = Integer.parseInt(st.nextToken());
    int[] sixPack = new int[brand];
    int[] one = new int[brand];

    for (int i = 0; i < brand; i++) {
      st = new StringTokenizer(br.readLine());
      sixPack[i] = Integer.parseInt(st.nextToken());
      one[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(sixPack);
    Arrays.sort(one);

    int needSixPack = (int) (need / 6);
    int needSixPackPlusOne = needSixPack+1;
    int needOne = need % 6;

    System.out.println(Math.min(Math.min(sixPack[0] * needSixPack + one[0] * needOne, one[0] * need), needSixPackPlusOne * sixPack[0]));
  }
}
