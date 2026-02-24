package programmers;

class Solution {
    static int maxMember = 0;
    static int maxEarn = 0;
    static int[][] globalUsers;
    static int[] globalEmoticons;
    static int[] userStatus;
    static boolean[] isUserMember;
    
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
            if (maxMember < membership) {
                maxMember = membership;
                maxEarn = earn;
                return;
            } else if (maxMember == membership) {
                maxEarn = Math.max(maxEarn, earn);
                return;
            } else {
                return;
            }
        }
        
        int[] nowUserBacktrack = userStatus.clone();
        boolean[] nowMemberBacktrack = isUserMember.clone();
        int nowEmoticonPrice = (int)((double) (globalEmoticons[depth] * (100 - saleRatio)) * 0.01);
        int nowMembership = membership;
        int nowEarn = earn;
        
        for (int i = 0; i < globalUsers.length; i++) {
            if (isUserMember[i]) continue;
            if (globalUsers[i][0] <= saleRatio) {
                userStatus[i] += nowEmoticonPrice;
                nowEarn += nowEmoticonPrice;
                
                if (userStatus[i] >= globalUsers[i][1]) {
                    nowEarn -= userStatus[i];
                    userStatus[i] = 0;
                    nowMembership++;
                    isUserMember[i] = true;
                }
            }
        }
        
        for (int nowSaleRatio = 10; nowSaleRatio < 41; nowSaleRatio += 10) {
            backtrack(depth+1, globalEmoticons.length, nowEarn, nowMembership, nowSaleRatio);
        }
        
        // 백트래킹
        userStatus = nowUserBacktrack;
        isUserMember = nowMemberBacktrack;
    }
}