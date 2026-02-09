package ssafy_task._260206;

import java.util.*;
import java.io.*;

public class codeTree_ROG마을 {

    static int N, A, ans;
    static int r, c, goalX, goalY;
    static int[][] board;
    static int[][] dist;
    static boolean[][][] visited;

    static class Node {
        int x, y, time, color;
        Node(int time, int x, int y) { // time: 이 노드가 선택되었을 때의 시간
        this.time = time;
        this.x = x;
        this.y = y;

        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken());
        ans = 0;
        board = new int[N][N];
        dist = new int[N][N];
        visited = new boolean[3*A][N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken())-1;
        c = Integer.parseInt(st.nextToken())-1;
        st = new StringTokenizer(br.readLine());
        goalX = Integer.parseInt(st.nextToken())-1;
        goalY = Integer.parseInt(st.nextToken())-1;
        
        System.out.println(bfs());
    }

    static int[] dr = {1, -1, 0, 0, 0}; 
    static int[] dc = {0, 0, 1, -1, 0};
    static int bfs() {
        Deque<Node> dq = new ArrayDeque<>();
        dq.offer(new Node(0, r,c));
        visited[0][r][c] = true;
        while (!dq.isEmpty()) {
            Node now = dq.pollFirst();
            for (int i = 0; i < 5; i++) {
                int nt = now.time + 1;
                int nx = now.x+dr[i];
                int ny = now.y+dc[i];

                if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nt%(3*A)][nx][ny]) {

                    if (board[nx][ny] == 0) continue; // 맨 처음 벽이었으면 넘김

                    // 처음이 길이었으면 무조건 길, 오랜지였으면 시간에 따른 변화
                    int color = (board[nx][ny] == 2) ? 2 : (board[nx][ny] + nt/A%3)%3;
                    if (nx == goalX && ny == goalY) {
                        return nt;
                    }

                    if (i == 4) {
                        visited[nt%(3*A)][nx][ny] = true;
                        dq.offer(new Node(nt, nx, ny));
                    } else {
                        if (color == 2) {
                            visited[nt%(3*A)][nx][ny] = true;
                            dq.offer(new Node(nt, nx, ny));
                        }
                    }
                }
            }
        }
        return -1;
    }
}
