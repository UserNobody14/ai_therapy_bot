from django.urls import path
from web.views import index, get_response, get_audio

app_name = "web"
urlpatterns = [
    path("", index, name="mainpage"),
    path("get_message", get_response, name="response_creator"),
    path("get_audio/<uuid:message_id>", get_audio, name="get_audio"),
]
