# Ex.04 Design a Website for Server Side Processing
## Date:10/12/25

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html
<html>
    <head>
        <title>
            Vehicle'S Mileage
        </title>
        <style>
            body{
                background-color:rgb(250, 207, 221); 
            }
            .box{
                margin-left:420px;
                margin-top:100px;
                background-color:rgb(255, 130, 170);
                border: dashed 5px rgb(105, 5, 5);
                width: 350px;
                height:auto;
                
            }
        </style>
    </head>
    <body>
        <div class="box">
             <h2 align="center">Vehicle Mileage</h2>
             <h4 align="center">A.Jannathul Shaban</h4>
             <h4 align="center">25015672</h4>
            <form method="post" align="center">
                {% csrf_token %}
                <label>Distance Travelled(in km):</label>
                <input type="text" name="distance" value="{{ distance }}">
                <br><br>
                <label>Amount Of Fuel(in litre):</label>
                <input type="text" name="fuel" value="{{ fuel }}">
                <br><br>
                <input type="submit" value="Calculate">
                <br><br>
                <label>Vehicle's Mileage:</label>
                <input type="text" name="mileage" value="{{mileage}}">
                


            </form>

        </div>
    </body>
</html>

views.py
from django.shortcuts import render 
def Vehicle(request):
    distance=float(request.POST.get('distance',0))
    fuel=float(request.POST.get('fuel',0))
    mileage=distance/fuel if request.method=='POST' else 0
    print("Distance_Travelled(in km):",distance)
    print("Amount_Of_Fuel(in litre):",fuel)
    print("Vehicle's_Mileage:",mileage)
    return render(request,'mathapp/math.html',{'distance':distance,'fuel':fuel,'mileage':mileage})

urls.py
from django.contrib import admin 
from django.urls import path
from mathapp import views
urlpatterns=[path('', views.Vehicle,name='Vehicle')]

```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (29).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (28).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
