package programmers;

import java.util.*;
import java.io.*;

public class _2024kakaoInternship_주사위고르기 {
    static int N;
    static List<Integer> ansList;
    static int maxWin = 0;
    static int[][] diceInfo;

    // public static void main(String[] args) {
    //     // 테스트 케이스 1
    //     int[][] dice1 = {
    //         {1, 2, 3, 4, 5, 6},
    //         {3, 3, 3, 3, 4, 4},
    //         {1, 3, 3, 4, 4, 4},
    //         {1, 1, 4, 4, 5, 5}
    //     };
    //     System.out.println("Test 1: " + Arrays.toString(solution(dice1))); 
    //     // 예상: [1, 4]

    //     // 테스트 케이스 2
    //     int[][] dice2 = {
    //         {1, 2, 3, 4, 5, 6},
    //         {2, 2, 4, 4, 6, 6}
    //     };
    //     System.out.println("Test 2: " + Arrays.toString(solution(dice2))); 
    //     // 예상: [2]
        
    //     // 테스트 케이스 3
    //     int[][] dice3 = {
    //          {40, 41, 42, 43, 44, 45},
    //          {43, 43, 42, 42, 41, 41},
    //          {1, 1, 80, 80, 80, 80},
    //          {70, 70, 1, 1, 70, 70}
    //     };
    //     System.out.println("Test 3: " + Arrays.toString(solution(dice3)));
    //     // 예상: [1, 3]
    // }

    static int[] solution(int[][] dice) {
        N = dice.length;
        diceInfo = dice;
        ansList = new ArrayList<>();
        maxWin = 0;

        List<Integer> aDices = new ArrayList<>();
        comb(0, 0, aDices); // A의 주사위 조합 결정

        // 결과 배열로 변환
        int[] res = new int[N/2];
        for (int i = 0; i < N/2; i++) {
            res[i] = ansList.get(i) + 1;
        }
        // 오름차순 정렬
        Arrays.sort(res);
        return res;
    }

    static void comb(int start, int depth, List<Integer> aDices) {
        if (depth ==  N/2) {
            calculateWinningRate(aDices); // 현재 주사위 조합을 들고 승률 체크
            return;
        }
        
        for (int i = start; i < N; i++) {
            aDices.add(i);
            comb(i+1, depth+1, aDices);
            aDices.remove(aDices.size()-1);
        }
    }

    // 승률 계산
    static void calculateWinningRate(List<Integer> aDices) {
        List<Integer> bDices = new ArrayList<>();
        boolean[] isSelected = new boolean[N];
        for (int idx : aDices) {
            isSelected[idx] = true;
        }
        // A가 고르지 않은 주사위는 B에게
        for (int i = 0; i < N; i++) {
            if (!isSelected[i]) bDices.add(i);
        }

        // 각 주사위 합의 모든 경우의 수를 담자
        List<Integer> sumA = new ArrayList<>();
        List<Integer> sumB = new ArrayList<>();
        
        perm(0, 0, aDices, sumA);
        perm(0, 0, bDices, sumB);

        // 이분 탐색을 위해 B의 합 배열을 정렬
        Collections.sort(sumB);
        int aWins = 0;
        for (int scoreA : sumA) {
            int cnt = bisect(sumB, scoreA);
            aWins += cnt;
        }
        
        if (aWins > maxWin) {
            maxWin = aWins;
            ansList = new ArrayList<>(aDices);
        }
    }

    // 각 주사위 눈의 합을 만드는 메서드
    static void perm(int depth, int sum, List<Integer> dices, List<Integer> sums) {
        if (depth == dices.size()) {
            sums.add(sum);
            return;
        }

        int idx = dices.get(depth);
        for (int i = 0; i < 6; i++) {
            perm(depth+1, sum+diceInfo[idx][i], dices, sums);
        }
    }

    // target보다 크거나 같은 첫 번째 위치 반환
    static int bisect(List<Integer> list, int target) {
        int start = 0;
        int end = list.size();

        while (start < end) {
            int mid = (start + end) / 2;
            if (list.get(mid) < target) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return start;
    }
}
