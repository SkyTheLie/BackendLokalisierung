from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

class lokalisierungView(viewsets.ModelViewSet):

    def fingerprints(request: Request):
        #Aus der tabelle lesen mit models.fp
        #Berechnen und denn nächsten nachbarn wieder geben
        data = "test"
        return HttpResponse(data)