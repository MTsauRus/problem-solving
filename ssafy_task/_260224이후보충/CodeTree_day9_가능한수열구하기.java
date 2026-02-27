package ssafy_task._260224이후보충;

import java.io.*;
import java.util.*;

public class CodeTree_day9_가능한수열구하기 {
    static int[] ansList;
    static int[] realAns;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        ansList = new int[n];
        realAns = new int[n];
        if (n == 1) System.out.println(4);
        else if (n == 2) System.out.println(45);
        else {
            dfs(0, n);
            for (int i = 0; i < n; i++) {
                System.out.print(realAns[i]);
            }
        }
    }


    static void dfs(int depth, int n) {
        if (realAns[0] != 0) return;

        if (depth == n) {
            realAns = ansList.clone();
            return;
        }

        for (int i = 4; i <= 6; i++) {
            ansList[depth] = i;
            int idx = depth;
            boolean cont = false;
            for (int len = 1; len <= (depth+1)/2; len++) {
                boolean diff = false;
                for (int j = idx; j <= depth; j++) {
                    if (ansList[j] != ansList[j-len]) {
                        diff = true;
                        break;
                    }
                }
                if (!diff) { // 같다면
                    cont = true;
                }
                idx--;
            }
            if (cont) continue;

            dfs(depth+1, n);
        }
    }
}
