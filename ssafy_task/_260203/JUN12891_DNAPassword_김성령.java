package ssafy_task._260203;
import java.util.*;
import java.io.*;


public class JUN12891_DNAPassword_김성령 {

    static final int A = 0;
    static final int C = 2;
    static final int G = 6;
    static final int T = 19;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int ans = 0;
        Deque<Integer> window = new ArrayDeque<>();

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int len = Integer.parseInt(st.nextToken());

        char[] dna = br.readLine().toCharArray();
        int[] cnt = new int[26];
        int[] goal = new int[4];

        String[] tmp = br.readLine().split(" ");
        for (int i = 0; i < 4; i++) 
            goal[i] = Integer.parseInt(tmp[i]);

        for (int i = 0; i < len; i++) { // 첫 윈도우 채우고 검사
            window.offer(dna[i] - 'A');
            cnt[dna[i] - 'A']++;
        }

        if (cnt[A] >= goal[0] && cnt[C] >= goal[1] && cnt[G] >= goal[2] && cnt[T] >= goal[3])
            ans++;

        for (int i = len; i < N; i++) { // --> 슬라이딩 윈도우 -->
            cnt[window.pollFirst()]--;
            cnt[dna[i] - 'A']++;
            window.offerLast(dna[i] - 'A');
            if (cnt[A] >= goal[0] && cnt[C] >= goal[1] && cnt[G] >= goal[2] && cnt[T] >= goal[3])
                ans++;
        }

        System.out.println(ans);
    }
}
