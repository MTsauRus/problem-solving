import sys
from solution import init, writeWord, eraseWord

CMD_INIT = 1
CMD_WRITE = 2
CMD_ERASE = 3

def run():
    query = int(input())
    ok = False
    for i in range(query):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            M = int(next(input_iter))
            init(N, M)
            ok = True
        elif cmd == CMD_WRITE:
            mId = int(next(input_iter))
            mLen = int(next(input_iter))
            ret = writeWord(mId, mLen)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
        elif cmd == CMD_ERASE:
            mId = int(next(input_iter))
            ret = eraseWord(mId)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
    return ok

if __name__ == '__main__':
    # sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)