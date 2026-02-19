package ssafy_task._260219;

import java.util.*;
import java.io.*;

/*
매번 큐/덱을 복사하는 방법 대신, 현재 덱의 사이즈를 측정한 후, 
while (qSize-->0) 이걸로 돌리면 됨!!
*/

public class JUN3055_Escape_김성령 {
    static char[][] board;
    static int r, c, er, ec, wr, wc, R, C;
    static Deque<Integer[]> wQ = new ArrayDeque<>();
    static boolean[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new char[R][C];
        for (int i = 0; i < R; i++) {
            board[i] = br.readLine().toCharArray();
        }

        r = 0; c = 0; er = 0; ec = 0; wr = 0; wc = 0;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] == 'D') {
                    er = i;
                    ec = j;
                } else if (board[i][j] == 'S') {
                    r = i;
                    c = j;
                    board[i][j] = '.';
                } else if (board[i][j] == '*') {
                    wQ.offer(new Integer[]{i, j});
                }
            }
        }

        visited = new boolean[R][C];

        System.out.println(solve());

    }    
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};


    static String solve() {

        Deque<Integer[]> sQ = new ArrayDeque<>();
        sQ.offer(new Integer[]{r, c, 0});

        while (true) {
            Deque<Integer[]> nwQ = new ArrayDeque<>();
            while (!wQ.isEmpty()) {
                Integer[] nextWater = wQ.pollFirst();
                for (int i = 0; i < 4; i++) {
                    int nwr = nextWater[0] + dr[i];
                    int nwc = nextWater[1] + dc[i];
                    if (nwr<0||nwr>=R||nwc<0||nwc>=C||board[nwr][nwc]=='*'||board[nwr][nwc]=='D'||board[nwr][nwc]=='X')
                        continue;
                    board[nwr][nwc] = '*';
                    nwQ.offer(new Integer[] {nwr, nwc});
                }
            }
            // 다음 레벨 큐로 복사
            wQ = nwQ;

            Deque<Integer[]> nsQ = new ArrayDeque<>();
            while(!sQ.isEmpty()) {
                Integer[] nextMove = sQ.pollFirst();
                for (int i = 0; i < 4; i++) {
                    int nsr = nextMove[0] + dr[i];
                    int nsc = nextMove[1] + dc[i];
                    if (nsr<0||nsr>=R||nsc<0||nsc>=C||board[nsr][nsc]=='*'||board[nsr][nsc]=='X'||visited[nsr][nsc])
                        continue;
                    if (board[nsr][nsc] == 'D') {
                        return String.valueOf(nextMove[2]+1);
                    }
                    visited[nsr][nsc] = true;
                    nsQ.offer(new Integer[]{nsr, nsc, nextMove[2]+1});
                }
            }
            if (nsQ.isEmpty()) {
                return "KAKTUS"; // 다음 이동 경로가 없다면 리턴
            }
            // 다음 레벨 큐로 복사
            sQ = nsQ;
        }
    }
}