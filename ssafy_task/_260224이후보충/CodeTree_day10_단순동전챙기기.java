package ssafy_task._260224이후보충;

import java.util.*;
import java.io.*;

public class CodeTree_day10_단순동전챙기기 {
    static char[][] board;
    static int r, c, er, ec;
    static int[][] dist;
    static Node[] locate;
    static boolean[] isValid;
    static int ans = -1;

    static class Node {
        int x;
        int y;
        Node (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        board = new char[N][N];

        dist = new int[11][11];
        locate = new Node[11];
        isValid = new boolean[11];
        isValid[0] = true;
        isValid[10] = true;
        int valNum = 0;

        for (int i = 0; i < N; i++) {
            board[i] = br.readLine().toCharArray();
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 'S') {
                    locate[0] = new Node(i, j);
                } else if (board[i][j] == 'E') {
                    locate[10] = new Node(i, j);
                } else if (board[i][j] == '.') {
                    continue; 
                } else {
                    int nowNum = board[i][j] - '0';
                    locate[nowNum] = new Node(i, j);
                    isValid[nowNum] = true;
                    valNum++;
                }
            }
        }

        for (int i = 0; i <= 9; i++) {
            if (!isValid[i]) continue;
            for (int j = i+1; j <= 10; j++) {
                if (!isValid[j]) continue;
                dist[i][j] = Math.abs(locate[i].x-locate[j].x) + Math.abs(locate[i].y-locate[j].y);
            }
        }

        if (valNum <= 2) System.out.println(ans);
        else {
            ans = 1000000;
            int[] possibleNum = new int[valNum];
            int idx = 0;
            for (int i = 1; i <= 9; i++) {
                if (isValid[i]) {
                    possibleNum[idx++] = i;
                }
            }

            dfs(possibleNum, 0, 0);

            System.out.println(ans);
        }
    }    

    static int nowSel[] = new int[3];
    static void dfs(int[] numList, int depth, int start) {
        if (depth == 3) {
            int tmpSum = dist[0][nowSel[0]] + dist[nowSel[0]][nowSel[1]] + dist[nowSel[1]][nowSel[2]] + dist[nowSel[2]][10];
            ans = Math.min(tmpSum, ans);
            return;
        }

        for (int i = start; i < numList.length; i++) {
            nowSel[depth] = numList[i];
            dfs(numList, depth+1, i+1);
        }
    }
}
