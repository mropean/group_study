import sys
N = int(sys.stdin.readline())
_list_1 = list(map(int, sys.stdin.readline().split())) # 입력받은 리스트

_list_2 = [0] * N # Temp용 리스트
_list_2[0] = _list_1[0]
for num in range(1, N):
    _list_2[num] = max(_list_1[num], _list_2[num-1] + _list_1[num])
            
print(max(_list_2))
