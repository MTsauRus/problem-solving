package ssafy_task._260206;

import java.util.*;
import java.io.*;

// 비트마스킹, 부분집합, dfs
public class SW3421_BurgerMaster_김성령_copy {

    static List<Integer> checkList = new ArrayList<>();
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());  

        for (int t = 1; t < T+1; t++) {
            ans = 0;   
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            checkList = new ArrayList<>();
            for (int m = 0; m < M; m++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                
                int checkBit = 0;
                checkBit = checkBit|1<<(a-1); // <<연산자 우선순위가 더 높음
                checkBit |= 1<<(b-1); // b 자리만큼 왼쪽으로 밀고 or연산

                checkList.add(checkBit);
            }
            makeHamburger(0, N, 0);

            sb.append("#").append(t).append(" ").append(ans+"\n");
        }
        System.out.println(sb);
    }

    static void makeHamburger(int depth, int N, int bit) {
        if (depth == N) {
            for (int check : checkList) {
                if ((bit & check) == check)
                    return;
            }
            ans++;
            return;
        }
        // 현재 비트 포함
        makeHamburger(depth+1, N, bit|(1<<depth));
        // 현재 비트 미포함
        makeHamburger(depth+1, N, bit);
    }
    
    /**
     * 
     * 
     * check(int idx) {
     *  if (idx == N) {
     *   ans++; return;  
     *  }
     * 
     *  check(idx + 1); // 현재 재료를 선택하지 않는 경우
     * 
     *  boolean canSelect = true;
     * 
     * // 충돌 여부 판단
     *  for (int k = 0; k < idx; k++) {
     *   if (selected[k] && bad[idx][k]) {
     *    canSelect = false; break;   
     * }  
     * }
     * 
     * // 충돌 없으면 선택
     * if (canSelect) selected[idx] = true; check(idx+1); selected[idx] = false;
     * }
     */
}
