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
            <h1>{post['id']} - {post['title']}</h1>
            <p>{post['content']}</p>
        </div>
        """
    return HttpResponse(html)
