from oneM2M_functions import *
import time
import random
from flask import Flask, render_template, redirect, url_for, jsonify
uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"
ae = "Indoor-Air-Pollution"
cnt = "Data"

headers = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
}

def CreateContainers():
    uri_ae = uri_cse+"/"+ae
    create_ae(uri_cse, ae)
    create_cnt(uri_ae,cnt)
    create_cnt(uri_ae,"Data_Description")
    create_data_cin(uri_ae+"/Data_Description","[Temperature, Humidity, CO2, VOC-Index, PM-2.5, PM-10]")
# CreateContainers()
for i in range(1000):
    n1 = random.randint(0,22)
    n2 = random.randint(0,22)
    n3 = random.randint(0,22)
    n4 = random.randint(0,22)
    n5 = random.randint(0,22)
    n6 = random.randint(0,22)

    create_data_cin(uri_cse+"/"+ae+"/"+cnt,[n1,n2,n3,n4,n5,n6])
    time.sleep(5)