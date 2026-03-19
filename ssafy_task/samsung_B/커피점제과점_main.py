import sys

from 커피점제과점_solution_가지치기코드 import init, add, calculate

CMD_INIT = 100
CMD_ADD = 200
CMD_CALC = 300

def run():
	q = int(sys.stdin.readline())
	okay = False

	sBuildingArr = []
	eBuildingArr = []
	mDistArr = []

	for i in range(q):
		cmd = int(sys.stdin.readline())

		if cmd == CMD_INIT:
			inputarray = sys.stdin.readline().split()
			n = int(inputarray[0])
			k = int(inputarray[1])
			for _ in range(k):
				road = sys.stdin.readline().split()
				sBuildingArr.append(int(road[0]))
				eBuildingArr.append(int(road[1]))
				mDistArr.append(int(road[2]))

			init(n, k, sBuildingArr, eBuildingArr, mDistArr)
			okay = True
		elif cmd == CMD_ADD:
			inputarray = sys.stdin.readline().split()
			sBuilding = int(inputarray[0])
			eBuilding = int(inputarray[1])
			mDist = int(inputarray[2])
			add(sBuilding, eBuilding, mDist)
		elif cmd == CMD_CALC:
			inputarray = sys.stdin.readline().split()
			m = int(inputarray[0])
			p = int(inputarray[1])
			r = int(inputarray[2])
			mCoffee = []
			for _ in range(m):
				mCoffee.append(int(sys.stdin.readline()))
			mBakery = []
			for _ in range(p):
				mBakery.append(int(sys.stdin.readline()))

			ans = int(sys.stdin.readline())
			ret = calculate(m, mCoffee, p, mBakery, r)
			if ans != ret:
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	#sys.stdin = open('sample_input.txt', 'r')
	inputarray = sys.stdin.readline().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run() else 0
		print("#%d %d" % (testcase, score), flush = True)