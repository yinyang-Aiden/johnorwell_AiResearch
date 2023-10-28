from bs4 import BeautifulSoup
import os,requests
filename_1=input('请输入要读取的字典名？\n')
filename_2=filename_1 + '.txt'
f=open(filename_2)
urls=[]
line=f.readline()
while line:
	n_tmp=len(line)-1
	urls.append(line[:n_tmp])
	line = f.readline()
f.close()
print(urls)
n=0
urls_len=len(urls)
for url in urls:
	n+=1
	r1=requests.get(url,'lxml')
	soup=BeautifulSoup(r1.text,'lxml')
	T=soup.find_all('p')
	print("进度："+str(n)+'/'+str(urls_len))
	for i in T:
		outfile=filename_1+'_resu.txt'
		fo=open(outfile,'a',encoding='utf-8')
		fo.write(i.text)
		fo.close()



