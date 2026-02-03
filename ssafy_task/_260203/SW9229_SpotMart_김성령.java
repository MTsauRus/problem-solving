package ssafy_task._260203;
import java.util.*;
import java.io.*;

// 투 포인터
public class SW9229_SpotMart_김성령 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int T;
    
    public static void main(String[] args) throws IOException {
        T = nextInt();
        for (int t = 1; t < T+1; t++) {
            int N = nextInt();
            int goal = nextInt();
            int ans = -1;

            int[] snacks = new int[N];
            for (int i = 0; i < N; i++) {
                snacks[i] = nextInt();
            }
            Arrays.sort(snacks);

            int s = 0;
            int e = N-1;

            while (s < e) {
                int tmpSum = snacks[s] + snacks[e];
                if (tmpSum < goal) {
                    ans = Math.max(ans, tmpSum);
                    s++;
                } else if (tmpSum == goal) {
                    ans = tmpSum;
                    break;
                } else {
                    e--;
                }
            }
            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }   
    
    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            String line = br.readLine();
            if (line == null) return null;
            st = new StringTokenizer(line);
        } return st.nextToken();
    }
    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
}
