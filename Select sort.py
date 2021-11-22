def select_sort(origin_item, comp=lambda a, b : a < b):
	item = origin_item[:]
	for i in range(len(item)-1):
		min_index = i
		for j in range(i+1, len(item)):
			if comp(item[j], item[min_index]):
				min_index = j
		item[i], item[min_index] = item[min_index], item[i]
	return item
 
def main():
	item = [34, 87, 3, 48, 98, 19, 82]
	result = select_sort(item)
	print(result)
 
if __name__ == '__main__':
	main()