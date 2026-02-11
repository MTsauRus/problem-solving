package ssafy_task._260211;

import java.util.*;
import java.io.*;

public class SW4796_HighMountain_김성령 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int T = sc.nextInt();
        for (int t = 1; t < T+1; t++) {
            int N = sc.nextInt();
            int[] arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();

            }

            int ans = 0;
            int asc = 0, desc = 0;
            int idx = 0;

            while (arr[idx] > arr[idx+1]) {
                idx++;
                if (idx+1 >= N) { // 계속 감소. 답 x
                    break;
                }
            }
            while (idx < N-1) {
                while (arr[idx] < arr[idx+1]) {
                    asc++;
                    idx++;
                    if (idx+1 == N) break; //
                }
                if (idx+1 == N) break;
                while (arr[idx] > arr[idx+1]) {
                    desc++;
                    idx++;
                    if (idx+1 == N) break;
                }
                ans += (desc*asc);
                asc = 0;
                desc = 0;
            }
            sb.append("#").append(t).append(" ").append(ans).append("\n");
            }
            System.out.println(sb);
        }
    }

