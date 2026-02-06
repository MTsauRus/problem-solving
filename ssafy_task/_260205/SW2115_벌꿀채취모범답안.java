package ssafy_task._260205;

import java.util.*;
import java.io.*;

public class SW2115_벌꿀채취모범답안 {
    static int N, M, C;
    static int[][] map, maxMap; // 입력받은 벌통 map, 각 위치부터 연속된 M개의 벌통 중 최대 이익

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int TC = Integer.parseInt(br.readLine());

        for (int t = 1; t < TC+1; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            
            map = new int[N][N];
            maxMap = new int[N][N-M+1];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            System.out.println("#"+t+" "+getMaxBenefit());
        }
    }

    static int getMaxBenefit() {
        // 연속된 M개를 선택할 수 있는 모든 행의 열의 위치마다 최대 이익 계산
        makeMaxMap();
        // 두 일꾼의 선택 조합
        return processCombination();
    }
    
    static void makeMaxMap() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - M + 1; j++) { // 시작이 가능한 인덱스
                // i, j 위치에서 부분집합을 따져보고 최대 이익 계산
                subset(i, j, 0, 0, 0);
                
            }   
        }   
    }

    static void subset(int i, int j, int cnt, int sum, int powSum) {
        if (sum > C) return; // sum이 C 이하일 때에만 maxMap 갱신
        
        if (cnt == M) { 
            if (maxMap[i][j-M] < powSum) maxMap[i][j-M] = powSum;
            return;
        }

        subset(i, j+1, cnt+1, sum, powSum);
        subset(i, j+1, cnt+1, sum+map[i][j], powSum + map[i][j] * map[i][j]);
        
    }

    static int processCombination() {
        int aBenefit, bBenefit, max=0;
        
        // 일꾼 두명 반복문으로 구현
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N-M+1; j++) {
                // 일꾼 A 고정
                aBenefit = maxMap[i][j];
                bBenefit = 0; // 반복 돌때마다 초기화
                for (int i2 = i; i2 < N; i2++) { // B일꾼은 A일꾼의 시작행부터
                    int start = (i==i2) ? j+M : 0; // 두 행이 같으면 떨어져서, 다른행이면 처음부터
                    for (int j2 = start; j2 < N-M+1; j2++) {
                        if (bBenefit < maxMap[i2][j2]) {
                            bBenefit = maxMap[i2][j2];
                        }
                    }
                }
                if (max < aBenefit+bBenefit) {
                    max = aBenefit+bBenefit;
                }
            }
        }
        return max;
    }

}
