package ssafy_task._260129;

import java.util.*;
import java.io.*;

public class SW3499_PerfectShuffle_김성령 {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringTokenizer st;
  static StringBuilder sb = new StringBuilder();
  
  public static void main(String[] args) throws IOException {
    int T = nextInt();
    
    for (int t = 1; t < T+1; t++) {
      int N = nextInt();

      String[] arr = br.readLine().split(" ");
      String[] front = Arrays.copyOfRange(arr, 0, (arr.length+1)/2);
      String[] rear = Arrays.copyOfRange(arr, (arr.length+1)/2, arr.length);

      String[] ans = new String[N];
      for (int i = 0; i < N/2; i++) {
        ans[i*2] = front[i];
        ans[i*2+1] = rear[i];
      }

      if (N%2==1) {
        ans[N-1] = front[front.length-1];
      }

      sb.append("#").append(t).append(" ");

      for (String s : ans) {
        sb.append(s).append(" ");
      }
    sb.append("\n");
    }
    System.out.println(sb);
  }


  static String next() throws IOException{
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
