package samsung;

import java.util.*;
import java.io.*;

public class 고대문명유적탐사_모범 {
    static final int N = 5;
    static final int[] DR = {0, 0, 1, -1};
    static final int[] DC = {1, -1, 0, 0};

    static int K, M;
    static int[][] board = new int[N][N];
    static Deque<Integer> wall = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        readInput();

        StringBuilder sb = new StringBuilder();
        for (int turn = 0; turn < K; turn++) {
            int[][] bestBoard = findBestRotation();
            if (bestBoard == null) break;          // 어떤 회전도 유물 못 얻으면 종료

            board = bestBoard;
            int turnScore = runCascade();
            sb.append(turnScore).append(' ');
        }
        System.out.println(sb.toString().trim());
    }

    static void readInput() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            wall.offer(Integer.parseInt(st.nextToken()));
        }
    }

    /**
     * 27개 회전 후보(각도 3 × 위치 9)를 모두 시도해서 1차 획득 가치가 최대인 보드 반환.
     * 우선순위: 작은 각도 → 작은 열 → 작은 행. 루프 순서로 우선순위를 표현하므로
     * `>` 로만 비교해도 동점일 때 먼저 만난 게 이긴다.
     */
    static int[][] findBestRotation() {
        int bestScore = 0;
        int[][] bestBoard = null;

        for (int times = 1; times <= 3; times++) {     // 90°, 180°, 270°
            for (int c = 0; c < 3; c++) {              // 작은 열 먼저
                for (int r = 0; r < 3; r++) {          // 작은 행 먼저
                    int[][] rotated = rotateSubgrid(board, r, c, times);
                    int score = computeScore(rotated);
                    if (score > bestScore) {
                        bestScore = score;
                        bestBoard = rotated;
                    }
                }
            }
        }
        return bestBoard;
    }

    /**
     * 그룹 제거 → 빈칸 채우기를 더 이상 그룹이 안 나올 때까지 반복.
     * 이번 턴에 획득한 유물의 총합 반환.
     */
    static int runCascade() {
        int total = 0;
        while (true) {
            int score = removeGroups(board);
            if (score == 0) break;
            total += score;
            fillBlanks(board);
        }
        return total;
    }

    /**
     * (r, c)를 좌상단으로 하는 3×3 부분 격자를 시계방향으로 90° × times 회전.
     * 원본은 건드리지 않고 새 보드를 반환. (i, j) → (j, 2-i).
     */
    static int[][] rotateSubgrid(int[][] src, int r, int c, int times) {
        int[][] result = new int[N][N];
        for (int i = 0; i < N; i++) result[i] = src[i].clone();

        for (int t = 0; t < times; t++) {
            int[][] tmp = new int[3][3];
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    tmp[j][2 - i] = result[r + i][c + j];
                }
            }
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    result[r + i][c + j] = tmp[i][j];
                }
            }
        }
        return result;
    }

    /** 보드를 건드리지 않고 점수(크기 ≥ 3인 그룹들의 셀 수 합계)만 계산. */
    static int computeScore(int[][] b) {
        boolean[][] visited = new boolean[N][N];
        int total = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] || b[i][j] == 0) continue;
                int size = bfsGroup(b, i, j, visited, null);
                if (size >= 3) total += size;
            }
        }
        return total;
    }

    /** 크기 ≥ 3인 그룹을 모두 찾아 0으로 만들고 총 점수 반환. */
    static int removeGroups(int[][] b) {
        boolean[][] visited = new boolean[N][N];
        List<List<int[]>> groupsToRemove = new ArrayList<>();
        int total = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] || b[i][j] == 0) continue;
                List<int[]> cells = new ArrayList<>();
                int size = bfsGroup(b, i, j, visited, cells);
                if (size >= 3) {
                    total += size;
                    groupsToRemove.add(cells);
                }
            }
        }

        for (List<int[]> group : groupsToRemove) {
            for (int[] cell : group) {
                b[cell[0]][cell[1]] = 0;
            }
        }
        return total;
    }

    /**
     * (r, c)에서 BFS 시작, visited 마킹. 그룹 크기 반환.
     * collected가 non-null이면 그룹에 속한 셀들을 모두 append. 시작 셀도 카운트됨.
     */
    static int bfsGroup(int[][] b, int r, int c, boolean[][] visited, List<int[]> collected) {
        int color = b[r][c];
        int size = 0;
        Deque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{r, c});
        visited[r][c] = true;

        while (!dq.isEmpty()) {
            int[] cur = dq.poll();
            size++;                                          // ← poll할 때 카운트하면 시작 셀 누락 없음
            if (collected != null) collected.add(cur);
            for (int d = 0; d < 4; d++) {
                int nr = cur[0] + DR[d];
                int nc = cur[1] + DC[d];
                if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if (visited[nr][nc] || b[nr][nc] != color) continue;
                visited[nr][nc] = true;
                dq.offer(new int[]{nr, nc});
            }
        }
        return size;
    }

    /**
     * 0인 셀을 벽면 큐에서 꺼내 채움.
     * 순서: 작은 열 먼저, 같은 열 안에서는 큰 행 먼저.
     */
    static void fillBlanks(int[][] b) {
        for (int c = 0; c < N; c++) {
            for (int r = N - 1; r >= 0; r--) {
                if (b[r][c] == 0 && !wall.isEmpty()) {
                    b[r][c] = wall.poll();
                }
            }
        }
    }
}