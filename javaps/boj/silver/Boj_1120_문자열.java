package javaps.boj.silver;

import java.io.*;
import java.util.StringTokenizer;

// S4 브루트포스
// 와일드카드 생각. B에서 A랑 겹치는거 출력하면 그게 답. 나머지는 와일드카드에 B랑 정확히 일치하는 문자를 넣으면 되므로. 
public class Boj_1120_문자열 {
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    String str1 = st.nextToken();
    String str2 = st.nextToken();
    
    int ans = 51;
    for (int i = 0; i < str2.length() - str1.length() + 1; i++) {
      int tmpDiff = 0;
      for (int j = 0; j < str1.length(); j++) {
        if (str1.charAt(j) != str2.charAt(i+j)) {
          tmpDiff++;
        }
      }
      ans = Math.min(ans, tmpDiff);
    }
    System.out.println(ans);
  }
}
