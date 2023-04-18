from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
# Create your views here.

def users(request):
    #pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json
    users = response.json()
    
    # print(users)
    return render(request, 'users.html',{'users': users})

def new(request):
    # response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    
    if request.method == 'POST':
        pass
    
    return render(request, 'todo.html', {'data':response.json()})
    return HttpResponse(response.json())

    
    
def category(request):
    response = requests.get('http://127.0.0.1:8000/category/')
    print(response)
    category = response.json()
    print(category[0])
    # print(category)

    
    return render(request, 'category.html',{'category': category})

def category_post(request):
    if request.method == "POST":
        print('here')
        category = request.POST.get('category')
        parent = request.POST.get('parent')
        
        data = {
            'category': category,
            'parent': parent,
        }
        
        requests.post('http://127.0.0.1:8000/category/', json=data)
        
    return render(request, 'post_cat.html')