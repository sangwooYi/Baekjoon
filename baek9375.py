import sys
sys.stdin = open("baek9375.txt")

"""
조합의 기본문제!    
n종류의 옷들이 있으면
ai = 같은 옷종류의 옷의 갯수
nC1*(a1) + nC2*(a1 * a2) + nC3*(a1*a2*a3) .. .. nCn(a1*a2*...*an)
기본은 위에처럼 푸는건데
위처럼 풀면 시간초과네 ㅡㅡ?
의상의 종류가 30종류까지 있으므로 당연히 시간초과!

조합공식은
nCr = nCn-r
nCr-1 + nCr = n+1Cr+1 이 있긴함
어차피 30가지까지 있어서 오래걸릴거같은데 2**20 만 해도 100만이다. (20자리)'


중요! 
a가지의 A ,  b가지의 B , c 가지의 C ... n 가지의 N 의 종류를 조합하여 만들수 있는 모든 경우의수는
(a+1) * (b+1) * (c+1) * ... (n+1) -1 이된다! 
(각각 경우에서 안고를때, 1개고를때, 2개고를떄 .. 이런식으로 해서
안고르는 경우에 대해서 경우가 1가지씩  추가되는것!)
그리고 모두다 안고르는 경우는 해당 안되므로 최종결과에서 1을 빼주면 우리가 원하는답이다! 
"""



T = int(input())
for tc in range(1, T+1):
    N = int(input())

    cloth_dict = {}
    category = []
    idx = 0
    for i in range(0, N):
        temp = list(input().split())
        if temp[1] in cloth_dict.keys():
            category[cloth_dict[temp[1]]] += 1
        else:
            category.append(1)
            cloth_dict[temp[1]] = idx
            idx += 1 
    count = 1
    for i in range(0, len(category)):
        count *= (category[i]+1)
    ans = count-1
    print(ans)