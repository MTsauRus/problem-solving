package ssafy_task._260415;

import java.io.*;
import java.util.*;

public class SW4038_WordFrequency_김성령 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            String B = br.readLine().trim();
            String S = br.readLine().trim();

            sb.append("#" + t + " " + kmpSearch(B, S) + "\n");
        }
        System.out.println(sb);        
    }

    public static int[] LPS(String pattern) {
        int pLen = pattern.length();
        int[] lps = new int[pLen];

        // j: 접두사의 끝부분이자, 일치하는 부분의 길이
        int j = 0;
        
        // i: 접미사의 끝부분
        for (int i = 1; i < pLen; i++) {
            // 접두사가 존재하고, 비교해야 하는 문자가 다르다면
            while (j > 0 && pattern.charAt(i) != pattern.charAt(j)) {
                // 이전에 일치했던 접두사의 끝 위치로 돌림
                j = lps[j-1];
            }

            if (pattern.charAt(i) == pattern.charAt(j)) {
                j++;
                lps[i] = j;
            }
        }

        return lps;
    }

    public static int kmpSearch(String text, String pattern) {
        int ans = 0;

        int tLen = text.length();
        int pLen = pattern.length();

        int[] lps = LPS(pattern);

        int j = 0;

        for (int i = 0; i < tLen; i++) {
            while (j > 0 && text.charAt(i) != pattern.charAt(j)) {
                j = lps[j-1];
            }

            if (text.charAt(i) == pattern.charAt(j)) {
                if (j == pLen - 1) {
                    ans++;
                    j = lps[j];
                }
                else {
                    j++;
                }
            }
        }

        return ans;
    }
    
}
