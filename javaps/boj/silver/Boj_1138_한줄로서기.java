package javaps.boj.silver;

import java.io.*;

public class Boj_1138_한줄로서기 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb =  new StringBuilder();

    int N = Integer.parseInt(br.readLine());
    String[] arr = br.readLine().split(" ");
    int[] iarr = new int[N];
    for (int i = 0; i<N;i++) {
      iarr[i] = Integer.parseInt(arr[i]);
    }
    int[] ans = new int[N];
    
    for (int i = 1; i < N+1; i++) {
      int leftNum = iarr[i-1];
      
      int idx = 0;

      while (leftNum > -1) {
        if (leftNum == 0) {
          if (ans[idx] == 0) {
            ans[idx] = i;
            break;
          } else {
            idx++;
            continue;
          }
        } else {
          if (ans[idx] == 0) {
            leftNum--;
            idx++;
          } else {
            idx++;
          }
        }
      }
    }

    for (int i : ans) {
      sb.append(i).append(" ");
    }

    System.out.println(sb);
  }  
}
