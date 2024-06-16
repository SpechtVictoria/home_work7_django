from django.http import HttpRequest, HttpResponse


def greeting_user(request: HttpRequest, your_name: str) -> HttpResponse:
    template = f"<h1>Hello, {your_name}</h1"

    return HttpResponse(template)

