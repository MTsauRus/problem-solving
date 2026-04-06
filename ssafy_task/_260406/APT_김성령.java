package ssafy_task._260406;

public class APT_김성령 {
    public static void main(String[] args) {
        int[] dp = new int[100];
        dp[0] = 1; dp[1] = 2; dp[2] = 3;

        for (int i = 3; i < 10; i++) {
            dp[i] = dp[i-1] + dp[i-2];

        }
        
        System.out.println(dp[8]);
    }    
}
