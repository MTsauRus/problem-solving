package ssafy_task._260204;

import java.util.*;
import java.io.*;

public class SW4130_UniqueMagnet_김성령 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static class Magnet {
        int[] NS;
        int p;

        public Magnet(int[] NS, int p) {
            this.NS = NS;
            this.p = p;
        }
    }

    public static void main(String[] args) throws IOException {

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t < T+1; t++) {
            int N = Integer.parseInt(br.readLine());
            List<Magnet> magnetList = new ArrayList<>();
            magnetList.add(new Magnet(null, 0)); // dummy
            
            for (int i = 0; i < 4; i++) {
                int[] NS = new int[8];
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 8; j++) {
                    NS[j] = Integer.parseInt(st.nextToken());
                }
                magnetList.add(new Magnet(NS, 0));
            }

            List<Integer[]> movingPlan = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int mgNum = Integer.parseInt(st.nextToken());
                int isClockWise = Integer.parseInt(st.nextToken());
                Integer[] tmpPlan = new Integer[2];
                tmpPlan[0] = mgNum;
                tmpPlan[1] = isClockWise;
                movingPlan.add(tmpPlan);

                
            }
        }
    }


    


    // static void rotate(int mgNum, int isClockWise, List<Magnet> mgList) {
    //     Magnet mg1 = mgList.get(1);
    //     Magnet mg2 = mgList.get(2);
    //     Magnet mg3 = mgList.get(3);
    //     Magnet mg4 = mgList.get(4);
        
    //     if (mgNum == 1) {
    //         if (mg1.NS[(mg1.p+2)%8] != mg2.NS[(mg2.p+6)%8]) { // 다르면 회전
    //             if (isClockWise == 1) {
    //                 mg1.p = (mg1.p + 7)%8;
    //                 mg2.p = (mg2.p + 1)%8;
    //             } else {
    //                 mg1.p = (mg1.p + 1)%8;
    //                 mg2.p = (mg2.p + 7)%8;
    //             }
    //         } else {
    //             if (isClockWise == 1) {
    //                 mg1.p = (mg1.p + 7)%8;
    //             } else {
    //                 mg1.p = (mg1.p + 1)%8;
    //             }
    //         }

    //     } else if (mgNum == 2) {

    //     } else if (mgNum == 3) {

    //     } else {

    //     }
    // }
}
