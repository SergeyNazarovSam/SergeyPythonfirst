from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from main.handlers import index, error_test
from tasks.lesson01 import task103
from tasks.lesson03 import task301, task302, task303, task304, task305, task306, task307, task309, task310, task311
from tasks.lesson04 import task402


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index.handler_django),
    path("e/", error_test.handler),
    path("tasks/1/103/", task103.handler_django),
    path("tasks/3/301/", task301.handler_django),
    path("tasks/3/302/", task302.handler_django),
    path("tasks/3/303/", task303.handler_django),
    path("tasks/3/304/", task304.handler_django),
    path("tasks/3/305/", task305.handler_django),
    path("tasks/3/306/", task306.handler_django),
    path("tasks/3/307/", task307.handler_django),
    path("tasks/3/309/", task309.handler_django),
    path("tasks/3/310/", task310.handler_django),
    path("tasks/3/311/", task311.handler_django),
    path("tasks/4/402/", task402.handler),
    path("api/v1/tasks/402/", task402.handler_api),
]
