if __name__ == '__main__':
	n = int(input())
	# sorted in descending order
	arr = sorted(map(int, input().split()), reverse=True)
	second = arr[0]
	for i in range(0, len(arr)):
		if arr[i] != second:
			second = arr[i]
			break
	print(second)