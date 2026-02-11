T = int(input())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for t in range(1, T+1):
    atoms = []
    N = int(input())
    atomSet = set()
    for i in range(N):
        atom = list(map(int, input().split()))
        atoms.append([atom[0]*2, atom[1]*2, atom[2], atom[3]])
        atomSet.add([atom[0], atom[1], atom[3]])
        
    for i in range(4000):
        for atom in atomSet:
            nextAtom = [atom[0]+dx[atom[2]], atom[1]+dy[atom[2]], atom[3]]
            if nextAtom in atomSet:
                
            
