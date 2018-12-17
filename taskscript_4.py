import subprocess
import numpy as np
import csv
import matplotlib.pyplot as plt

Listplot = np.array([])
Locplot = np.array([])
benchmark=["fibonacci","matmul","pi","whetstone","memcopy"]

#Create Subprocesses for each config and add output in Log
for x in range(0,5):
	bench = "benchmarks/"+benchmark[x]
  	resultarg = "results4/log"+"0"+benchmark[x]+".out"
  	inp = ["./sim-cache","-redir:sim",resultarg, "-cache:dl1","dl1:16:32:16:l", "-cache:il1" ,"dl1" ,"-cache:dl2" ,"none" ,"-cache:il2" ,"none",  bench]
  	subprocess.Popen(inp).communicate()
  	resultarg = "results4/log"+"1"+benchmark[x]+".out"
  	inp = ["./sim-cache","-redir:sim",resultarg, "-cache:dl1","dl1:16:32:16:f", "-cache:il1" ,"dl1" ,"-cache:dl2" ,"none" ,"-cache:il2" ,"none",  bench]
  	subprocess.Popen(inp).communicate()
  	resultarg = "results4/log"+"2"+benchmark[x]+".out"
	inp = ["./sim-cache","-redir:sim",resultarg, "-cache:dl1","dl1:16:32:16:r", "-cache:il1" ,"dl1" ,"-cache:dl2" ,"none" ,"-cache:il2" ,"none",  bench]
  	subprocess.Popen(inp).communicate()

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        print height
        ax.text(rect.get_x() + rect.get_width()/2.,1.01*height,'%.4f' % float(height),ha='center', va='bottom',fontsize=10 )

	  	#print inp
# 	  	subprocess.Popen(inp).communicate()
# #Extract Missrate from logs and create a list
X_Axis= np.array([1,2,3])
my_xticks = ['LRU','FIFO','Random']
for x in range(0,5):
	bench= benchmark[x]
	#print bench
	for n in range (0,3):
		path = "results4/log" +str(n)+bench+".out"
		#print path
		log =open(path,'r')	
		for line in log:
			if line.find('dl1.miss_rate') == 0:
	#	  		print(float(line.split()[1]))
		 		Listplot= np.append(Listplot,float((line.split()[1])))
		 		Locplot= np.append(Locplot,float((line.split()[1])))
	fig, ax = plt.subplots()
	rect1=ax.bar(X_Axis,Locplot)
	ax.set_ylabel('Miss Rate')
	ax.set_xlabel('Replacement Policy')
	ax.set_title(bench, fontsize=16)
	ax.set_xticks(X_Axis)
	ax.set_xticklabels(my_xticks)
	#plt.legend(['8B', '16B', '32B', '64B'], loc='upper right')
	autolabel(rect1)
	plt.show()  
	Locplot = np.array([])
    #Plot grapgs for each Benchmark
#print Listplot
splitarray=np.array_split(Listplot,5)
width = 0.1
#print splitarray
fig, ax = plt.subplots()
ax.bar(X_Axis,splitarray[0],width)
ax.bar(X_Axis+width,splitarray[1],width)
ax.bar(X_Axis+width+width,splitarray[2],width)
ax.bar(X_Axis+width+width+width,splitarray[3],width)
ax.bar(X_Axis+width+width+width+width,splitarray[4],width)

ax.set_ylabel('Miss Rate')
ax.set_xlabel('Replacement Policy')
ax.set_xticks(X_Axis, my_xticks)
ax.set_title('Replacement Policy Across Benchmarks', fontsize=16)
ax.set_xticks(X_Axis + (width*2) / 2)
ax.set_xticklabels(my_xticks)
ax.legend(['fibonacci','matmul','pi','whetstone','memcopy'], loc='upper right')
plt.show()  
#Listplot = np.array([])
# #Create a plot for comparing Benchmarks
# X_Axis=np.array([1,2,3,4,5])
# my_xticks = ['Fibonacci','Matmul','Pi','Whetstone','Memcopy']
# for x in range(0,5):
# 	bench = benchmark[x]
# 	path = "results/log0"+bench+".out"
# 	log =open(path,'r')	
# 	for line in log:
# 		if line.find('mycache.miss_rate') == 0:
# 	#	  		print(float(line.split()[1]))
# 	 		Listplot= np.append(Listplot,float((line.split()[1])))
# plt.bar(X_Axis,Listplot)
# plt.ylabel('Miss Rate')
# plt.xlabel('Benchmarks')
# plt.xticks(X_Axis, my_xticks)
# plt.title("Miss Rate comparision accross Benchmarks(Sets=1K , Block Size = 8B)", fontsize=10)
# plt.show()
# #fig.savefig('Graphs/step1/Across.png')
# #print Listplot
# # with open('Step1.csv', 'wb') as myfile:
# #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# #     wr.writerow(Listplot)
