package programmers;

public class _2023kakao_택배배달과수거 {

    public static void main(String[] args) {
        long ans = solution(
            1, 2, new int[]{5,0}, new int[]{0,5}
        );

        long ans2 = solution(
            2,7,new int[]{1,0,2,0,1,0,2},new int[]{0,2,0,1,0,2,0}
        );
        System.out.println(ans);
        System.out.println(ans2);
    }
    public static long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        int mainIdx = n-1;
        int deliIdx = n-1; int pickIdx = n-1;

        while (mainIdx > -1) {
            int deliCap = 0; int pickCap = 0;
            int maxDeliIdx = -1; int maxPickIdx = -1;
            for (;deliCap < cap && deliIdx>-1; deliIdx--) {
                // 
                if (deliveries[deliIdx] == 0) continue;
                
                maxDeliIdx = Math.max(maxDeliIdx, deliIdx);
                
                if (deliCap + deliveries[deliIdx] < cap) {
                    deliCap+=deliveries[deliIdx];
                    deliveries[deliIdx] = 0;
                    continue;
                } else if (deliCap + deliveries[deliIdx] == cap) {
                    deliveries[deliIdx] = 0;
                    deliIdx--;
                    break;
                } else { // deliveries[deliIdx]를 모두 못옮기는 경우
                    deliveries[deliIdx] -= cap - deliCap;
                    break;
                }
            }
            
            for (;pickCap < cap && pickIdx>-1; pickIdx--) {
                // 
                if (pickups[pickIdx] == 0) continue;
                
                maxPickIdx = Math.max(maxPickIdx, pickIdx);
                
                if (pickCap + pickups[pickIdx] < cap) {
                    pickCap+=pickups[pickIdx];
                    pickups[pickIdx] = 0;
                    continue;
                } else if (pickCap + pickups[pickIdx] == cap) {
                    pickups[pickIdx] = 0;
                    pickIdx--;
                    break;
                } else { 
                    pickups[pickIdx] -= cap - pickCap;
                    break;
                }
            }
            
            mainIdx = Math.max(deliIdx, pickIdx);
            answer += (Math.max(maxDeliIdx, maxPickIdx)+1) * 2;
        }
        
        return answer;
    }
}
