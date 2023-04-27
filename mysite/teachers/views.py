from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

from .models import Teacher

faker = Faker()


def generate_teachers(request):
    teacher = Teacher.objects.create(
        first_name=faker.first_name(), last_name=faker.last_name()
    )
    return HttpResponse(
        f"""
            <p>A new teacher added: {teacher.first_name} {teacher.last_name}<p>
        """
    )


def teachers_list_view(request):
    teachers = Teacher.objects.all()
    return render(request, "index.html", {"teachers": teachers})
