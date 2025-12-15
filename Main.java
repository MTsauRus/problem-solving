import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());

            int[][] ranks = new int[N][2];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                ranks[i][0] = Integer.parseInt(st.nextToken());
                ranks[i][1] = Integer.parseInt(st.nextToken());
                
            }

            Arrays.sort(ranks, (o1, o2) -> o1[0] - o2[0]); // 오름차순. 음수 시 앞에 둠
            int ans = 1;
            int minInterview = ranks[0][1];

            for (int i = 1; i < N; i++) {
                if (ranks[i][1] < minInterview) {
                    ans++;
                    minInterview = ranks[i][1];
                }
            }
            System.out.println(ans);
        }
    }
}