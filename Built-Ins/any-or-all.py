n = int(input())
n_list = input().split(" ")
print(all(int(i) >= 0 for i in n_list) and any(j == j[::-1] for j in n_list))