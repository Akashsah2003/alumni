from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all().order_by("-date_time_created")
    context = {
        'blogs': blogs
    }
    print(context.get('blogs'))
    return render(request, "blog/home.html", context)

# Endpoints:

def view_blog(request, blogid):

    requested_blog = Blog.objects.get(id=blogid)

    if not requested_blog:
        return HttpResponse("Requested Blog does not exist")
    print(requested_blog)
    DATA = {
        "blog_id": requested_blog.id,
        "author": requested_blog.author,
        "date_time_created": requested_blog.date_time_created,
        "title": requested_blog.title,
        "description": requested_blog.description,
        "image": requested_blog.image
    }
    print(blogid)


    return render(request, "blog/viewblog.html", DATA)

def create_blog(request):
    if request.method == 'POST':
        try:
            author = request.user
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.POST.get('image')

            print(author, title, description)

            created_blog = Blog.objects.create(
                author=author,
                title=title,
                description=description,
                image = image
            )

            created_blog.save()
        except Exception as e:
            return HttpResponse("Bad Request")
            print("Error is", e)
    return render(request, "blog/createblog.html")