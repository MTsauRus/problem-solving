package samsung;

import java.io.*;
import java.util.*;

public class 고대문명유적탐사 {
    static int K, M;
    static Deque<Integer> nextNums = new ArrayDeque<>();
    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};
    static int[][] board;
    static int gmax;
    static boolean[][] isItem;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        K = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[5][5];
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            nextNums.offer(Integer.parseInt(st.nextToken()));
        }

        for (int i = 0; i < K; i++) {
            int[][] bestBoard = findBestRot();
            // 회전해도 유물 못 얻으면 종료
            if (bestBoard == null) break;

            board = bestBoard;
            int nowScore = calcScore();
            sb.append(nowScore + " ");
        }
        System.out.println(sb);
    }

    static int[][] findBestRot() {
        int maxScore = 0;
        int[][] bestBoard = null;

        // 회전 -> c -> r
        for (int rot = 0; rot <= 2; rot++) {
            for (int c = 0; c < 3; c++) {
                for (int r = 0; r < 3; r++) {
                    int[][] rotatedBoard = rotate(board, r, c, rot);
                    int tmpScore = calcScore(rotatedBoard);
                    if (tmpScore > maxScore) {
                        maxScore = tmpScore;
                        bestBoard = rotatedBoard;
                    }
                }
            }
        }

        return bestBoard;
    }

    static class MaxNode implements Comparable<MaxNode>{
        int sum, rot, r, c;
        public MaxNode(int sum, int rot, int r, int c) {
            this.sum = sum;
            this.rot = rot;
            this.r = r;
            this.c = c;
        }

        @Override
        public int compareTo (MaxNode o) {
            if (this.sum != o.sum) return Integer.compare(o.sum, this.sum);
            if (this.rot != o.rot) return Integer.compare(this.rot, o.rot);
            if (this.c != o.c) return Integer.compare(this.c, o.c);
            return Integer.compare(this.r, o.r);
        }
    }

    // 점수 계산
    static int calcScore(int[][] tmpBoard) {
        boolean[][] visited = new boolean[5][5];
        int score = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (!visited[i][j]) {
                    visited[i][j] = true;
                    score += bfs(board, i, j, visited);
                }
            }
        }
        return score;
    }

    static int bfs(int[][] board, int r, int c, boolean[][] visited) {
        int cnt = 1;
        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};
        Deque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{r, c});

        while (!dq.isEmpty()) {
            int[] now = dq.poll();

            for (int i = 0; i < 4; i++) {
                int nr = now[0] + dr[i];
                int nc = now[1] + dc[i];
                if (nr < 0 || nc < 0 || nr >= 5 || nc >= 5 || visited[nr][nc]) continue;
                if (board[nr][nc] == board[now[0]][now[1]]) {
                    visited[nr][nc] = true;
                    cnt++;
                    dq.offer(new int[]{nr, nc});
                } 
            }

        }
        
        return (cnt >= 3) ? cnt : 0;
    }

    // 채워넣을게 없으면 false 리턴
    static boolean fillBlank() {
        boolean flag = false;
        for (int c = 0; c < 5; c++) {
            for (int r = 4; r >= 0; r--) {
                if (gBoard[r][c] == 0) {
                    gBoard[r][c] = nextNums.poll();
                    flag = true;
                }
            }
        }
        return flag;
    }

    static int[][] copyBoard(int[][] origin) {
        int[][] copied = new int[5][5];
        for (int i = 0; i < 5; i++) {
            copied[i] = origin[i].clone();
        }
        return copied;
    }

    static int[][] rotate(int[][] tmpBoard, int r, int c, int rot) {
        int[][] ret = new int[5][5];
        for (int i = 0; i < 5; i++) {
            ret[i] = tmpBoard[i].clone();
        }

        for (int times = 0; times <= rot; times++) {
            // tmp: 3*3 회전된 부분 보드
            int[][] tmp = new int[3][3];
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    tmp[j][2-i] = ret[r+i][c+j];
                }
            }
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    ret[r+i][c+j] = tmp[i][j];
                }
            }
        }
        return ret;
    }

    static void modGBoard(MaxNode maxNode) {
        int rot = maxNode.rot;
        int r = maxNode.r;
        int c = maxNode.c;
        int[][] selected = rotate(r, c, rot);
        // 보드 돌리기
        for (int x = 0; x < 3; x++) {
            for (int y = 0; y < 3; y++) {
                gBoard[r+x][c+y] = selected[x][y];
            }
        }

        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};
        Deque<int[]> dq = new ArrayDeque<>();
        boolean[][] visited = new boolean[5][5];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (!visited[i][j]) {
                    visited[i][j] = true;
                    if (bfs(gBoard, i, j, visited) >= 3) {
                        dq.offer(new int[]{i, j});

                        while (!dq.isEmpty()) {
                            int[] now = dq.poll();
                            for (int k = 0; k < 4; k++) {
                                int nr = now[0] + dr[k];
                                int nc = now[1] + dc[k];

                                if (nr < 0 || nc < 0 || nr >= 5 || nc >= 5) continue;
                                if (gBoard[nr][nc] == gBoard[i][j]) {
                                    visited[nr][nc] = true;
                                    gBoard[nr][nc] = 0;
                                    dq.offer(new int[]{nr, nc});
                                }
                            }
                        }
                    }
                }
            }
        }
    }
 }
