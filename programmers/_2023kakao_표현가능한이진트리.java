package programmers;

import java.util.Arrays;

public class _2023kakao_표현가능한이진트리 {

    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];
        
        for (int i = 0; i < numbers.length; i++) {
            String bStr = Long.toBinaryString(numbers[i]);

            int len = bStr.length();
            int h = 1;
            int treeLen = 1;
            while (treeLen < len) {
                h++;
                treeLen = (int) Math.pow(2, h) - 1;
            }
            
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < treeLen - len; j++) {
                sb.append("0");
            }
            sb.append(bStr);
            
            if (dfs(sb.toString(), 0, treeLen - 1, false)) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        return answer;
    }

    private boolean dfs(String s, int start, int end, boolean isParentDummy) {
        int mid = (start + end) / 2; // 현재 서브트리의 루트 노드
        boolean isCurrentDummy = (s.charAt(mid) == '0');
        
        if (isParentDummy && !isCurrentDummy) {
            return false;
        }
        
        // 리프면 리턴
        if (start == end) {
            return true;
        }
        
        return dfs(s, start, mid - 1, isCurrentDummy) && 
               dfs(s, mid + 1, end, isCurrentDummy);
    }
}
