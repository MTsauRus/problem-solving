package ssafy_task._260202;

import java.io.*;
import java.util.*;

public class SW1228_CryptoMessage1_useCollections_김성령 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        for (int t = 1; t <= 10; t++) {
            List<String> list = new LinkedList<>();
            int len = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < len; i++) {
                list.add(st.nextToken());
            }

            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());

            for (int i = 0; i < N; i++) {
                String cmd = st.nextToken();
                int index = Integer.parseInt(st.nextToken());
                int count = Integer.parseInt(st.nextToken());
            

                for (int j = 0; j < count; j++) {
                    list.add(index + j, st.nextToken());
                }
            
            }
            sb.append("#").append(t).append(" ");
            for (int i = 0; i < 10; i++) {
                sb.append(list.get(i)).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
    