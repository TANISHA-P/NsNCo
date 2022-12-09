from django.shortcuts import render

posts = [
    {
        'author' : 'Tanisha',
        'date_posted' : '1 December 2022',
        'content' : 'First Post',
    },
    {
        'author' : 'Divya',
        'date_posted' : '7 December 2022',
        'content' : 'Second Post',
    }
] #list of dictionaries.

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html',context) #All html files must be in templates folder.

def about(request):
    return render(request, 'blog/about.html')