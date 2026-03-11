package ssafy_task.samsung_B;
import java.util.*;

class UserSolution {
    
    // 우선순위 큐에 넣을 간선 객체. 
    // 최대 힙(Max-Heap)으로 쓰기 위해 Comparable 구현!
    static class Edge implements Comparable<Edge> {
        int to, weight;
        
        public Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
        
        @Override
        public int compareTo(Edge o) {
            // 최대 하중을 먼저 꺼내야 하니까 내림차순 정렬
            return Integer.compare(o.weight, this.weight);
        }
    }
    
    int n;
    List<Edge>[] graph;

    public void init(int N, int K, int[] sCity, int[] eCity, int[] mLimit) {
        this.n = N;
        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }
        
        // 양방향 그래프 초기 세팅
        for (int i = 0; i < K; i++) {
            graph[sCity[i]].add(new Edge(eCity[i], mLimit[i]));
            graph[eCity[i]].add(new Edge(sCity[i], mLimit[i]));
        }
    }

    public void add(int sCity, int eCity, int mLimit) {
        graph[sCity].add(new Edge(eCity, mLimit));
        graph[eCity].add(new Edge(sCity, mLimit));
    }

    public int calculate(int sCity, int eCity, int M, int[] mStopover) {
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        
        // mLimit 최대값이 30000이므로 30005 정도면 무한대(INF) 역할로 충분함
        int INF = 30005; 
        dist[sCity] = INF;
        pq.offer(new Edge(sCity, INF));
        
        // 시작점 S에서 한 번만 다익스트라 실행 (최대 중량 경로 탐색)
        while (!pq.isEmpty()) {
            Edge curr = pq.poll();
            int cv = curr.to;
            int cw = curr.weight;
            
            // 이미 더 큰 중량으로 갱신된 옛날 정보면 빠르게 스킵 (효율성 핵심)
            if (dist[cv] > cw) continue;
            
            for (Edge next : graph[cv]) {
                // 현재까지의 병목과 다음 다리의 중량 중 더 작은 값이 새로운 병목
                int nextLimit = Math.min(cw, next.weight);
                
                // 새로운 병목이 기존에 알던 값보다 더 크면 갱신
                if (nextLimit > dist[next.to]) {
                    dist[next.to] = nextLimit;
                    pq.offer(new Edge(next.to, nextLimit));
                }
            }
        }
        
        // 최종 정답 구하기 (S에서 각 목적지까지 가는 경로의 병목들 중 최솟값)
        int ans = dist[eCity];
        if (ans == -1) return -1; // 도착지도 못 가면 바로 아웃
        
        for (int i = 0; i < M; i++) {
            if (dist[mStopover[i]] == -1) {
                return -1; // 경유지 중 하나라도 길이 끊겨 있으면 -1
            }
            ans = Math.min(ans, dist[mStopover[i]]);
        }
        
        return ans;
    }
}