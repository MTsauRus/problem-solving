package ssafy_task._260311;
import java.io.*;
import java.util.*;
/*
    이 문제는 N = 1000인 완전 그래프임. 따라서 크루스칼이나 PQ를 활용한 프림은
    오히려 비효율적임. 객체를 따로 생성하지 않고 dist 배열을 활용하여 최적화한
    O(N^2) 프림을 사용하는 것이 가장 효율적임
*/
public class SW1251_Hanaro_prim최적화복습 {
  
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            int N = Integer.parseInt(br.readLine());
            int[] xPos = new int[N];
            int[] yPos = new int[N];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                xPos[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                yPos[i] = Integer.parseInt(st.nextToken());
            }
            double feeRate = Double.parseDouble(br.readLine());

            boolean[] visited = new boolean[N];
            long[] dist = new long[N];

            Arrays.fill(dist, Long.MAX_VALUE);

            int nodeCnt = 0;
            dist[0] = 0; // 임의의 시작 노드 0
            long globalSum = 0l;
            while (nodeCnt < N) {
                long localMin = Long.MAX_VALUE;
                int nowNode = -1;

                for (int i = 0; i < N; i++) {
                    // 현재 가장 가까운 노드 선택
                    if (!visited[i] && localMin > dist[i]) {
                        localMin = dist[i];
                        nowNode = i;
                    }
                }
                // MST를 만들 수 없는 경우
                if (nowNode == -1) break;

                // 방문처리 후 sum++
                visited[nowNode] = true;
                globalSum += dist[nowNode];
                nodeCnt++;

                // MST에 포함되지 않는 노드의 최솟값 업데이트
                for (int i = 0; i < N; i++) {
                    if (!visited[i]) {
                        long dx = xPos[i] - xPos[nowNode];
                        long dy = yPos[i] - yPos[nowNode];
                        long nowDist = dx*dx + dy*dy;

                        if (dist[i] > nowDist) {
                            dist[i] = nowDist;
                        }
                    }
                }
            }

            sb.append("#" + t + " " + Math.round(globalSum*feeRate) + "\n");
        }
        System.out.println(sb);
    }
}
