package ssafy_task._260311;
import java.io.*;
import java.util.*;
/*
    이 문제는 N = 1000인 완전 그래프임. 따라서 크루스칼이나 PQ를 활용한 프림은
    오히려 비효율적임. 객체를 따로 생성하지 않고 dist 배열을 활용하여 최적화한
    O(N^2) 프림을 사용하는 것이 가장 효율적임
*/
public class SW1251_Hanaro_prim최적화 {
  
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
            double ans = 0.0;

            boolean[] visited = new boolean[N];
            // mst를 구성하지 않는 노드 중 가장 가까운 노드
            double[] dist = new double[N];
            Arrays.fill(dist, Double.MAX_VALUE);

            int cnt = 0;
            dist[0] = 0.0; // 임의의 시작 노드
            
            while (cnt++ < N) {
                double localMin = Double.MAX_VALUE;
                int now = 0;
                // 최소 weight를 가진 노드 탐색
                for (int i = 0; i < N; i++) {
                    if (!visited[i] && dist[i] < localMin) {
                        localMin = dist[i];
                        now = i;
                    }

                }
                ans += localMin;
                visited[now] = true;

                for (int i = 0; i < N; i++) {
                    if (!visited[i]) {
                        long dx = xPos[now]-xPos[i];
                        long dy = yPos[now]-yPos[i];

                        double localFee = (dx*dx+dy*dy)*feeRate;

                        if (dist[i] > localFee) {
                            dist[i] = localFee;
                        }
                    }
                }
            }
            sb.append("#" + t + " " + Math.round(ans) + "\n");
        }
        System.out.println(sb);
    }
}
