package javaps.boj.silver;

import java.io.*;
import java.util.*;

// 수학, 비트연산
public class Boj_1094_막대기 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int x = Integer.parseInt(br.readLine());
    // 1. Integer.bitCount(); 이진수 변환 시 1의 개수 리턴
    // 2. Integer.toBinaryString(); 이진수 문자열로 변환
    // 3. (X & 1) == 1, X>>1로 반복 체크

    int ans = 0;
    while (x > 0) {
      if ((x & 1) == 1) {
        ans++;
      }
      x>>=1;
    }
    System.out.println(ans);
  }
}