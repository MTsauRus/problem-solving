package ssafy_task._260212;

import java.io.*;
import java.util.*;

public class SW14510_TreeHeight_김성령 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            int N = Integer.parseInt(br.readLine());
            int[] tree = new int[N];
            int max = 0;
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int now = Integer.parseInt(st.nextToken());
                max = Math.max(now, max);
                tree[i] = now;
            }
            int sum = 0;
            for (int i = 0; i < N; i++) {
                tree[i] = max - tree[i];
                sum += tree[i];
            }

            int ans = 0;
            boolean odd = true;
            Arrays.sort(tree);

            while (sum > 0) {
                ans++;
                if (odd) { // 1 빼주기
                    for (int i = 0; i < N; i++) {
                        if (tree[i] == 0) continue;
                        else if (tree[i] == 2) continue;
                        else if (tree[i] == 1) {
                            tree[i]--; sum--; break;
                        } else {
                            tree[i] -= 1; sum--; break;
                        }
                    }
                    odd = !odd;
                } else { // 2 빼주기
                    for (int i = 0; i < N; i++) {
                        if (tree[i] == 0) continue;
                        else if (tree[i] == 1) continue;
                        else if (tree[i] == 2) {
                            tree[i] -= 2; sum -=2; break;
                        } else {
                            tree[i] -= 2; sum -=2; break;
                        }
                    } 
                    odd = !odd;
                }
            }
            sb.append("#").append(t + " " + ans + "\n");
        }
        System.out.println(sb);
    }
}
