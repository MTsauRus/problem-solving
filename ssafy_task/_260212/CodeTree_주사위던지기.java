package ssafy_task._260212;

import java.util.*;
import java.io.*;

public class CodeTree_주사위던지기 {
    static int[][] board;
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken())-1;
        int c = Integer.parseInt(st.nextToken())-1;
        board = new int[N][N];
        board[r][c] = 6;
        st = new StringTokenizer(br.readLine());
        char[] dir = new char[M];
        for (int i = 0; i < M; i++) {
            dir[i] = st.nextToken().charAt(0);
        }

        // Bottom: 0, Up: 1, Left: 2, Right: 3, Down: 4, Top: 5
        int[] dice = new int[]{6, 5, 4, 3, 2, 1};
        int[] dr = new int[]{-1, 1, 0, 0};
        int[] dc = new int[]{0, 0, -1, 1};
        for (int i = 0; i < M; i++) {
            int nextDir = 0;
            if (dir[i] == 'U') nextDir = 0;
            else if (dir[i] == 'D') nextDir = 1;
            else if (dir[i] == 'L') nextDir = 2;
            else nextDir = 3;
            int nr = r + dr[nextDir];
            int nc = c + dc[nextDir];
            if (0<nr||nr>=N||0<nc||nc>=N) continue;
            dice = roll(dice, dir[i]);
            board[nr][nc] = dice[0];
            r = nr;
            c = nc;
        }

        int sum = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sum += board[i][j];
            }
        }

        System.out.println(sum);
    }   
    static int[] roll(int[] dice, char dir) {
        int[] resultDice = new int[6];
        if (dir == 'U') {
            resultDice[0] = dice[1];
            resultDice[1] = dice[5];
            resultDice[2] = dice[2];
            resultDice[3] = dice[3];
            resultDice[4] = dice[0];
            resultDice[5] = dice[4];
        } else if (dir == 'D') {
            resultDice[0] = dice[4];
            resultDice[1] = dice[0];
            resultDice[2] = dice[2];
            resultDice[3] = dice[3];
            resultDice[4] = dice[5];
            resultDice[5] = dice[1];    
        } else if (dir == 'L') {
            resultDice[0] = dice[2];
            resultDice[1] = dice[1];
            resultDice[2] = dice[5];
            resultDice[3] = dice[0];
            resultDice[4] = dice[4];
            resultDice[5] = dice[3];    
        } else {
            resultDice[0] = dice[3];
            resultDice[1] = dice[1];
            resultDice[2] = dice[0];
            resultDice[3] = dice[5];
            resultDice[4] = dice[4];
            resultDice[5] = dice[2];        
        }
        return resultDice;
    } 
}
