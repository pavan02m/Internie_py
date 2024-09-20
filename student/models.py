from django.db import models

# Create your models here.
class Candidate(models.Model):
    student_name = models.CharField(max_length=100)
    student_email=models.CharField(max_length=100)
    pass1=models.CharField(max_length=10,default="")
    username=models.CharField(max_length=100,unique=True)
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=7000)
    college_name = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=2)

    def __str__(self):
        return self.student_name

    # def get_absolute_url(self):
    #     return reverss("Student_detail", kwargs={"pk": self.pk})
