package ssafy_task._260312;

import java.io.*;
import java.util.*;

public class SW5656_BreakingBricks_김성령 {
    static int N, R, C;
    static int[][] board;
    static int ans;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            ans = Integer.MAX_VALUE;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            
            board = new int[R][C];
            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            // System.out.println();
            // board = dropBall(board, 9);
            // board = dropBall(board, 9);
            // printArr(board);
            // board = arrangeBoard(board);
            // printArr(board);
            for (int i = 0; i < C; i++) {
                dfs(0, copyBoard(board), i);
            }
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }

    static void dfs(int depth, int[][] nBoard, int dropC) {
        if (depth == N) {
            int tmpSum = 0;
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (nBoard[i][j] > 0) tmpSum++;
                }
            }
            ans = Math.min(ans, tmpSum);
            return;
        }

        // 공떨구기 로직
        nBoard = dropBall(nBoard, dropC);
        // 벽돌삭제 로직
        nBoard = arrangeBoard(nBoard);
        // 다음 dropC 분기
        for (int i = 0; i < C; i++) {
            dfs(depth+1, copyBoard(nBoard), i);
        }
    }

    static class Block {
        int r, c, p;
        public Block(int r, int c, int p) {
            this.r = r;
            this.c = c;
            this.p = p;
        }
    }
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    static int[][] dropBall(int[][] nBoard, int dropC) {
        int r = 0, c = dropC;

        Deque<Block> dq = new ArrayDeque<>();
        // bfs 탐색 중복 방지 + 삭제될 블록 탐지
        boolean[][] visited = new boolean[R][C];
        boolean[][] deleted = new boolean[R][C];
        
        while (r < R && nBoard[r][c] == 0) {
            r++;
        }
        
        if (r == R) {
            // 벽돌이 아예 없는 경우
            return nBoard;
        }
        int range = nBoard[r][c];
        // 사정거리 1짜리 박으면 걍 그거 없애고 리턴
        if (range == 1) {
            nBoard[r][c] = 0;
            return nBoard;
        }

        visited[r][c] = true;
        deleted[r][c] = true;
        dq.offer(new Block(r, c, range));

        while (!dq.isEmpty()) {
            Block now = dq.pollFirst();

            for (int k = 1; k <= now.p-1; k++) {
                for (int i = 0; i < 4; i++) {
                    int nr = now.r + dr[i]*k;
                    int nc = now.c + dc[i]*k;
                    if (nr<0||nc<0||nr>=R||nc>=C) continue;
                    deleted[nr][nc] = true;

                    // power가 1이면 굳이 큐에 안넣어도 됨
                    if (nBoard[nr][nc] == 1) continue;
                    // 큐에 들어간 적이 있다면 넘기기
                    if (visited[nr][nc]) continue;
                    visited[nr][nc] = true;
                    dq.offer(new Block(nr, nc, nBoard[nr][nc]));
                }
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (deleted[i][j]) {
                    nBoard[i][j] = 0;
                }
            }
        }
        return nBoard;
    }

    static int[][] arrangeBoard(int[][] nBoard) {
        for (int c = 0; c < C; c++) {
            int[] tmpArr = new int[R];
            int rIdx = 0;
            for (int r = R-1; r >= 0; r--) {
                if (nBoard[r][c] != 0) {
                    tmpArr[rIdx++] = nBoard[r][c];
                }
            }
            
            rIdx = 0;
            for (int r = R-1; r >= 0; r--) {
                nBoard[r][c] = tmpArr[rIdx++];
            }

        }

        return nBoard;
    }


    static int[][] copyBoard(int[][] befBoard) {
        int[][] copied = new int[R][C];
        for (int i = 0; i < R; i++) {
            copied[i] = befBoard[i].clone();
        }
        return copied;
    }

    static void printArr(int[][] nBoard) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                sb.append(nBoard[i][j] + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}