package ssafy_task._260313;

import java.io.*;
import java.util.*;

public class SW4014_RunwayConstruction_김성령 {
    static int N, ans, X;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            X = Integer.parseInt(st.nextToken());
            
            // // 테스트코드
            // int[] test = new int[N];
            // ans = 0;
            // st = new StringTokenizer(br.readLine());
            // for (int i = 0; i < N; i++) {
            //     test[i] = Integer.parseInt(st.nextToken());
            // }

            // solve(test);
            // System.out.println(ans);
            // System.exit(0);







            board = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            ans = 0;
            for (int i = 0; i < N; i++) {
                solve(board[i]);
            }

            for (int c = 0; c < N; c++) {
                int[] tmpArr = new int[N];
                for (int r = 0; r < N; r++) {
                    tmpArr[r] = board[r][c];

                }

                solve(tmpArr);
            }

            sb.append("#" + t + " " + ans + "\n");
        } 
        System.out.println(sb);
    }


    static void solve(int[] tmpArr) {

        int lv = tmpArr[0];
        int cnt = 1;
        boolean add = true;
        for (int j = 1; j < N; j++) {
            if (tmpArr[j] == lv) cnt++;
            
            // 다음 칸이 더 큰 경우
            else if (tmpArr[j] > lv) {
                // 딱 1칸 차이나는 경우
                if (tmpArr[j] == lv+1) {
                    if (cnt < X) {
                        add = false;
                        break;
                    } else {
                        lv = tmpArr[j];
                        cnt = 1;
                    }

                } else { // 2칸 이상 -> break
                    add = false;
                    break;
                }
                
            // 다음 칸이 더 작은 경우
            } else { 
                if (tmpArr[j] < lv-1) {
                    add = false;
                    break;
                } else {
                    int localLv = tmpArr[j];
                    for (int k = j; k < j+X; k++) {
                        // 인덱스를 벗어난 경우 못놓음
                        if (k >= N) {
                            add = false;
                            break;
                        // 높이가 달라졌다면 못놓음
                        } else if (tmpArr[k] != localLv) {
                            add = false;
                            break;
                        }
                    }
                    // 위의 예외조건에 걸리지 않고 살아남았다면
                    lv = tmpArr[j];
                    cnt = 0;
                    // 현재 탐색한 인덱스를 바깥 인덱스에도 업데이트
                    j += X-1;
                    
                }
            }
            if (!add) break;
        }
        // 살아남았다면 
        if (add) {
            ans++;
        }
    }
}
