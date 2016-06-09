from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render
import MySQLdb

 
 
def home(request):   
    return render(request,'index.html',{})

def request_page(request):
    if(request.POST.get('mybtn')):
         name = request.POST.get('username')
         password = request.POST.get('password')
	 print name
	 db = MySQLdb.connect("localhost","root","1234","EComm_DB")
	 cursor = db.cursor()
	 sql = "select * from register_info where email = '%s'" %(name)
	 cursor.execute(sql)
	 results = cursor.fetchall()
         for row in results:
            fname = row[4]
            print fname
            if fname == password:
              return render(request,'clicked.html')
	 return render(request,'index.html',{})

def show(request):
	db = MySQLdb.connect("localhost","root","1234","EComm_DB")
	cursor = db.cursor()
	sql = "select * from product_info"
	cursor.execute(sql)
	names = [row[3] for row in cursor.fetchall()]
    	return render(request,'clicked.html',{'names':names})
