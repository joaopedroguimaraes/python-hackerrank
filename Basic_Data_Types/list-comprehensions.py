if __name__ == '__main__':
	x = int(input()) + 1
	y = int(input()) + 1
	z = int(input()) + 1
	n = int(input())

	print([[a,b,c] for a in range(0,x) for b in range(0,y) for c in range(0,z) if a+b+c != n])