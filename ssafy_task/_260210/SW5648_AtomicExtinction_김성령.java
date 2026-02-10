package ssafy_task._260210;

import java.util.*;
import java.io.*;

public class SW5648_AtomicExtinction_김성령 {
    static int N;
    static List<Atom> atomList;

    static int[] dx = {};
    static int[] dy = {};
    static class Atom {
        int x, y;
        int d; 
        int e;

        public Atom(int x, int y, int d, int e) {
            this.x = x;
            this.y = y;
            this.d = d;
            this.e = e;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());

            atomList = new ArrayList<>();
            for (int i  = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                atomList.add(new Atom(
                    Integer.parseInt(st.nextToken()), 
                    Integer.parseInt(st.nextToken()), 
                    Integer.parseInt(st.nextToken()), 
                    Integer.parseInt(st.nextToken())));    
            }
        }


    }
}
