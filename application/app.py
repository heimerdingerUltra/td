import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

settings.configure(
    DEBUG=True,
    SECRET_KEY="django-demo-local-only",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[],
)

def accueil(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Django dans Docker</title>
<style>
body {font-family:Arial,sans-serif;background:#0f172a;color:white;display:grid;place-items:center;min-height:100vh;margin:0;}
main {text-align:center;padding:40px;background:#1e293b;border-radius:20px;}
h1 {color:#38bdf8;}
</style>
</head>
<body><main><h1>Bienvenue sur Django !</h1>
<p>Cette page est servie par une application Django dans Docker.</p>
<p>Application réalisée par M. TRAORE.</p></main></body>
</html>""")

urlpatterns = [path("", accueil)]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
