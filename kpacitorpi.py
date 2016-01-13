#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

import RPi.GPIO as GPIO
import time
import os

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

dir_frente	= GPIO.PWM(17, 100) #Direita Para Frente
dir_tras	= GPIO.PWM(22, 100) #Direita Para Tras
esq_frente	= GPIO.PWM(23, 100) #Esquerda Para Frente
esc_tras	= GPIO.PWM(27, 100) #Esquerda Para Tras 


@app.route("/")
def hello():
    return render_template('kpacitorpi.html')


# Movimenta o Robo
@app.route("/")
@app.route('/comando_kpacitorpi/<int:cod_movimentar>/', methods=['GET', 'POST'])
def comando_kpacitorpi(cod_movimentar):	
	if request.method == 'POST':
		if cod_movimentar == 1:
			movimentar("FRENTE")
		elif cod_movimentar == 2:
			movimentar("TRAS")
		elif cod_movimentar == 3:
			movimentar("ESQUERDA")
	 	elif cod_movimentar == 4:
	 		movimentar("DIREITA")	
		elif cod_movimentar == 5:
			movimentar("STOP")
		else	
			print "Ok, Movimentado"
	else:
		return render_template('kpacitorpi.html')


@app.route("/movimentar")
def movimentar(run):
	if run == 'FRENTE':
		dir_frente.start(20) #Duty Cycle de 20%
		esq_frente.start(18) #Duty Cycle de 20%
		dir_tras.stop()
		esc_tras.stop()

	elif run == 'TRAS':
		dir_tras.start(18) #Duty Cycle de 20%
		esc_tras.start(20) #Duty Cycle de 20%
		dir_frente.stop()
		esq_frente.stop()

	elif run == 'DIREITA':
		esq_frente.start(20) #Duty Cycle de 20%
		dir_tras.start(20) #Duty Cycle de 20%
		dir_frente.stop()
		esc_tras.stop()

	elif run == 'ESQUERDA':
		dir_frente.start(20) #Duty Cycle de 20%
		esc_tras.start(20) #Duty Cycle de 20%
		esq_frente.stop()
		dir_tras.stop()

	else:
		dir_frente.stop()
		esq_frente.stop()
		dir_tras.stop()
		esc_tras.stop()

# Funcao que 
def delay_info(time):
	for x in range(0, time):
		time.sleep(1)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)