package ssafy_task._260129;

import java.util.*;
import java.io.*;

// 자료 구조, 수학
public class SW3260_SumOfTwoNumbers_김성령 {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    StringBuilder sb = new StringBuilder();

    int T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t < T+1; t++) {
      sb.append("#").append(t).append(" ");
      st = new StringTokenizer(br.readLine());
      String a = st.nextToken();
      String b = st.nextToken();

      int len = Math.max(a.length(), b.length());
      char[] arr = new char[len+1];
      char[] brr = new char[len+1];

      Arrays.fill(arr, '0');
      Arrays.fill(brr, '0');
      
      int[] crr = new int[len+1];

      for (int i = 0; i < a.length(); i++) {
        arr[i] = a.charAt(a.length()-i-1);
      }

      for (int i = 0; i < b.length(); i++) {
        brr[i] = b.charAt(b.length()-i-1);
      }
      

      int upper = 0;
      for (int i = 0; i < len; i++) {
        int ta = arr[i] - '0';
        int tb = brr[i] - '0';

        if (ta + tb + upper >= 10) {
          crr[i] = upper + ta + tb - 10;
          upper = 1;
        } else {
          crr[i] = upper + ta + tb;
          upper = 0;
        }
      }
      if (upper == 1) {
        crr[len] = 1;
        sb.append(1);
      }

      for (int i = len-1; i > -1; i--) {
        sb.append(crr[i]);
      }
      sb.append("\n");
    }
    System.out.println(sb);
  }  
}
