package ssafy_task._260210;

import java.util.*;
import java.io.*;
// map의 key를 String으로 변환하여 사용

// 구현 풀이
public class SW5648_AtomicExtinction_김성령 {
    static int N;
    static List<Integer[]> atomList;
    static int ans;
    static int[][] map = new int[4001][4001];

    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    static class Unit {
        int x, y, dir, e;
        public Unit(int x, int y, int dir, int e) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.e = e;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            atomList = new ArrayList<>();
            ans = 0;

            ArrayDeque<Unit> dq = new ArrayDeque<>();

            for (int i  = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int x = (Integer.parseInt(st.nextToken())+1000)*2;
                int y = (Integer.parseInt(st.nextToken())+1000)*2;
                int d = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                
                map[y][x] = e;
                dq.addLast(new Unit(x, y, d, e));
            }
    
            while (!dq.isEmpty()) {
                Unit cur = dq.pollFirst();

                // 충돌 확인
                if (map[cur.y][cur.x] != cur.e) {
                    ans += map[cur.y][cur.x];
                    map[cur.y][cur.x] = 0;
                    continue;
                }
                // 충돌하지 않았으면 다음 방향에 기록 후 덱에 넣기
                map[cur.y][cur.x] = 0;
                int nx = cur.x+dx[cur.dir];
                int ny = cur.y+dy[cur.dir];
                if (nx>=0&&nx<=4000&&ny>=0&&ny<=4000) {
                    cur.x = nx;
                    cur.y = ny;
                    map[cur.y][cur.x] += cur.e;
                    dq.addLast(cur);
                }
            }
            System.out.println("#" + t + " " + ans);
        }
    }
}
