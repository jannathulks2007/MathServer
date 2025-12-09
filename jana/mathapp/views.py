from django.shortcuts import render 
def Vehicle(request):
    distance=float(request.POST.get('distance',0))
    fuel=float(request.POST.get('fuel',0))
    mileage=distance/fuel if request.method=='POST' else 0
    print("Distance_Travelled(in km):",distance)
    print("Amount_Of_Fuel(in litre):",fuel)
    print("Vehicle's_Mileage:",mileage)
    return render(request,'mathapp/math.html',{'distance':distance,'fuel':fuel,'mileage':mileage})