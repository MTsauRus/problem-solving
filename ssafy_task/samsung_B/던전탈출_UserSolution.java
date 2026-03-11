package ssafy_task.samsung_B;

import java.util.*;

class 던전탈출_UserSolution {
	static int[][] board;
	static int N, gateCnt;
	static int hp;
	static Gate[] gateList;
	static boolean[] isValid;
	static boolean[] visited;
	static List<Node>[] graphList;

	static class Gate {
		int r, c;
		public Gate(int r, int c) {
			this.r = r; this.c = c;
		}
	}

	static class Node implements Comparable<Node>{
		int gateNum, d;
		public Node(int gateNum, int d) {
			this.gateNum = gateNum;
			this.d = d;
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.d, o.d);
		}
	}

	static class Point {
		int r, c, t;
		Point(int r, int c, int t) {
			this.r = r;
			this.c = c;
			this.t = t;
		}
	}
	void init(int n, int mMaxStamina, int mMap[][]) {
		board = mMap;
		N = n;
		hp = mMaxStamina;
		gateCnt = 0;
		gateList = new Gate[201];
		isValid = new boolean[201];
		graphList = new ArrayList[201];

		return;
	}

	void addGate(int mGateID, int mRow, int mCol) {
		gateCnt++;
		gateList[mGateID] = new Gate(mRow, mCol);
		isValid[mGateID] = true;
		// 게이트 음수로 저장
		board[mRow][mCol] = -mGateID;
		// 게이트 추가될때마다 bfs 한번씩 돌리기
		boolean[][] tmpVisited = new boolean[N][N];
		Deque<Point> dq = new ArrayDeque<>();
		dq.offer(new Point(mRow, mCol, 0));
		int[] dr = {1, -1, 0, 0};
		int[] dc = {0, 0, 1, -1};
		tmpVisited[mRow][mCol] = true;

		while (!dq.isEmpty()) {
			Point now = dq.pollFirst();
			if (now.t == hp) break; // 최대 체력까지만 bfs를 돌 수 있다.
			
			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];

				if (nr<0||nc<0||nr>=N||nc>=N||tmpVisited[nr][nc]) continue;
				if (board[nr][nc] == 1) continue;
				if (board[nr][nc] < 0) { // 게이트를 만났다면
					// 현재 bfs의 거리를 저장해주자 (양방향)
					if (graphList[mGateID] == null) 
						graphList[mGateID] = new ArrayList<Node>();
					graphList[mGateID].add(new Node(-board[nr][nc], now.t+1));
					if (graphList[-board[nr][nc]] == null)
						graphList[-board[nr][nc]] = new ArrayList<Node>();
					graphList[-board[nr][nc]].add(new Node(mGateID, now.t+1));
					tmpVisited[nr][nc] = true;
					dq.offer(new Point(nr, nc, now.t+1));
					continue; 
				}
				// 그냥 길인 경우
				dq.offer(new Point(nr, nc, now.t+1));
				tmpVisited[nr][nc] = true;
			}
		}
		return;
	}

	void removeGate(int mGateID) {
		Gate removal = gateList[mGateID];
		board[removal.r][removal.c] = 0;
		gateList[mGateID] = null;
		isValid[mGateID] = false;
		return;
	}

	int getMinTime(int mStartGateID, int mEndGateID) {
		visited = new boolean[201];
		Gate start = gateList[mStartGateID];
		Gate end = gateList[mEndGateID];
		
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.offer(new Node(mStartGateID, 0));
		int[] dist = new int[201];
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[mStartGateID] = 0;

		while (!pq.isEmpty()) {
			Node now = pq.poll();
			// 옛날정보 스킵
			if (dist[now.gateNum] < now.d) continue; 
			if (now.gateNum == mEndGateID) { // 종료게이트라면
				return dist[mEndGateID];
			}
			visited[now.gateNum] = true;

			// 다음 현재 노드에서 다음으로 갈 방법이 없다면 넘기기
			if (graphList[now.gateNum] == null) continue;
			// 연결된 다음 노드를 보자
			for (Node next : graphList[now.gateNum]) {
				// 이미 방문했거나 삭제된 게이트라면 넘김
				if (visited[next.gateNum] || !isValid[next.gateNum]) continue;
				int nextDist = dist[now.gateNum] + next.d;
				if (dist[next.gateNum] > nextDist) {
					dist[next.gateNum] = nextDist;
					pq.offer(new Node(next.gateNum, nextDist));
				}
			}
		}
		return -1;
	}
}