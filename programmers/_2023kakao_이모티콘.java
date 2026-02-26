package programmers;

class Solution {
    static int maxMember = 0; // 멤버십을 가입한 최대 인원
    static int maxEarn = 0; // 최대 멤버십 가입자일 때의 최대 구매 가격
    static int[][] globalUsers; // solution에서 받은 users를 static으로 쓰기 위해 사용
    static int[] globalEmoticons; // 동일
    static int[] userStatus; // 현재 유저들의 구매 금액 (백트래킹의 visited 역할)
    static boolean[] isUserMember; // 현재 유저가 멤버십을 가입했는지의 여부. 가입 시 구매하지 않고 건너뛰기 위함
    
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer;
        globalUsers = users;
        globalEmoticons = emoticons;
        
        userStatus = new int[users.length];
        isUserMember = new boolean[users.length];
        
        backtrack(0, emoticons.length, 0, 0, 10);
        backtrack(0, emoticons.length, 0, 0, 20);
        backtrack(0, emoticons.length, 0, 0, 30);
        backtrack(0, emoticons.length, 0, 0, 40);
        
        answer = new int[]{maxMember, maxEarn};
        return answer;
    }
    
    static void backtrack(int depth, int m, int earn, int membership, int saleRatio) {
        if (depth == m) {
            if (maxMember < membership) { // 멤버십 인원이 현재 최대보다 많다면 
                maxMember = membership;
                maxEarn = earn; // 가격 역시 현재 가격으로 갱신
                return;
            } else if (maxMember == membership) { // 멤버십 인원이 최대 인원과 동일하다면
                maxEarn = Math.max(maxEarn, earn); // 최대 가격 비교 갱신
                return;
            } else {
                return;
            }
        }
        
        int[] nowUserBacktrack = userStatus.clone(); // 백트래킹을 위해 현재 구매 금액 복사
        boolean[] nowMemberBacktrack = isUserMember.clone(); // 백트래킹을 위해 현재 멤버십 가입 여부 복사
        int nowEmoticonPrice = (int)((double) (globalEmoticons[depth] * (100 - saleRatio)) * 0.01);
        int nowMembership = membership;
        int nowEarn = earn;
        
        for (int i = 0; i < globalUsers.length; i++) {
            if (isUserMember[i]) continue; // 해당 유저가 이미 멤버십을 가입했다면 볼 필요가 없음
            if (globalUsers[i][0] <= saleRatio) { // 현재 유저의 희망 세일 비율보다 높다면 이를 구매
                userStatus[i] += nowEmoticonPrice;
                nowEarn += nowEmoticonPrice;
                
                if (userStatus[i] >= globalUsers[i][1]) { // 구매했는데 구매금액이 멤버십 가입금액을 넘었다면
                    nowEarn -= userStatus[i]; // 현재 차례의 수입에서 해당 유저의 구매금액을 모두 빼주고
                    userStatus[i] = 0; // 해당 유저는 모든 구매를 취소함
                    nowMembership++; // 멤버십 가입
                    isUserMember[i] = true;
                }
            }
        }
        // 10, 20, 30, 40 dfs
        for (int nowSaleRatio = 10; nowSaleRatio < 41; nowSaleRatio += 10) {
            backtrack(depth+1, globalEmoticons.length, nowEarn, nowMembership, nowSaleRatio);
        }
        
        // 백트래킹 처리
        userStatus = nowUserBacktrack;
        isUserMember = nowMemberBacktrack;
    }
}