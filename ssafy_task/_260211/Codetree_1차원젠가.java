package ssafy_task._260211;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Codetree_1차원젠가 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] list = new int[N];

        for (int i = 0; i < N; i++) {
            list[i] = Integer.parseInt(br.readLine());
        }

        st = new StringTokenizer(br.readLine());
        int x1 = Integer.parseInt(st.nextToken())-1;
        int x2 = Integer.parseInt(st.nextToken())-1;
        for (int i = x1; i <= x2; i++) {
            list[i] = 0;
        } 
        int[] tmp = new int[N-(x2-x1+1)];
        int idx = 0;
        for (int i = 0; i < N; i++) {
            if (list[i] != 0) {
                tmp[idx] = list[i];
                idx++;
            }
        }
        list = tmp;

        st = new StringTokenizer(br.readLine());
        int y1 = Integer.parseInt(st.nextToken())-1;
        int y2 = Integer.parseInt(st.nextToken())-1;

        for (int i = y1; i <= y2; i++) {
            list[i] = 0;
        } 
        int[] tmp2 = new int[list.length-(y2-y1+1)];
        int idx2 = 0;
        for (int i = 0; i < list.length; i++) {
            if (list[i] != 0) {
                tmp2[idx2] = list[i];
                idx2++;
            }
        }
        list = tmp2;
        System.out.println(list.length);
        for (int i : list) {
            System.out.println(i);
        }
    }
    
}