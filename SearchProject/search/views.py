from django.shortcuts import render,get_object_or_404
from .forms import InputForm
from .models import Input
import time
import requests

# view for home page
def home(request):	
	if request.method == 'POST':		
		form = InputForm(request.POST)
		query = request.POST['query']		
		try: 
			from googlesearch import search 
		except ImportError:  
			print("No module named 'google' found")
		output = search(query, tld="co.in", num=10, stop=10, pause=2)		
		outputlist=[]
		for j in output: 
			print(outputlist.append(j))		
		return render(request,'home.html',{'output':outputlist,'form':form})
	else:
		form = InputForm()
	return render(request,'home.html',{'form':form})