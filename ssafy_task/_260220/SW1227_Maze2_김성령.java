package ssafy_task._260220;

import java.io.*;
import java.util.*;
import java.awt.Point;

public class SW1227_Maze2_김성령 {

    static char[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        for (int t = 1; t < 11; t++) {
            String foo = br.readLine();
            board = new char[100][100];
            for (int i = 0; i < 100; i++) {
                board[i] = br.readLine().toCharArray();
            }

            int sr = 0; int sc = 0;
            for (int i = 0; i < 100; i++) {
                for (int j = 0; j < 100; j++) {
                    if (board[i][j] == '2') {
                        sr = i; sc = j;
                    }
                }
            }
            sb.append("#"+t+" "+bfs(new Point(sr, sc))+"\n");   
        }
        System.out.println(sb);
    }

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int bfs(Point start) {
        Deque<Point> dq = new ArrayDeque<>();
        dq.offer(start);
        board[start.x][start.y] = '1';

        while (!dq.isEmpty()) {
            Point now = dq.pollFirst();
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                
                if (0 > nx || nx >= 100 || 0 > ny || ny >= 100 || board[nx][ny] == '1')
                    continue;
                if (board[nx][ny] == '3') return 1;
                board[nx][ny] = '1';
                dq.offer(new Point(nx, ny));
            }
        }

        return 0;
    }
}
