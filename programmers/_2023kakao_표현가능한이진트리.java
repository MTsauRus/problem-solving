package programmers;

import java.util.Arrays;

public class _2023kakao_표현가능한이진트리 {

    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];
        
        for (int i = 0; i < numbers.length; i++) {
            String bStr = Long.toBinaryString(numbers[i]); // 현재 숫자를 이진수로 변환

            int len = bStr.length(); // 현재 길이 저장
            int h = 1;
            int treeLen = 1;
            while (treeLen < len) { 
                h++;
                treeLen = (int) Math.pow(2, h) - 1; 
            }
            
            StringBuilder sb = new StringBuilder();
            // 1, 3, 7, 15 중 가장 가까운 이진트리만큼 0을 패딩
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
        
        // 부모가 더미인데 자식도 더미면 불가능
        if (isParentDummy && !isCurrentDummy) {
            return false;
        }
        
        // 리프까지 갔으면 살아있는거임
        if (start == end) {
            return true;
        }
        
        // 왼쪽 자식, 오른쪽 자식으로 dfs. 하나라도 false가 나오면 false 리턴
        return dfs(s, start, mid - 1, isCurrentDummy) && 
               dfs(s, mid + 1, end, isCurrentDummy);
    }
}
