package SWEA.D3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SW1289_MemoryRecovery_김성령 {

// 원재의 메모리 복구하기 (D3)
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
      
        for (int t = 1; t < T+1; t++) {
            String input = br.readLine();
            boolean[] inputBits = new boolean[input.length()];
            for (int i = 0; i < input.length(); i++) {
                inputBits[i] = input.charAt(i) == '1';
            }
            boolean[] ansBits = new boolean[input.length()];
            int ans = 0;
            boolean flag = false;
            for (int i = 0; i < input.length(); i++) {
                if (flag ? !(inputBits[i]^ansBits[i]) : inputBits[i]^ansBits[i]) {
                    flag = !flag;
                    ans += 1;
                }
            }
            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }
}