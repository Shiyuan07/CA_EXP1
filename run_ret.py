import os
import gzip

def test(nums):
	filelist = os.listdir("traces")
	for num in nums:
	    # os.system("mkdir "+str(num))
	    for file in filelist:
	        if file.endswith("out.trace.gz"):
	            try:
	                command = "time ./bin/CMPsim.usetrace.32 -threads 1 -t " \
	                		+"./traces/"+file+" -o ./"+str(num)+"/" \
	                		+file[:-13]+".stats -cache UL3:1024:64:16 -LLCrepl " \
	                		+str(num) \
	                		+" > "+"./"+str(num)+"/"+file[:-13]+".log" \
	                		+" 2>&1"
	                print command
	                # os.system(command)
	                break
	            except:
	                pass    

def parseRes(dir):
	filelist = os.listdir(dir)
	fout = open(dir+'res.txt','w')
	res = []
	anc = 'Per Thread Demand Reference Statistics'
	for file in filelist:
		if file.endswith('stats.gz'):
			id = file.split(".")[0]
			res.append((id,file))

	for id,file in res:
		print dir+file
		fin = gzip.GzipFile(dir+file)
		while 1:
			line = fin.readline()
			if anc in line:
				line = fin.readline()
				fout.write(id+':'+line.split('Miss Rate: ')[1])
				break

		fin.close()
	fout.close()
		

if __name__ == '__main__':
	parseRes("3/")