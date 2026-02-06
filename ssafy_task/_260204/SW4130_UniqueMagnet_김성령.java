package ssafy_task._260204;

import java.util.*;
import java.io.*;

public class SW4130_UniqueMagnet_김성령 {
    static int[][] magnet;
    static int[] pointer;
    static int[] rotWise;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));      
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            int K = Integer.parseInt(br.readLine());
            magnet = new int[4][8];

            for (int i = 0; i < 4; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 8; j++) {
                    magnet[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            pointer = new int[4];

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int mgNum = Integer.parseInt(st.nextToken())-1;
                int clockwise = Integer.parseInt(st.nextToken());
                rotWise = new int[4];
                rotWise[mgNum] = clockwise;

                rotateRight(mgNum, clockwise);
                rotateLeft(mgNum, clockwise);

                for (int j = 0; j < 4; j++) {
                    if (rotWise[j] == 1) {
                        pointer[j] = (pointer[j] + 7)%8;
                    } else if (rotWise[j] == -1) {
                        pointer[j] = (pointer[j] + 1)%8;
                    }
                }
            }
            int ans = 0;
            for (int i = 0; i < 4; i++) {
                if (magnet[i][pointer[i]] == 1) {
                    ans += 1<<i;
                }
            }

            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }

    static void rotateRight(int mgNum, int clockwise) {
        // 내 자석의 오른쪽 자석 돌리기
        if (mgNum >= 3) return; // 3번 자석 오른쪽에는 자석이 없음
        // 오른쪽 자석 조건 체크
        if (magnet[mgNum][(pointer[mgNum]+2)%8] != magnet[mgNum+1][(pointer[mgNum+1]+6)%8]) {
            rotWise[mgNum+1] = clockwise * (-1); // 다음 자석 회전 결정
            rotateRight(mgNum+1, clockwise * (-1));
        }
    }

    static void rotateLeft(int mgNum, int clockwise) {
        if (mgNum <= 0) return; 
        if (magnet[mgNum][(pointer[mgNum]+6)%8] != magnet[mgNum-1][(pointer[mgNum-1]+2)%8]) {
            rotWise[mgNum-1] = clockwise * (-1); // 다음 자석 회전 결정
            rotateLeft(mgNum-1, clockwise * (-1));
        }
    }
}