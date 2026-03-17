package ssafy_task._260313;

import java.io.*;
import java.util.*;

public class SW7793_AhMyGoddess_김성령 {
    static int R, C, ans;
    static char[][] board;
    static Node start, end;
    static List<Node> evils;
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    static class Node {
        int r, c;
        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            board = new char[R][C];
            evils = new ArrayList<>();
            for (int i = 0; i < R; i++) {
                board[i] = br.readLine().toCharArray();
                for (int j = 0; j < C; j++) {
                    char tmp = board[i][j];
                    board[i][j] = tmp;
                    if (tmp == 'D') {
                        end = new Node(i, j);
                    } else if (tmp == 'S') {
                        start = new Node(i, j);
                        board[i][j] = '.';
                    } else if (tmp == '*') {
                        evils.add(new Node(i, j));
                    }
                }
            }
            boolean[][] suVisited = new boolean[R][C];
            boolean[][] evilVisited = new boolean[R][C];
            Deque<Node> suDq = new ArrayDeque<>();
            suDq.offer(start);
            suVisited[start.r][start.c] = true;
            Deque<Node> evilDq = new ArrayDeque<>();
            for (int i = 0; i < evils.size(); i++) {
                Node nowEvil = evils.get(i);
                evilVisited[nowEvil.r][nowEvil.c] = true;
                evilDq.offer(nowEvil);

            }

            String ans = "";
            int timer = 0;
            boolean breakFlag = false;
            while (!suDq.isEmpty()) {
                timer++;
                // 악마 먼저 이동
                int nowEvilSize = evilDq.size();
                // 현재 깊이만큼만 수행
                for (int i = 0; i < nowEvilSize; i++) {
                    Node nowEvil = evilDq.pollFirst();

                    for (int k = 0; k < 4; k++) {
                        int nr = nowEvil.r + dr[k];
                        int nc = nowEvil.c + dc[k];

                        if (nr < 0 || nc < 0 || nr >= R || nc >= C || evilVisited[nr][nc]) continue;
                        if (board[nr][nc] == 'D' || board[nr][nc] == 'X') continue;

                        evilVisited[nr][nc] = true;
                        board[nr][nc] = '*';

                        evilDq.offer(new Node(nr, nc));
                    }
                }
                // 수연이 이동
                int nowSuSize = suDq.size();
                for (int i = 0; i < nowSuSize; i++) {
                    Node nowSu = suDq.pollFirst();

                    for (int k = 0; k < 4; k++) {
                        int nr = nowSu.r + dr[k];
                        int nc = nowSu.c + dc[k];

                        if (nr < 0 || nc < 0 || nr >= R || nc >= C || suVisited[nr][nc]) continue;
                        if (board[nr][nc] == 'D') {
                            ans = Integer.toString(timer);
                            breakFlag = true;
                            break;
                        }

                        if (board[nr][nc] == 'X' || board[nr][nc] == '*') continue;

                        suVisited[nr][nc] = true;
                        suDq.offer(new Node(nr, nc));
                    }
                    if (breakFlag) break;
                }
                if (breakFlag) break;
            }
            
            ans = ans.equals("") ? "GAME OVER" : ans;
            sb.append("#" + t + " " + ans + "\n");
        }
        System.out.println(sb);
    }
}