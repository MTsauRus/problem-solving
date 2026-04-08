package ssafy_task._260408;

import java.io.*;
import java.util.*;

/*
    1. 고객 도착 시간 정렬 -> 고객번호부여
    2. 접수큐 통과시킴
    3. 접수 통과 결과를 (시간, 접수큐번호, 고객번호)로 저장
    4. 정비큐 입장 -> 
        - 접수큐 번호가 요구와 동일하고, 정비큐가 동일하다면 ans++
        - 
*/

public class SW2477_AutoRepairShop_김성령 {
    static int recepCnt, repairCnt, custCnt, recepAnsNum, repairAnsNum;
    static int[] recepTime, repairTime, custArriveTime;

    static class Customer implements Comparable<Customer>{
        int waitingTime, recepNum, repairNum;

        public Customer(int waitingTime)  {
            this.waitingTime = waitingTime;
            this.recepNum = -1;
            this.repairNum = -1;
        }

        @Override
        public int compareTo(Customer o) {
            if (this.waitingTime == o.waitingTime) return Integer.compare(this.recepNum, o.recepNum);
            return Integer.compare(this.waitingTime, o.waitingTime);
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t < T+1; t++) {
            st = new StringTokenizer(br.readLine());
            recepCnt = Integer.parseInt(st.nextToken());
            repairCnt = Integer.parseInt(st.nextToken());
            custCnt = Integer.parseInt(st.nextToken());
            recepAnsNum = Integer.parseInt(st.nextToken());
            repairAnsNum = Integer.parseInt(st.nextToken());
            
            st = new StringTokenizer(br.readLine());
            recepTime = new int[recepCnt];
            for (int i = 0; i < recepCnt; i++) {
                recepTime[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            repairTime = new int[repairCnt];
            for (int i = 0; i < repairCnt; i++) {
                repairTime[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            custArriveTime = new int[custCnt];
            for (int i = 0; i < custCnt; i++) {
                custArriveTime[i] = Integer.parseInt(st.nextToken());
            }
            
            PriorityQueue<Customer> custPq = new PriorityQueue<>();
            for (int i = 0; i < custCnt; i++) {
                custPq.offer(new Customer(custArriveTime[i]));
            }

            while (!custPq.isEmpty()) {
                Customer now = custPq.poll();

                // 
            }
        }
    }
}
