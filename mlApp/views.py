from django.shortcuts import render

from joblib import load
model = load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        age = request.POST['age']
        sex = request.POST['sex']
        bp = request.POST['bp']
        cholesterol = request.POST['cholesterol']
        na_to_k = request.POST['na_to_k']

        y_pred = model.predict([[age, sex, bp, cholesterol,na_to_k]])
        if y_pred[0] == 0:
            y_pred = 'DrugY'
        elif y_pred[0] == 1:
            y_pred = 'drugX'
        elif y_pred[0] == 2:
            y_pred = 'drugA'
        elif y_pred[0] == 3:
            y_pred = 'drugC'
        else:
            y_pred = 'drugB'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')
