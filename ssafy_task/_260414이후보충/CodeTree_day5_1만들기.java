package ssafy_task._260414이후보충;
import java.io.*;
import java.util.*;

public class CodeTree_day5_1만들기 {
    static class Node implements Comparable<Node> {
        int depth, num;
        public Node(int depth, int num) {
            this.depth = depth;
            this.num = num;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.depth, o.depth);
        }
    }
    static int N;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        visited = new boolean[N+1];
        visited[N] = true;

        int ans = bfs(new Node(0, N));
        System.out.println(ans);
    }

    static int bfs(Node start) {
        Deque<Node> dq = new ArrayDeque<>();
        dq.offer(start);

        while (!dq.isEmpty()) {
            Node now = dq.poll();
            if (now.num == 1) return now.depth;

            if (now.num % 3 == 0 && !visited[now.num/3]) {
                visited[now.num/3] = true;
                dq.offer(new Node(now.depth+1, now.num/3));
            }
            
            if (now.num % 2 == 0 && !visited[now.num/2]) {
                visited[now.num/2] = true;
                dq.offer(new Node(now.depth+1, now.num/2));
            }

            if (now.num + 1 < N*2 && !visited[now.num+1]) {
                visited[now.num+1] = true;
                dq.offer(new Node(now.depth+1, now.num + 1));
            }

            if (now.num - 1 >= 0 && !visited[now.num-1]) {
                visited[now.num - 1] = true;
                dq.offer(new Node(now.depth+1, now.num - 1));
            }

        }
        return 0;
    }
}

