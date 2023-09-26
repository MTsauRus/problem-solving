while True:
    cnt = 0
    tmp = input().strip()
    if tmp[-1] == "#":
        break
    for ch in tmp:
        if ch in ["i", "e", "a", "o", "u"]:
            cnt += 1
    print(cnt)