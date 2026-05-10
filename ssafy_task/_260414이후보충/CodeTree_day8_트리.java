package ssafy_task._260414이후보충;

import java.util.*;
import java.io.*;

public class CodeTree_day8_트리 {
    
    static int N;
    static int[] indegree;
    static List<Integer>[] graph;
    static Map<Integer, String> intToStr;
    static Map<String, Integer> strToInt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        String[] input = new String[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            input[i] = st.nextToken();
        }

        Arrays.sort(input);
        intToStr = new HashMap<>();
        strToInt = new HashMap<>();
        for (int i = 0; i < N; i++) {
            intToStr.put(i, input[i]);
            strToInt.put(input[i], i);
        }
        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }

        indegree = new int[N];
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = strToInt.get(st.nextToken());
            int e = strToInt.get(st.nextToken());
            graph[e].add(s);
            indegree[s]++;    
        }
           
        List<Integer> rootList = new ArrayList<>();
        Deque<Integer> dq = new ArrayDeque<>();
        int rootCnt = 0;
        for (int i = 0; i < N; i++) {
            if (indegree[i] == 0) {
                rootList.add(i);
                rootCnt++;
                dq.offer(i);
            }
        }


        List<Integer>[] ansGraph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            ansGraph[i] = new ArrayList<>();
        }
        
        while (!dq.isEmpty()) {
            int now = dq.pollFirst();
            for (int next : graph[now]) {
                if (--indegree[next] == 0) {
                   ansGraph[now].add(next);
                   dq.offer(next); 
                }
            }
        }
        
        for (List<Integer> tmpList : ansGraph) {
            Collections.sort(tmpList);
        }

        System.out.println(rootCnt);
        for (int root : rootList) {
            sb.append(intToStr.get(root) + " ");
        }
        sb.append("\n");
        for (int i = 0; i < N; i++) {
            sb.append(intToStr.get(i) + " ");
            sb.append(ansGraph[i].size() + " ");
            for (int next : ansGraph[i]) {
                sb.append(intToStr.get(next) + " ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
