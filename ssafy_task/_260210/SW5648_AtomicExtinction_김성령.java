package ssafy_task._260210;

import java.util.*;
import java.io.*;
// map의 key를 String으로 변환하여 사용

public class SW5648_AtomicExtinction_김성령 {
    static int N;
    static List<Integer[]> atomList;
    static int ans;

    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        
        for (int t = 1; t < T+1; t++) {
            N = Integer.parseInt(br.readLine());
            atomList = new ArrayList<>();
            ans = 0;
            Map<String, List<Integer[]>> hmap;
            for (int i  = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken())*2;
                int y = Integer.parseInt(st.nextToken())*2;
                int d = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                atomList.add(new Integer[]{x,y,d,e});
                
            }

            for (int i = 0; i < 4000; i++) { // 4천번 반복
                hmap = new HashMap<>();
                for (Integer[] atom : atomList) { // 원자별로 꺼내서
                    atom[0] += dx[atom[2]]; // 이동하고
                    atom[1] += dy[atom[2]];

                    if (atom[0] < -2000 || atom[0] > 2000 || atom[1] < -2000 || atom[1] > 2000) continue;
                    String key = atom[0] + " " + atom[1];
                    if (hmap.containsKey(key)) {
                        hmap.get(key).add(atom);
                    } else {
                        List<Integer[]> tmp = new ArrayList<>();
                        tmp.add(atom);
                        hmap.put(key, tmp);    
                    }
                }

                List<Integer[]> nextAtoms = new ArrayList<>();
                for (List<Integer[]> list : hmap.values()) {
                    if (list.size() > 1) {
                        for (Integer[] atom : list) {
                            ans += atom[3];
                        }
                    } else {
                        nextAtoms.add(list.get(0));
                    }
                }
            }
            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
        System.out.println(sb);
    }
}
