#coding=utf-8     
#定义求质数的函数 
def getprim(n):  
#我们从3开始，提升效率，呵呵，微乎其微啦     
	p=3    
	x=0    
	while(x<n):         
		result=True         
		for i in range(2,p-1):             
			if(p%i==0):                 
				result=False         
		if result==True:             
			x=x+1            
			rst=p 
#注意:这里加2是为了提升效率，因为能被双数肯定不是质数。         
		p+=2    
	print(rst)      
#调用函数 
getprim(1000)


path=path+..


django
path=path+djangoPath