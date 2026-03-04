import sys

from 경유지운송_solution import init, add, calculate

CMD_INIT = 100
CMD_ADD = 200
CMD_CALC = 300

def run():
	q = int(sys.stdin.readline())
	okay = False

	sCityArr = []
	eCityArr = []
	mLimitArr = []

	for i in range(q):
		cmd = int(sys.stdin.readline().split()[0])

		if cmd == CMD_INIT:
			inputarray = sys.stdin.readline().split()
			n = int(inputarray[1])
			k = int(inputarray[3])
			for _ in range(k):
				road = sys.stdin.readline().split()
				sCityArr.append(int(road[1]))
				eCityArr.append(int(road[3]))
				mLimitArr.append(int(road[5]))

			init(n, k, sCityArr, eCityArr, mLimitArr)
			okay = True
		elif cmd == CMD_ADD:
			inputarray = sys.stdin.readline().split()
			sCity = int(inputarray[1])
			eCity = int(inputarray[3])
			mLimit = int(inputarray[5])
			add(sCity, eCity, mLimit)
		elif cmd == CMD_CALC:
			inputarray = sys.stdin.readline().split()
			sCity = int(inputarray[1])
			eCity = int(inputarray[3])
			m = int(inputarray[5])
			mStopover = []
			for _ in range(m):
				mStopover.append(int(sys.stdin.readline().split()[1]))

			ans = int(sys.stdin.readline().split()[1])
			ret = calculate(sCity, eCity, m, mStopover)
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