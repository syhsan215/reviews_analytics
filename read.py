data = []
count = 0

with open("reviews.txt","r")as f:
	for line in f:
		count += 1
		data.append(line.strip())
		#if count % 10000 == 0:
			#print(len(data))



print("讀取完了，總共有",len(data),"筆留言")


sum_len = 0
for d in data:
	sum_len += len(d)



print("每筆留言平均長度為：",sum_len/len(data))


# print(data[0])