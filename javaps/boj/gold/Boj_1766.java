package javaps.boj.gold;

import java.io.*;
import java.util.*;

// 1766. 문제집 (G2)
// 위상 정렬
public class Boj_1766 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String args[]) throws IOException {
		int V = nextInt();
		int E = nextInt();
		
		// indegree array
		int[] indegree = new int[V+1];
		List<List<Integer>> graph = new ArrayList<>();
		for (int i = 0; i < V+1; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		for (int i = 0; i < E; i++) {
			int s = nextInt();
			int e = nextInt();
			
			// (s, e)
			graph.get(s).add(e);
			indegree[e]++;
		}
		
		topologicalSort(V, graph, indegree);
		System.out.println(sb);
		
	}
	
	public static void topologicalSort(int V, List<List<Integer>> graph, int[] indegree) {
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		
		// 그래프의 시작점을 큐에 넣어줌
		for (int i = 1; i < V+1; i++) {
			if (indegree[i] == 0) {
				pq.offer(i); 
			}
		}
		
		while (!pq.isEmpty()) {
			int cur = pq.poll();
			sb.append(cur).append(" ");
			for (int next : graph.get(cur)) {
				indegree[next]--;
			
				if (indegree[next] == 0) {
					pq.offer(next);
				}
			}
		}
	}
	
	
	public static String next() throws IOException {
		while (st == null || !st.hasMoreTokens()) {
			String line = br.readLine();
			if (line == null) return null;
			st = new StringTokenizer(line);
		} return st.nextToken();
	}
	
	public static int nextInt() throws IOException {
		return Integer.parseInt(next());
	}
}
