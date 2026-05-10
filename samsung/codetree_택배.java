package samsung;

import java.io.*;
import java.util.*;

public class codetree_택배 {
    static int N, M;
    static int[][] board;
    static Map<Integer, int[]> boxes = new TreeMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        board = new int[N][N];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken())-1;
            dropBox(k, h, w, c);

        }

        boolean flag = true;
        while (M-->0) {
            if (flag) {
                leftOut();
                gravity();
                flag = false;
            } else {
                rightOut();
                gravity();
                flag = true;
            }
        }
    }

    static void dropBox(int k, int h, int w, int c) {
        int bottom = N-1;
        for (int j = c; j < c+w; j++) { // c~c+w
            for (int i = 0; i < N; i++) {
                // 바닥 찾기
                if (board[i][j] != 0) {
                    bottom = Math.min(bottom, i-1);
                    break;
                }
            }
        }

        int top = bottom - h + 1;
        for (int i = top; i <= bottom; i++) {
            for (int j = c; j < c+w; j++) {
                board[i][j] = k;
            }
        }
        // 맨 위, 왼쪽열, h, w
        boxes.put(k, new int[]{top, c, h, w});
    }
}


/**
 * 
 * import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] board;
    static Map<Integer, int[]> boxes = new TreeMap<>(); // k -> [topRow, leftCol, h, w]

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken()) - 1; // 0-indexed
            dropBox(k, h, w, c);
        }

        boolean left = true;
        while (!boxes.isEmpty()) {
            // TreeMap이라 keySet()이 k 오름차순 → 첫 번째 removable이 최소 k
            int target = -1;
            for (int k : boxes.keySet()) {
                if (left ? canRemoveLeft(k) : canRemoveRight(k)) {
                    target = k;
                    break;
                }
            }
            removeBox(target);
            gravity();
            sb.append(target).append('\n');
            left = !left;
        }

        System.out.print(sb);
    }

    static void dropBox(int k, int h, int w, int c) {
        // 각 열에서 첫 번째 장애물 찾아 bottom 결정
        int bottom = N - 1;
        for (int j = c; j < c + w; j++) {
            for (int i = 0; i < N; i++) {
                if (board[i][j] != 0) {
                    bottom = Math.min(bottom, i - 1);
                    break;
                }
            }
        }
        int top = bottom - h + 1;
        for (int i = top; i <= bottom; i++)
            for (int j = c; j < c + w; j++)
                board[i][j] = k;
        boxes.put(k, new int[]{top, c, h, w});
    }

    static boolean canRemoveLeft(int k) {
        int[] b = boxes.get(k);
        int r = b[0], c = b[1], h = b[2];
        // 박스가 차지하는 모든 행에서, 왼쪽 영역에 다른 택배 없으면 OK
        for (int i = r; i < r + h; i++)
            for (int j = 0; j < c; j++)
                if (board[i][j] != 0) return false;
        return true;
    }

    static boolean canRemoveRight(int k) {
        int[] b = boxes.get(k);
        int r = b[0], c = b[1], h = b[2], w = b[3];
        for (int i = r; i < r + h; i++)
            for (int j = c + w; j < N; j++)
                if (board[i][j] != 0) return false;
        return true;
    }

    static void removeBox(int k) {
        int[] b = boxes.get(k);
        int r = b[0], c = b[1], h = b[2], w = b[3];
        for (int i = r; i < r + h; i++)
            for (int j = c; j < c + w; j++)
                board[i][j] = 0;
        boxes.remove(k);
    }

    static void gravity() {
        // ★ 바닥에 가까운(bottom row가 큰) 택배부터 먼저 처리
        List<Integer> keys = new ArrayList<>(boxes.keySet());
        keys.sort((a, b) -> {
            int[] ba = boxes.get(a), bb = boxes.get(b);
            return Integer.compare((bb[0] + bb[2] - 1), (ba[0] + ba[2] - 1));
        });

        for (int k : keys) {
            int[] box = boxes.get(k);
            int r = box[0], c = box[1], h = box[2], w = box[3];

            // 1. 보드에서 임시 제거
            for (int i = r; i < r + h; i++)
                for (int j = c; j < c + w; j++)
                    board[i][j] = 0;

            // 2. 현재 bottom 아래에서 장애물 탐색
            int bottom = N - 1;
            for (int j = c; j < c + w; j++) {
                for (int i = r + h; i < N; i++) {
                    if (board[i][j] != 0) {
                        bottom = Math.min(bottom, i - 1);
                        break;
                    }
                }
            }
            bottom = Math.max(bottom, r + h - 1); // 위로는 못 올라감

            // 3. 새 위치에 배치
            box[0] = bottom - h + 1;
            for (int i = box[0]; i <= bottom; i++)
                for (int j = c; j < c + w; j++)
                    board[i][j] = k;
        }
    }
}
 */