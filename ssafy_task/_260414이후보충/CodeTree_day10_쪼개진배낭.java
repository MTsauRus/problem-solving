package ssafy_task._260414이후보충;

import java.io.*;
import java.util.*;

public class CodeTree_day10_쪼개진배낭 {
    static class Gem {
        double weight, value;
        public Gem(double weight, double value) {
            this.weight = weight;
            this.value = value;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        double W = Double.parseDouble(st.nextToken());
        
        PriorityQueue<Gem> pq = new PriorityQueue<>(
            (Gem o1, Gem o2) -> {
                double firstValue = o1.value / o1.weight;
                double secondValue = o2.value / o2.weight;
                int flag = 0;
                if (firstValue >= secondValue) {
                    flag = -1;
                } else {
                    flag = 1;
                }
                return flag;
            }
        );

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            pq.offer(new Gem(
                Double.parseDouble(st.nextToken()), 
                Double.parseDouble(st.nextToken()) 
            ));
        }

        double ans = 0.0;
        while (!pq.isEmpty() && W > 0) {
            Gem now = pq.poll();
            if (now.weight <= W) {
                W -= now.weight;
                ans += now.value;
            } else {
                double pieceSize = W / now.weight;
                ans += now.value * pieceSize;
                break;
            }
        }

       System.out.printf("%.3f", ans);

    }
}