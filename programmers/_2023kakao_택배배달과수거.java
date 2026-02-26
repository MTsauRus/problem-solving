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
        int mainIdx = n-1; // 메인 인덱스. deliIdx, pickIdx 중 더 큰 값임. 택배차가 여기까지는 와야 한다는 의미
        int deliIdx = n-1; int pickIdx = n-1;

        while (mainIdx > -1) {
            int deliCap = 0; int pickCap = 0; // 현재 반복의 배달/수거 개수
            int maxDeliIdx = -1; int maxPickIdx = -1; // 현재 반복문에서 가장 먼 집을 기록합니다. 

            // 배달부터 시작
            for (;deliCap < cap && deliIdx>-1; deliIdx--) { // 배달 cap을 다 채우거나, deliIdx가 유효할 때까지 반복. 
                if (deliveries[deliIdx] == 0) continue; // 이번 집의 배달이 없으면 넘김
                
                maxDeliIdx = Math.max(maxDeliIdx, deliIdx); // 가장 먼 집이 최초 1회 기록됩니다. (인덱스는 작아지는 방향으로 탐색되므로 최초에만 업데이트됨)
                
                if (deliCap + deliveries[deliIdx] < cap) {  // 현재 집의 모든 배달을 수행해도 cap보다 작은 경우
                    deliCap+=deliveries[deliIdx]; // 모든 배달을 수행합니다. 
                    deliveries[deliIdx] = 0;
                    continue;
                } else if (deliCap + deliveries[deliIdx] == cap) { // 현재 집의 배달을 수행하면 정확히 cap을 채우는 경우
                    deliveries[deliIdx] = 0;
                    deliIdx--; // 다음 반복에서는 현재 집의 바로 앞집부터 탐색하면 됩니다. 
                    break; // 차피 배달 못하므로 for문 탈출
                } else { // deliveries[deliIdx]를 모두 못옮기는 경우
                    deliveries[deliIdx] -= cap - deliCap; // 옮길 수 있는 만큼 배달합니다.
                    break;
                }
            }
            
            for (;pickCap < cap && pickIdx>-1; pickIdx--) {
                // 위의 배달 로직과 정확히 동일
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
            
            mainIdx = Math.max(deliIdx, pickIdx); // 메인 인덱스는 배달/픽업 인덱스 중 더 먼 곳을 저장합니다. 
            answer += (Math.max(maxDeliIdx, maxPickIdx)+1) * 2; // 이번 반복에서 가장 멀리 간 집의 왕복거리를 answer에 더해줍니다. 
        }
        
        return answer;
    }
}
