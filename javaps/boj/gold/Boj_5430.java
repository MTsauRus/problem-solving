package javaps.boj.gold;
import java.io.*;
import java.util.*;

// 5430. AC (G5)
// 자료 구조
public class Boj_5430 {
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            solve();
        }
        System.out.println(sb);
    }

    private static void solve() throws IOException {
        String command = br.readLine();
        int N = Integer.parseInt(br.readLine());
        String inputStr = br.readLine();

        Deque<Integer> dq = new ArrayDeque<>();
        

        st = new StringTokenizer(inputStr.substring(1, inputStr.length() - 1), ",");
        
        while (st.hasMoreTokens()) {
            dq.offer(Integer.parseInt(st.nextToken()));
        }

        boolean isReverse = false;
        boolean isError = false;

        for (char cmd : command.toCharArray()) {
            if (cmd == 'R') {
                isReverse = !isReverse; 
            } else { 
                if (dq.isEmpty()) {
                    isError = true;
                    break;
                }

                if (isReverse) {
                    dq.pollLast();
                } else {
                    dq.pollFirst();
                }
            }
        }

        if (isError) {
            sb.append("error\n");
        } else {
            makeOutput(dq, isReverse);
        }
    }

    private static void makeOutput(Deque<Integer> dq, boolean isReverse) {
        sb.append('[');
        
        while (!dq.isEmpty()) {
            if (isReverse) {
                sb.append(dq.pollLast());
            } else {
                sb.append(dq.pollFirst());
            }
        
            if (!dq.isEmpty()) {
                sb.append(',');
            }
        }
        
        sb.append(']').append('\n');
    }
}