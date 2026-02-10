package ssafy_task._260205;
import java.util.*;
import java.io.*;

// 맨하탄 거리
public class codeTree_금채굴하기 {


    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int value = Integer.parseInt(st.nextToken());
        
        List<Point> golds = new ArrayList<>();
        
        int[][] grid = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int next = Integer.parseInt(st.nextToken());
                if (next == 1) {
                    golds.add(new Point(i, j));
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int[] tmpGolds = new int[2*N]; // idx: 현재 점에서 금까지의 거리. value: 금 갯수
                for (Point gold : golds) {
                    tmpGolds[Math.abs(i - gold.x) + Math.abs(j - gold.y)]++;
                }
                for (int k = 0; k < 2*N; k++) {
                    if (tmpGolds[k] >= 1) { // k 마름모 크기에 금이 존재한다면
                        int goldCount = 0; // 0부터 k 거리까지의 금 개수를 세고
                        for (int w = 0; w <= k; w++) {
                            goldCount += tmpGolds[w];
                        }
                        if ((k*k + (k+1) * (k+1)) <= value * goldCount) { // 손해를 보지 않는다면
                            ans = Math.max(ans, goldCount); // 금 개수 업데이트
                        }
                    }
                }
            }
        }
        System.out.println(ans);
    }
}
