package ssafy_task._260414;

import java.io.*;
import java.util.*;

public class JUN17135_CastleDefense_김성령 {
    static int R, C, K;
    static int[][] globalBoard;
    static boolean[][] killed;
    static int globalEnemyCnt, localEnemyCnt;
    static int[] selectedCol;
    static int ans = 0;
    static int killscore;
    static int INF = 1000000;

    static class Node {
        int r, c;
        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
     
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        globalBoard = new int[R+1][C];
        selectedCol = new int[3];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                globalBoard[i][j] = tmp;
                if (tmp == 1) globalEnemyCnt++;
            }
        }
        comb(0, 0);

        System.out.println(ans);

    }

    static void comb(int idx, int depth) {

        if (depth == 3) {

            localEnemyCnt = globalEnemyCnt;
            killscore = 0;
            int[][] board = copyBoard(globalBoard);
            simulation(board);
            ans = Math.max(ans, killscore);
            return;
        }

        for (int i = idx; i < C; i++) {
            selectedCol[depth] = i;
            comb(i+1, depth+1);
        }
    }

    static void simulation(int[][] board) {
        Node[] archerArr = new Node[3];
        archerArr[0] = new Node(R, selectedCol[0]);
        archerArr[1] = new Node(R, selectedCol[1]);
        archerArr[2] = new Node(R, selectedCol[2]);
        while (localEnemyCnt > 0) {
            selectMinDist(archerArr, board);
            board = fire(board);
            board = march(board);
            
        }
    }

    static void selectMinDist(Node[] archerArr, int[][] board) {
        killed = new boolean[R][C];
        for (Node now : archerArr) {
            Node target = null;
            int minDist = INF;
            for (int i = R-1; i >= 0; i--) {
                for (int j = 0; j < C; j++) {
                    if (board[i][j] == 1) {
                        int tmpDist = Math.abs(now.r-i) + Math.abs(now.c-j);
                        if (tmpDist > K) continue;

                        if (target == null) {
                            target = new Node(i, j);
                            minDist = tmpDist;
                        } else {
                            if (minDist < tmpDist) continue;
                            else if (minDist == tmpDist) {
                                if (j < target.c) {
                                    target = new Node(i, j);
                                }
                            }
                            else {
                                minDist = tmpDist;
                                target = new Node(i, j);
                            }
                        }
                    }
                }
            }

            if (target != null)
                killed[target.r][target.c] = true;

        }
    }

    static int[][] fire(int[][] board) {
        // killscore++, localEnemyCnt--
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (killed[i][j]) {
                    killscore++;
                    localEnemyCnt--;
                    board[i][j] = 0;
                }
            }
        }

        return board;
    }    

    static int[][] march(int[][] board) {
        // localEnemyCnt--
        for (int j = 0; j < C; j++) {
            if (board[R-1][j] == 1) {
                board[R-1][j] = 0;
                localEnemyCnt--;
            }
        }
        for (int i = R-2; i >= 0; i--) {
            for (int j = 0; j < C; j++) {
                board[i+1][j] = board[i][j];
            }
        }

        for (int j = 0; j < C; j++) {
            board[0][j] = 0;
        }

        return board;
    }

    static int[][] copyBoard(int[][] before) {
        int[][] copied = new int[R+1][C];
        for (int i = 0; i < R; i++) {
            copied[i] = before[i].clone();
        }

        return copied;
    }
}
