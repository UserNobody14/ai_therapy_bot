from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import web.TTS as el
from web.therapist_bot_openai import send_message


# Create your views here.
@csrf_exempt
def index(request):
    return JsonResponse({"message": "hello!"}, status=200)


@csrf_exempt
def get_response(request):
    if request.method == "GET":
        return HttpResponseRedirect(reverse("web:index"))
    elif request.method == "POST":
        user_input = json.loads(request.body)
        past_messages = user_input["past_messages"]
        current_message = user_input["current_message"]
        # send to openAI
        bot_voice_message = None
        bot_voice_message = send_message(current_message)
        # send to elevenlabs code
        msg_id = el.create_voice_message(bot_voice_message)
        # send to front end
        response_data = {
            "audio_file": f"http://localhost:8000/get_audio/{msg_id}",
            "bot_message": bot_voice_message,
        }
        resp = JsonResponse(response_data, status=200)
        # add CORS headers
        resp["Access-Control-Allow-Origin"] = "*"
        return resp


@csrf_exempt
def get_audio(request, message_id):
    if request.method == "GET":
        file = open(f"{message_id}.mp3", "rb").read()
        respo = HttpResponse(file, content_type="audio/mpeg")
        respo["Content-Disposition"] = f"attachment; filename={message_id}.mp3"
        return respo
    else:
        return HttpResponseRedirect(reverse("web:index"))
