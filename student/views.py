from django.shortcuts import render, redirect
from student.models import Candidate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def register_student(request):
    if request.method == "POST":
        print(request.POST)
        student_name = request.POST['name']
        student_email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        username = request.POST['username']
        # phno = request.POST['phone']
        # address = request.POST['address']
        # college = request.POST['college']
        # cgpa = request.POST['cgpa']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "User with this username already exists, please try a different one.")
            return redirect('student:sign-up')

        # Check if the email already exists
        if Candidate.objects.filter(student_email=student_email).exists():
            messages.error(request, "User with this email ID already exists!")
            return redirect('student:sign-up')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            return redirect('student:sign-up')
        
        user = User(username=username, email=student_email)
        user.set_password(pass1)
        user.save()

        # Create and save the candidate
        candidate = Candidate(
            student_name=student_name,
            student_email=student_email,
            pass1=user.password,
            username=username,
            # phone_no=phno,
            # address=address,
            # college_name=college,
            # cgpa=cgpa
        )
        candidate.save()
        user = authenticate(request, username=student_email, password=pass1)

        return redirect('index')
    
    return render(request, 'userauth/student_registration.html')
