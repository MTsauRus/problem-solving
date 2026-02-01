package ssafy_task._260129;

import java.util.*;
import java.io.*;

public class SW1225_PasswordGenerator_김성령 {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringTokenizer st;
  static StringBuilder sb = new StringBuilder();
  
  public static void main(String[] args) throws IOException{
    for (int t = 1; t < 11; t++) {
      int foo = nextInt();
      Deque<Integer> dq = new ArrayDeque<>();

      for (int i = 0; i < 8; i++) {
        dq.offer(nextInt());
      }

      Boolean breakWhile = false;

      while (true) {
        for (int i = 1; i < 6; i++) {
          int target = dq.pollFirst() - i;
          if (target <= 0) {
            target = 0;
            dq.offerLast(target);
            breakWhile = true;
            break;
          } else {
            dq.offerLast(target);
          }
        }
        if (breakWhile) break;
      }

      sb.append("#").append(t).append(" ");
      for (int i = 0; i < 8; i++) {
        sb.append(dq.pollFirst()).append(" ");
      }
      sb.append("\n");
    }
    System.out.println(sb);
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