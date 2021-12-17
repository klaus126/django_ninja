from ninja import NinjaAPI

api = NinjaAPI()

@agi.get("/hello")
def hello(request):
    return "Hello world"