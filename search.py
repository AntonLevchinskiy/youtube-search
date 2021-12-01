from youtubesearchpython import ChannelsSearch
import time
import random
import webbrowser

list_id = []
list_title = []

input_str = input("Введите запрос-> ")

start_time = time.time()

search = ChannelsSearch(input_str, limit = 20) #, region='US'

stop=0
k=0
for i in range(100):
	if stop==1:
		break

	results = search.result()
	search.next()

	for result in results['result']:
		if len(list_id)==100:
			stop=1
			break

		if result['id'] in list_id:
			continue
			
		list_id.append(result['id'])
		list_title.append(result['title'])

		print("  Progress {:2.2%}".format(k / len(list_id)), end="\r")
		k += 1


r = random.randint(0,99)

k=1
for i in range(len(list_id)):
	print(str(k)+"."+list_title[i]+" - "+list_id[i])
	k += 1 

print()
print("Канал №"+str(r)+": "+str(list_title[r])+" - "+str(list_id[r]))
print()
print("Время выполнения: "+str(time.time()-start_time)+"s.")

webbrowser.open("https://www.youtube.com/channel/"+str(list_id[r]))