package javaps.boj.silver;
import java.io.*;
import java.util.*;

// 수학
public class Boj_1057_토너먼트 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int A = Integer.parseInt(st.nextToken());
    int B = Integer.parseInt(st.nextToken());
  
    int iter = 0;
    while (true) {
      iter++;
      // 정수 나눗셈 올림: 1을 더하고 나누자. int끼리의 나눗셈은 소수점을 자동으로 버림. 
      A = (A+1)/2;
      B = (B+1)/2;
      
      if (A==B) {
        System.out.println(iter);
        break;
      }
    }
  }
}
