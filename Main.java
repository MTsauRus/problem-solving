import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        Queue<Integer> leftHeap = new PriorityQueue<>(Collections.reverseOrder()); // 최대 힙
        Queue<Integer> rightHeap = new PriorityQueue<>(); // 최소 힙, 디폴트

        for (int i = 0; i < N; i++) {
            int nextNum = Integer.parseInt(br.readLine());

            if (leftHeap.size() == rightHeap.size()) { // 힙 크기가 같은 경우 왼쪽 힙에 넣음
                leftHeap.offer(nextNum); // 파이썬과 달리 처음 선언할 때 최대 힙으로 선언했으므로 음수 안넣어도 됨
            } else {
                rightHeap.offer(nextNum);
            }
            
            // 순서가 바뀌어 들어갔다면
            if (!rightHeap.isEmpty() && rightHeap.peek() < leftHeap.peek()) {
                rightHeap.offer(leftHeap.poll());
                leftHeap.offer(rightHeap.poll());
            }
        sb.append(leftHeap.peek()).append('\n');
        }
        System.out.println(sb);
    }
}