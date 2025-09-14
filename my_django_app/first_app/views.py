from django.http import HttpResponse
from django.views import View
import datetime
from django.views.generic import TemplateView


def home(request):
    return HttpResponse("Hello, Django!")

def not_found(request):
    return HttpResponse("404")

def current_datetime(request):
    now = datetime.datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Time</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background: linear-gradient(135deg, #ff7eb9, #ff65a3, #7afcff);
                font-family: Arial, Helvetica, sans-serif;
                color: #fff;
                text-align: center;
            }}
            .card {{
                background: rgba(0, 0, 0, 0.3);
                padding: 30px 50px;
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(10px);
            }}
            h1 {{
                font-size: 2.5rem;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.3rem;
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✨ Current Date & Time ✨</h1>
            <p>{now}</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)



class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home page!")

class NotFoundView(View):
    def get(self, request):
        return HttpResponse("404")