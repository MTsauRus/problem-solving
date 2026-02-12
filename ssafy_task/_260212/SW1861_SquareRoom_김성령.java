package ssafy_task._260212;

import java.util.*;
import java.io.*;

// 방 번호 -> 좌표값의 경우 rows, cols 배열 두 개를 관리
public class SW1861_SquareRoom_김성령 {
    static int N, ansCnt, ansNum;
    static int[][] board;
    static int[] rows, cols;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            ansCnt = 1;
            ansNum = 1;
            N = Integer.parseInt(br.readLine());
            board = new int[N][N];
            rows = new int[N*N+1];
            cols = new int[N*N+1];
            
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    int input = Integer.parseInt(st.nextToken());
                    board[i][j] = input;
                    rows[input] = i;
                    cols[input] = j;
                }
            }

            for (int i = 1; i <= N*N;) {
                int nextNum = move(i);
                i = nextNum+1;
            }
            sb.append("#" + t + " " + ansNum + " " + ansCnt + "\n");
        }
        System.out.println(sb);
    }

    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};
    static int move(int s) {
        int cnt = 1;
        int r = rows[s];
        int c = cols[s];
        while (true) {
        boolean again = false;
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr<0||nr>=N||nc<0||nc>=N) continue;
                if (board[nr][nc] == board[r][c]+1) {
                    cnt++;
                    r = nr;
                    c = nc;
                    again = true;
                    break;
                }
            }
            if (again) continue;
            break;
        }
        if (ansCnt < cnt) {
            ansCnt = cnt;
            ansNum = s;
        }
        return board[r][c]; // 마지막으로 밟은 칸 번호 리턴
    }
}
