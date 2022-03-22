import sys
sys.stdin = open("baek1620.txt")

"""
리스트랑, dict를 같이 활용하자!
숫자 => 포켓몬는 리스트
포켓몬 => 숫자는 dict를!
"""

N, M = map(int, input().split())
pokemons = [0] * N
poke_dict = {}
digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(0, N):
    pokemon = input()
    poke_dict[pokemon] = i+1
    pokemons[i] = pokemon
for i in range(0, M):
    now = input()
    # 숫자 들어온것
    if now[0] in digit:
        num = int(now)
        # 인덱스 저장이므로 -1
        print(pokemons[num-1])
    # 포켓몬 이름
    else:
        print(poke_dict[now])

