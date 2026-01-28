package javaps.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

// 1865. 웜홀 (G3)
// 벨만-포드, 음수 사이클 판단
// O(VE)
class Edge {
    int start, end, cost;
    
    public Edge(int start, int end, int cost) {
      this.start = start;
      this.end = end;
      this.cost = cost;    
    }
}

public class Boj_1865_웜홀 {

  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringTokenizer st;
  static StringBuilder sb = new StringBuilder();
  static int T;
  static int V, E, W;
  static List<Edge> edges = new ArrayList<>();
  static long[] dist;
  static long INF = 10000 * 2500 + 1;
  public static void main(String[] args) throws IOException {
    T = nextInt();
    
    for (int t = 0; t < T; t++) {
      V = nextInt();
      E = nextInt();
      W = nextInt();
      
      edges = new ArrayList<>();
      dist = new long[V+1];
      Arrays.fill(dist, INF);

      for (int i = 0; i < E; i++) {
        int s = nextInt();
        int e = nextInt();
        int w = nextInt();
        edges.add(new Edge(s, e, w));
        edges.add(new Edge(e, s, w));
      }
      // 웜홀
      for (int i = 0; i < W; i++) {
        int s = nextInt();
        int e = nextInt();
        int w = nextInt();
        
        edges.add(new Edge(s, e, -w));
      }

      boolean ans = Belman(1); // 1로 먼저 돌려봄
      if (ans) {
        System.out.println("YES");
      } else {
        System.out.println("NO");
      }

      // if (ans) { // 사이클 있으면
      //   System.out.println("YES");
      // } else { 
      //   for (int i = 2; i < V+1; i++) {
      //     if (dist[i] == INF) { // 한 번도 간 적이 없으면 거기서도 벨만 돌려봄
      //       ans = Belman(i);
      //       if (ans) break;
      //     }
      //   }

      //   if (ans) {
      //     System.out.println("YES");
      //   } else {
      //     System.out.println("NO");
      //   }
      // }
    }
  }

  static boolean Belman(int start) {
    dist[start] = 0;
    for (int i = 0; i < V; i++) { // V-1번 + 1번 수행
      
      for (Edge edge : edges) {
        int cur = edge.start;
        int next = edge.end;
        int cost = edge.cost;

        if (dist[cur] + cost < dist[next]) {
          dist[next] = dist[cur] + cost;

          if (i == V-1) { // V번째 수행 때에 dist가 감소했다면
            return true; // 음수 사이클 있음
          }
        }
      }
    }
    return false;
  }

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