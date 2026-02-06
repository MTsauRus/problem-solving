package ssafy_task._260206;

import java.util.*;
import java.io.*;

public class SW1873_BattleField_김성령 {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int N, r, c, R, C;
    static char[][] board;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            r = 0;
            c = 0;
            board = new char[R][C];
            for (int x = 0; x < R; x++) {
                board[x] = br.readLine().toCharArray();
                for (int y = 0; y < C; y++) {
                    if (board[x][y] == '<' || board[x][y] == '>' || board[x][y] == '^' || board[x][y] == 'v') {
                        r = x;
                        c = y;
                    }
                }
            }

            N = Integer.parseInt(br.readLine());
            char[] CMD = br.readLine().toCharArray();

            for (char next : CMD) {
                if (next == 'S') {
                    shoot();
                } else {
                    move(next);
                }
            }

            sb.append('#').append(t).append(" ");
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    sb.append(board[i][j]);
                }
                sb.append("\n");
            } 
        }
        System.out.println(sb);
    }


    static void shoot() {

        // 포탄의 좌표
        int pr = r;
        int pc = c;

        int direction = 0;
        if (board[r][c] == '^') {
            direction = 0;
        } else if (board[r][c] == 'v') {
            direction = 1;
        } else if (board[r][c] == '<') {
            direction = 2;
        } else {
            direction = 3;
        }

        int nr = pr + dr[direction];
        int nc = pc + dc[direction];

        while (0 <= nr && nr < R && 0 <= nc && nc < C) { // 유효하면
            if (board[nr][nc] == '*') { // 벽돌이면
                board[nr][nc] = '.';
                return;
            } else if (board[nr][nc] == '#') { // 강철이면
                return; // 아무일도 일어나지 않음
            } else { // 평지 등
                pr = nr;
                pc = nc; // 다음칸
                nr = pr + dr[direction];
                nc = pc + dc[direction];
                continue;
            } 
        }
    }

    static void move(char cmd) {
        char player = board[r][c];
        int direction = 0;
        if (cmd == 'U') {
            direction = 0;
            player = '^';
        } else if (cmd == 'D') {
            direction = 1;
            player = 'v';
        } else if (cmd == 'L') {
            direction = 2;
            player = '<';
        } else {
            direction = 3;
            player = '>';
        }

        board[r][c] = player; // 방향전환
        int nr = r + dr[direction];
        int nc = c + dc[direction];
        
        if (0 <= nr && nr < R && 0 <= nc && nc < C && board[nr][nc] == '.') { // 유효하면
            board[r][c] = '.';
            r = nr;
            c = nc; // 이동
            board[nr][nc] = player;
        }
    }
}
