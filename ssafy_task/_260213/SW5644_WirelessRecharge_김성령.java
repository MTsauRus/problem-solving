package ssafy_task._260213;

import java.io.*;
import java.util.*;

public class SW5644_WirelessRecharge_김성령 {
    static class Charger {
        int r, c, range, energy;
        public Charger(int r, int c, int range, int energy) {
            this.r = r;
            this.c = c;
            this.range = range;
            this.energy = energy;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            // 시간
            int M = Integer.parseInt(st.nextToken());
            // 충전기 수
            int S = Integer.parseInt(st.nextToken());
            
            int[] userA = new int[M];
            int[] userB = new int[M];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                userA[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                userB[i] = Integer.parseInt(st.nextToken());
            }
            
            List<Charger> chargers = new ArrayList<>();
            for (int i = 0; i < S; i++) {
                
            }

        }


    }    
}
