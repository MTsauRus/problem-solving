package ssafy_task._260202;

import java.util.*;
import java.io.*;

public class SW1226_Maze1_김성령 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[][] maze;

    public static class Node {
        int x;
        int y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException {
        for (int t = 1; t < 11; t++) {
            int foo = Integer.parseInt(br.readLine());
            maze = new int[16][16];

            for (int i = 0; i < 16; i++) {
                char[] tmpArr = br.readLine().toCharArray();
                for (int j = 0; j < 16; j++) {
                    maze[i][j] = tmpArr[j] - '0';
                }
            }
            sb.append("#").append(t).append(" ");
            sb.append(bfs()).append("\n");
        }
        System.out.println(sb);
    }

    static int bfs() {
        Deque<Node> dq = new ArrayDeque<>();
        dq.offer(new Node(1,1));

        while (!dq.isEmpty()) {
            Node now = dq.poll();
            
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (0 <= nx && nx < 16 && 0 <= ny && ny < 16) {
                    if (maze[nx][ny] == 3) {
                        return 1;
                    } else if (maze[nx][ny] == 0) {
                        maze[nx][ny] = -1;
                        dq.offer(new Node(nx, ny));
                    } else {
                        continue;
                    }
                }
                
            }
        }
        return 0;
    }
}
