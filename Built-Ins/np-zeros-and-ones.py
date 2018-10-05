import numpy

numbers_list = tuple(map(int, input().split()))
print(numpy.zeros(numbers_list, dtype = numpy.int))
print(numpy.ones(numbers_list, dtype = numpy.int))