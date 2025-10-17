from django.shortcuts import render

def employee_data(request):
    employees = [
        {'name': 'Jacob', 'job_title': 'Graphic Designer', 'salary': 45000, 'full_time': True},
        {'name': 'Jane Smith', 'job_title': 'Graphic Designer', 'salary': 45000, 'full_time': False},
        {'name': 'Alex Brown', 'job_title': 'Project Manager', 'salary': 70000, 'full_time': True},    
    ]
    return render(request, "employee_data.html", {"employees": employees})
