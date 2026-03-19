package ssafy_task.samsung_B;
import java.util.PriorityQueue;

class 커피점제과점_UserSolution {
    static final int MAX_V = 10005;
    static final int MAX_E = 65005;

    int[] head = new int[MAX_V];
    int[] next = new int[MAX_E];
    int[] to = new int[MAX_E];
    int[] weight = new int[MAX_E];
    int edgeCnt;
    int V;

    public void init(int N, int K, int[] sBuilding, int[] eBuilding, int[] mDistance) {
        V = N;
        edgeCnt = 0;
        for (int i = 0; i < N; i++) {
            head[i] = -1;
        }
        for (int i = 0; i < K; i++) {
            addEdge(sBuilding[i], eBuilding[i], mDistance[i]);
            addEdge(eBuilding[i], sBuilding[i], mDistance[i]);
        }
    }

    public void add(int sBuilding, int eBuilding, int mDistance) {
        addEdge(sBuilding, eBuilding, mDistance);
        addEdge(eBuilding, sBuilding, mDistance);
    }

    private void addEdge(int u, int v, int w) {
        to[edgeCnt] = v;
        weight[edgeCnt] = w;
        next[edgeCnt] = head[u];
        head[u] = edgeCnt++;
    }

    class Node implements Comparable<Node> {
        int v, w;
        public Node(int v, int w) {
            this.v = v;
            this.w = w;
        }
        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.w, o.w);
        }
    }

    public int calculate(int M, int[] mCoffee, int P, int[] mBakery, int R) {
        int[] distCof = new int[V];
        int[] distBak = new int[V];
        boolean[] isCoffee = new boolean[V];
        boolean[] isBakery = new boolean[V];

        for (int i = 0; i < V; i++) {
            distCof[i] = Integer.MAX_VALUE;
            distBak[i] = Integer.MAX_VALUE;
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();

        // 1. 커피점 시작 다익스트라
        for (int i = 0; i < M; i++) {
            int c = mCoffee[i];
            distCof[c] = 0;
            isCoffee[c] = true;
            pq.offer(new Node(c, 0));
        }

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (distCof[curr.v] < curr.w) continue;

            // 배열 기반 인접 리스트 탐색
            for (int e = head[curr.v]; e != -1; e = next[e]) {
                int nv = to[e];
                int nw = weight[e];
                int nextDist = curr.w + nw;

                if (nextDist <= R && distCof[nv] > nextDist) {
                    distCof[nv] = nextDist;
                    pq.offer(new Node(nv, nextDist));
                }
            }
        }

        for (int i = 0; i < P; i++) {
            int b = mBakery[i];
            distBak[b] = 0;
            isBakery[b] = true;
            pq.offer(new Node(b, 0));
        }

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (distBak[curr.v] < curr.w) continue;

            for (int e = head[curr.v]; e != -1; e = next[e]) {
                int nv = to[e];
                int nw = weight[e];
                int nextDist = curr.w + nw;

                if (nextDist <= R && distBak[nv] > nextDist) {
                    distBak[nv] = nextDist;
                    pq.offer(new Node(nv, nextDist));
                }
            }
        }

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < V; i++) {
            if (isCoffee[i] || isBakery[i]) continue;

            if (distCof[i] <= R && distBak[i] <= R) {
                ans = Math.min(ans, distCof[i] + distBak[i]);
            }
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}