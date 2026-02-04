package ssafy_task._260204;

import java.util.*;
import java.io.*;

public class SW6808_CardGame_김성령 {

    static int aWin = 0;
    static int aLose = 0;
    static boolean[] visited;
    static List<Integer> aNums;
    static List<Integer> bNums;
    

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            aWin = 0;
            aLose = 0;
            visited = new boolean[9];
            boolean[] taken = new boolean[19];
            st = new StringTokenizer(br.readLine());
            aNums = new ArrayList<>(9);
            bNums = new ArrayList<>(9);
            
            for (int i = 0; i < 9; i++) {
                int a = Integer.parseInt(st.nextToken());
                aNums.add(a);
                taken[a] = true;
            }

            
            for (int i = 1; i < 19; i++) {
                if (!taken[i]) bNums.add(i);
            }
            
            makePerm(0, new ArrayList<Integer>());
            sb.append("#").append(t).append(" ").append(aWin).append(" ").append(aLose).append("\n");
        }
        System.out.println(sb);
    }


    static void makePerm(int depth, List<Integer> perms) {
        if (depth == 9) {
            game(perms, aNums, bNums);
            return;
        }

        for (int i = 0; i < 9; i++) {
            if (!visited[i]) {
                visited[i] = true;
                perms.add(i);
                makePerm(depth + 1, perms);
                perms.remove(depth); // 원상복귀
                visited[i] = false;
            }
        }
    }


    static void game(List<Integer> arr, List<Integer> given, List<Integer> remains) {
        int aScore = 0;
        int bScore = 0;
        for (int i = 0; i < 9; i++) {
            int now = arr.get(i);
            if (given.get(i) > remains.get(now)) {
                aScore += given.get(i) + remains.get(now);
            } else {
                bScore += given.get(i) + remains.get(now);
            }
        }

        if (aScore > bScore) aWin++;
        else if (aScore < bScore) aLose++;
    }
}
