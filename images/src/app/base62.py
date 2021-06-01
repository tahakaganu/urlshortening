
map = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def toBase62(id: int):
	result = ""
	rest = 0
	while(id > 0):
		rest = id % 62
		result = map[rest] + result
		id = int(id / 62)
	return result

def toBase10(id: str):
	i =0
	total = 0
	while(i < len(id)):
		counter = i + 1
		mapped = map.index(id[i])
		total += (mapped * (62 ** (len(id) - counter)))
		i += 1
	return total
