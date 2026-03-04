package ssafy_task._260224이후보충;
import java.io.*;
import java.util.*;

public class CodeTree_day7_쌓인숫자의순차적이동 {
    
    static int N, M;
    static Deque<Integer>[][] dqList;
    static int[] moves;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        dqList = new ArrayDeque[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dqList[i][j] = new ArrayDeque<>();
            }
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                dqList[i][j].offer(Integer.parseInt(st.nextToken()));
            }
        }

        moves = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            moves[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < M; i++) {
            int nextMove = moves[i];
            // 위치 찾고 이동하기
            move(nextMove);
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (dqList[i][j].isEmpty()) {
                    sb.append("None"+"\n");
                } else {
                    while (!dqList[i][j].isEmpty()) {
                        sb.append(dqList[i][j].pollFirst() + " ");
                    }
                    sb.append("\n");
                }
            }
        }

        System.out.println(sb);
    }

    static int[] dr = {-1, -1, -1, 0, 1, 1, 1, 0};
    static int[] dc = {-1, 0, 1, 1, 1, 0, -1, -1};

    static void move(int nextMove) {
        boolean breakFlag = false;
        int r = 0; int c = 0; int fromIdx = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int tmpIdx = 0;
                for (int now : dqList[i][j]) {
                    if (now == nextMove) {
                        breakFlag = true;
                        r = i; c = j; fromIdx = tmpIdx;
                        break;
                    }
                    tmpIdx++;
                }
                if (breakFlag) break;
            }
        if (breakFlag) break;
        }

        int localMax = 0; int mr = 0; int mc = 0;
        for (int i = 0; i < 8; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

            for (int next : dqList[nr][nc]) {
                if (next > localMax) {
                    localMax = next;
                    mr = nr; mc = nc; 
                }
            }
        }

        if (localMax == 0) return;

        Deque<Integer> moveDq = new ArrayDeque<>();
        while (fromIdx-->=0) {
            moveDq.offer(dqList[r][c].pollFirst());
        }

        while (!moveDq.isEmpty()) {
            dqList[mr][mc].offerFirst(moveDq.pollLast());
        }
    }
}
