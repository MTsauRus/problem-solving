package programmers;

public class _2024kakaoInternship_주사위고르기 {
    

    public static void main(String[] args) {
        int[][] array1 = {
            {1, 2, 3, 4, 5, 6},
            {3, 3, 3, 3, 4, 4},
            {1, 3, 3, 4, 4, 4},
            {1, 1, 4, 4, 5, 5}
        };

        int[][] array2 = {
            {1, 2, 3, 4, 5, 6},
            {2, 2, 4, 4, 6, 6}
        };

        int[][] array3 = {
            {40, 41, 42, 43, 44, 45},
            {43, 43, 42, 42, 41, 41},
            {1, 1, 80, 80, 80, 80},
            {70, 70, 1, 1, 70, 70}
        };
        Solution s = new Solution();
        s.solution(null);
    }

    static class Solution {
        public int[] solution(int[][] dice) {
            double[] prop = new double[dice.length];
            for (int i = 0; i < dice.length; i++) {
                int[] d = dice[i];
                int tmpSum = 0;
                for (int tmp : d) {
                    tmpSum+=tmp;
                }
                prop[i] = tmpSum / 6.0;
            }


            }


            int[] answer = {};
            return answer;
        }
    }
}
