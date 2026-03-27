package ssafy_task.samsung_B;

import java.io.*;
import java.util.*;

class 입시예측_UserSolution
{
	static int N, M;
	static TreeSet<Student>[] univs;
	static int[][] weights;
	static boolean isDirty;
	static int[] ans;
	static Student[][] cache;

    static int[] assignedList;
    static int assignedCnt;

	static class Student implements Comparable<Student>{
		int sid, tot;

		public Student(int sid, int tot) {
			this.sid = sid;
			this.tot = tot;
		}

		@Override
		public int compareTo(Student o) {
			if (this.tot == o.tot) {
				// 학번 오름차순
				return Integer.compare(this.sid, o.sid);
			}
			// 총점 내림차순
			return Integer.compare(o.tot, this.tot);
		}
	}
	public void init(int n, int m, int[][] mWeights)
	{
		N = n;
		M = m;
		weights = mWeights;
		univs = new TreeSet[M];
		isDirty = false;
		ans = new int[20001];
		cache = new Student[M][20001];
		assignedList = new int[55005]; 
        assignedCnt = 0;
		Arrays.fill(ans, -1);

		for (int i = 0; i < M; i++) {
			univs[i] = new TreeSet<Student>();
		}
	}

	public void add(int mID, int[] mScores)
	{
		for (int m = 0; m < M; m++) {
			int tmpTot = 0;
			for (int i = 0; i < 5; i++) {
				tmpTot += mScores[i] * weights[m][i];
			}
			Student s = new Student(mID, tmpTot);
			univs[m].add(s);
			cache[m][mID] = s;
		}

		isDirty = true;
	}

	public void erase(int mID)
	{
		for (int m = 0; m < M; m++) {
			if (cache[m][mID] != null) {
				univs[m].remove(cache[m][mID]);
				cache[m][mID] = null;
			}
		}
		isDirty = true;
		return;
	}

	public int suggest(int mID)
	{
		if (!isDirty) 
			return ans[mID];

		for (int i = 0; i < assignedCnt; i++) {
			ans[assignedList[i]] = -1;
			}
		assignedCnt = 0; // 수첩 초기화

		for (int m = 0; m < M; m++) {
			int picked = 0;

			for (Student s : univs[m]) {
				if (ans[s.sid] != -1) continue;

			ans[s.sid] = m+1;
			picked++;
			assignedList[assignedCnt++] = s.sid;
			
			if (picked == N) break;
			}
		}
		
		isDirty = false;
		return ans[mID];
	}
}