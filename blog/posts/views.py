from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post"},
    {"id": 2, "title": "Second Post", "content": "This is the second post"},
    {"id": 3, "title": "Third Post", "content": "This is the third post"},
]


# Create your views here.
def home(request):
    html = ""
    for post in posts:
        html += f"""
        <div>
            <a href = "/posts/{post['id']}">
            <h1>{post['id']} - {post['title']}</h1></a>
            <p>{post['content']}</p>
        </div>
        """
    return HttpResponse(html)


def post(request, id):
    post = next(post for post in posts if post["id"] == int(id))
    html = f"""
        <div>
            <h1>{post['id']} - {post['title']}</h1>
            <p>{post['content']}</p>
        </div>
    """
    return HttpResponse(html)
