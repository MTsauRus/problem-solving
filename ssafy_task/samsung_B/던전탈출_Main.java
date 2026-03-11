package ssafy_task.samsung_B;

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class 던전탈출_Main {
	private static final int CMD_INIT				= 0;
	private static final int CMD_ADD_GATE			= 1;
	private static final int CMD_REMOVE_GATE		= 2;
	private static final int CMD_GET_MIN_TIME		= 3;
	private static final int MAX_N					= 350;

	private static int[][] map = new int[MAX_N][MAX_N];
	private static UserSolution usersolution = new UserSolution();
	private static Scanner sc;

	private static boolean run() throws Exception 	{
		int Q = sc.nextInt();
		
		boolean okay = false;

		for (int q = 0 ; q < Q ; ++q) {
			int cmd = sc.nextInt();
			int ret, ans;
			int N;
			int maxStamina;
			int gateID1, gateID2;
			int r, c;
			
			switch(cmd) {
			case CMD_INIT:
				N = sc.nextInt();
				maxStamina = sc.nextInt();
				for (int i = 0 ; i < N ; i++) {
					for (int j = 0 ; j < N ; j++) {
						int in = sc.nextInt();
						map[i][j] = in;
					}
				}
				usersolution.init(N, maxStamina, map);
				okay = true;
				break;
			case CMD_ADD_GATE:
				gateID1 = sc.nextInt();
				r = sc.nextInt();
				c = sc.nextInt();
				usersolution.addGate(gateID1, r, c);
				break;
			case CMD_REMOVE_GATE:
				gateID1 = sc.nextInt();
				usersolution.removeGate(gateID1);
				break;
			case CMD_GET_MIN_TIME:
				gateID1 = sc.nextInt();
				gateID2 = sc.nextInt();
				ret = usersolution.getMinTime(gateID1, gateID2);
				ans = sc.nextInt();
				if (ret != ans) okay = false;
				break;
			default:
				okay = false;
				break;
			}
		}
		return okay;
	}
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new java.io.FileInputStream("res/sample_input.txt"));
		sc = new Scanner(System.in);

		int TC = sc.nextInt();
		int MARK = sc.nextInt();
		
		for (int testcase = 1 ; testcase <= TC ; ++testcase) {
			int score = run() ? MARK : 0;
			System.out.println("#" + testcase + " " + score);
		}
		sc.close();
	}
}