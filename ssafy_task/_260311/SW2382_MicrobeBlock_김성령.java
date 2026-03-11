package ssafy_task._260311;

import java.util.*;
import java.io.*;

public class SW2382_MicrobeBlock_김성령 {
    static int N, M, K;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int[][] board;
    static Node[] nodeList;
    static boolean[] isMerged;

    static class Node implements Comparable<Node> {
        int i, r, c, n, dir;
        public Node(int i, int r, int c, int n, int dir) {
            this.i = i;
            this.r = r;
            this.c = c;
            this.n = n;
            this.dir = dir;
        }

        @Override
        public int compareTo(Node o) {
            // 내림차순 정렬
            return Integer.compare(o.n, this.n);
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());    
            M = Integer.parseInt(st.nextToken());    
            K = Integer.parseInt(st.nextToken());    

            board = new int[N][N];

            // nodeList의 0번 인덱스는 사용하지 않음. (board와의 충돌 회피)
            nodeList = new Node[K+1];
            // 병합 여부 판단 배열
            isMerged = new boolean[K+1];
            for (int i = 1; i <= K; i++) {
                st = new StringTokenizer(br.readLine());
                nodeList[i] = new Node(
                    i, 
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())-1
                );
            }

            // M번 반복
            while (M-->0) {
                PriorityQueue<Node> pq = new PriorityQueue<>();
                // board 청소 + pq초기화
                for (int i = 1; i <= K; i++) {
                    if (isMerged[i]) continue;
                    Node now = nodeList[i];
                    board[now.r][now.c] = 0;
                    // 살아있는 미생물을 pq에 넣음
                    pq.offer(now);
                }

                // 모든 미생물 순회
                while (!pq.isEmpty()) {
                    Node now = pq.poll();
                    int nr = now.r + dr[now.dir];
                    int nc = now.c + dc[now.dir];
                    
                    // 약물을 밟았다면
                    if (nr == 0 || nc == 0 || nr == N-1 || nc == N-1) {
                        // 방향을 반대로 전환하고 수를 절반으로
                        now.dir ^= 1;
                        now.n /= 2;
                        now.r = nr;
                        now.c = nc;
                        if (now.n == 0) { // 미생물 다 죽었으면 삭제
                            isMerged[now.i] = true;
                            board[now.r][now.c] = 0;
                        }
                        // 약물에서 겹칠 일은 없으므로 board 처리 생략

                    } else { // 일반 이동
                        now.r = nr;
                        now.c = nc;
                        // 이미 누가 있다면
                        if (board[nr][nc] != 0) {
                            Node opp = nodeList[board[nr][nc]];
                            isMerged[now.i] = true;
                            opp.n += now.n;
                        }
                         else {
                            board[nr][nc] = now.i;
                        }
                    }
                }
            }

            int ans = 0;
            for (int i = 1; i <= K; i++) {
                if (isMerged[i]) continue;
                Node now = nodeList[i];
                ans += now.n;
            }

            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }    
}
