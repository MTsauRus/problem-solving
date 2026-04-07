package ssafy_task._260407;

import java.io.*;
import java.util.*;

public class SW2112_ProtectionFilm_김성령 {
    static int R, C, K;
    static int[][] board;
    static int ans;
    static int[] selected;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            
            board = new int[R][C];
            selected = new int[R];
            Arrays.fill(selected, -1);
            ans = -1;

            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());        
                }
            }
            
            for (int i = 0; i < R; i++) {
                //System.out.println("now: " + i);
                Arrays.fill(selected, -1);
                selectInject(0, 0, i);
                if (ans != -1) break;
            }

            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }   

    static void selectInject(int idx, int cnt, int injectCnt) {
        if (cnt == injectCnt) {
            //System.out.println(Arrays.toString(selected));
            if (simul()) {
                ans = injectCnt;
                return;
            }
            return;
        }

        if (idx == R) return;

        
        // 현재 idx 0 선택
        selected[idx] = 0;
        selectInject(idx+1, cnt+1, injectCnt);
        // 현재 idx 1 선택
        selected[idx] = 1;
        selectInject(idx+1, cnt+1, injectCnt);
        // 선택 안하기
        selected[idx] = -1;
        selectInject(idx+1, cnt, injectCnt);
        
    }
    
    static boolean simul() {
        for (int i = 0; i < C; i++) {
            int tmpCnt = 1;
            int bef = -1;
            if (selected[0] == -1) bef = board[0][i];
            else if (selected[0] == 0) bef = 0;
            else bef = 1;
            
            for (int j = 1; j < R; j++) {

                // 다음칸 확인, 같으면 tmpCnt++, 다르면 초기화
                int now = -1;
                if (selected[j] == -1) now = board[j][i];
                else if (selected[j] == 0) now = 0;
                else now = 1;

                if (bef == now) {
                    tmpCnt++;
                    if (tmpCnt >= K) // 조건 충족, 더 볼 필요 없음
                        break; 
                } else {
                    tmpCnt = 1;
                    bef = now;
                }
            }
            if (tmpCnt < K) {
                return false;
            } 
        }

        return true;
    }
}
