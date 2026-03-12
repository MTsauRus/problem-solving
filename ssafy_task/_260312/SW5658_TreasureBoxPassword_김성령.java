package ssafy_task._260312;

import java.io.*;
import java.util.*;

public class SW5658_TreasureBoxPassword_김성령 {
    static int N, K;
    static char[] charSet;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            charSet = br.readLine().toCharArray();

            int truncIdx = N/4; // 숫자 크기
            HashSet<Integer> hSet = new HashSet<>();
            List<Integer> numList = new ArrayList<>();

            for (int offset = 0; offset < truncIdx; offset++) {
                for (int idx = offset; idx < N; idx += truncIdx) {
                    int hexMult = truncIdx-1; // 최대자릿수
                    int nowNum = 0;

                    
                    for (int tmpIdx = 0, nowIdx = idx; tmpIdx < truncIdx; nowIdx = (nowIdx+1)%N, tmpIdx++) {
                        if (charSet[nowIdx] <= '9') {
                            nowNum += (charSet[nowIdx] - '0') * Math.pow(16, hexMult);
                        } else {
                            nowNum += (charSet[nowIdx] - 55) * Math.pow(16, hexMult);
                        }
                        hexMult--;
                    }

                    if (hSet.add(nowNum)) {
                        numList.add(nowNum);
                        
                    }
                }
            } 

            Collections.sort(numList, (a,b) -> b-a);

            sb.append("#" + t + " " + numList.get(K-1) + "\n");
        }
        System.out.println(sb);
    }    
}
