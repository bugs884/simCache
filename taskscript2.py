import subprocess
import numpy as np
import csv
import matplotlib.pyplot as plt

Listplot = np.array([])
Listplotacross =np.array([])
benchmark=["fibonacci","matmul","pi","whetstone","memcopy"]
#Create Subprocesses for each config and add output in Log
for x in range(0,5):
	for i in range(0,5):
	  #for j in range(0,8):
	  	ass=2**i
	  	bsize =32
	  	nsets = 8192/ (32*ass)      #(2**j)*1024
	  	argv = "mycache:"+str(nsets)+":"+str(bsize)+":"+str(ass)+":l"
	  	resultarg = "results/log"+str(i)+benchmark[x]+".out"
	  	bench = "benchmarks/"+benchmark[x]
	  	inp = ["./sim-cache", "-redir:sim",resultarg,"-cache:dl1", argv,"-cache:il1", "il1:512:32:1:l", "-cache:dl2" ,"ul2:1024:64:4:l", "-cache:il2","dl2",bench]
	  	#print inp
	  	subprocess.Popen(inp).communicate()
#Extract Missrate from logs and create a list
X_Axis= np.array([1,2,3,4,5])
my_xticks = ['1way','2way','4way','8way','16way']
for x in range(0,5):
	bench= benchmark[x]
	
	for n in range (0,5):
		path = "results/log" +str(n)+bench+".out"
		#print path
		log =open(path,'r')	
		for line in log:
			if line.find('mycache.miss_rate') == 0:
	#	  		print(float(line.split()[1]))
		 		Listplot= np.append(Listplot,float((line.split()[1])))
		 		Listplotacross=np.append(Listplotacross,float((line.split()[1])))

    
	plt.bar(X_Axis,Listplot)	
	plt.ylabel('Miss Rate')
	plt.xlabel('Set Associativity')
	plt.xticks(X_Axis, my_xticks)
	plt.title(bench, fontsize=16)
	plt.show()  
	Listplot = np.array([])
	
#print Listplotacross
splitarray=np.array_split(Listplotacross,5)
#plt.plot(X_Axis,Listplot)

plt.plot(X_Axis,splitarray[0])
plt.plot(X_Axis,splitarray[1])
plt.plot(X_Axis,splitarray[2])
plt.plot(X_Axis,splitarray[3])
plt.plot(X_Axis,splitarray[4])
plt.ylabel('Miss Rate')
plt.xlabel('Set Associativity')
plt.xticks(X_Axis, my_xticks)
plt.title("Across Benchmarks", fontsize=16)
plt.legend(['Fibonacci','Matmul','Pi','Whetstone','Memcopy'], loc='upper right')
plt.show()  

#Create a plot for comparing Benchmarks
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
#fig.savefig('Graphs/step1/Across.png')
#print Listplot
# with open('Step1.csv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(Listplot)
