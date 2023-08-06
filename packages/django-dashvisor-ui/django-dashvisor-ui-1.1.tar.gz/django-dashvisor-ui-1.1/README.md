# django-dashvisor
Django supervisor dashboard UI

Requirements:
    
    Django >= 1.11

    
Install:

    pip install django-dashvisor-ui
    
Instructions
============

Add to django installed apps:

    INSTALLED_APPS = [
        ...
        dashvisor
    ]


Configure urls:

    url(r'^/dashboard/', include('dashvisor.urls'))
 

Execute on web browser:
    
    http://localhost:8000/dashboard/


![dashboard](https://github.com/alexsilva/django-dashvisor-ui/blob/master/dashvisor/ui/dashboard.png)
