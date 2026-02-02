package javaps.boj.gold;

import java.util.*;
import java.io.*;

// SSAFY 스터디 문제
// 15683. 감시 (G3)
// 시뮬레이션, 백트래킹, 깊은 복사
public class Boj_ssafy_15683 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] room;
    static int R, C;
    static int ans = 64;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static List<Node> cctvList;

    static class Node {
        int x, y, type;
        public Node(int x, int y, int type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }
    }

    static void cctv1(int x, int y, int dr, int[][] map) {
        while (true) {
            int nx = x + dx[dr];
            int ny = y + dy[dr];
            if (0 <= nx && nx < R && 0 <= ny && ny < C) { // 그래프에서 벗어나지 않았고
                if (map[nx][ny] == 6) // 벽이라면 리턴
                    return;
                else if (map[nx][ny] == -1) { // 이미 방문했다면 다음 칸으로
                    x = nx;
                    y = ny;
                    continue;
                } else { // 방문했거나 cctv라면 방문처리
                    x = nx;
                    y = ny;        
                    map[nx][ny] = -1;
                }
            } else { // 벗어나면 리턴
                return;
            }
        }
    }

    static void cctv2(int x, int y, int dr, int[][] map) {
        cctv1(x, y, dr, map);
        cctv1(x, y, (dr+2)%4, map);
    }

    static void cctv3(int x, int y, int dr, int[][] map) {
        cctv1(x, y, dr, map);
        cctv1(x, y, (dr+1)%4, map);
    }

    static void cctv4(int x, int y, int dr, int[][] map) {
        cctv1(x, y, dr, map);
        cctv1(x, y, (dr+1)%4, map);
        cctv1(x, y, (dr+2)%4, map);
    }

    static void cctv5(int x, int y, int dr, int[][] map) {
        cctv1(x, y, dr, map);
        cctv1(x, y, (dr+1)%4, map);
        cctv1(x, y, (dr+2)%4, map);
        cctv1(x, y, (dr+3)%4, map);
    }

    static void activateCCTV(Node node, int dr, int[][] map) {
        int x = node.x;
        int y = node.y;
        int type = node.type;
        switch (type) {
            case 1:
                cctv1(x, y, dr, map);
                break;
            case 2:
                cctv2(x, y, dr, map);
                break;
            case 3:
                cctv3(x, y, dr, map);
                break;
            case 4:
                cctv4(x, y, dr, map);
                break;
            case 5:
                cctv5(x, y, dr, map);
                break;
        }
    }

    static int[][] copyRoom(int[][] pastRoom) { // 깊은 복사
        int[][] copiedRoom = new int[R][C];
        for (int i = 0; i < R; i++) {
            copiedRoom[i] = pastRoom[i].clone();
        }
        return copiedRoom;
    }

    static void dfs(int depth, int[][] pastRoom) {
        if (depth == cctvList.size()) { // 모든 cctv를 다 보았다면
            int tmpSum = 0;
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (pastRoom[i][j] == 0) // 0의 개수를 세자. 
                        tmpSum++;
                }
            }

            ans = Math.min(ans, tmpSum); // ans의 최솟값을 갱신
            return;
        }

        Node nowCCTV = cctvList.get(depth);
        for (int dr = 0; dr < 4; dr++) {
            int[][] newRoom = copyRoom(pastRoom); // depth - 1의 room을 복사한 newRoom을 새로 만들고
            activateCCTV(nowCCTV, dr, newRoom); // 복제된 room 위에 현재(depth) cctv를 그리고
            dfs(depth+1, newRoom); // 복제된 room을 들고 다음 단계로 보냄
        }
    }

    public static void main(String args[]) throws IOException {
        R = nextInt();
        C = nextInt();
        cctvList = new ArrayList<>();

        room = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                room[i][j] = nextInt();
                if (room[i][j] != 0 && room[i][j] != 6)
                    cctvList.add(new Node(i, j, room[i][j]));
            }
        }
        int[][] pastRoom = copyRoom(room);
        dfs(0, pastRoom); // 백트래킹 시작

        System.out.println(ans);
    }

    // 입출력 매크로 
    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            String line = br.readLine();
            if (line == null) return null;
            st = new StringTokenizer(line);
        }
        return st.nextToken();
    }
    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
}