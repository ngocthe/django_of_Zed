# myapp/models.py
from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return self.file.name.split("/")[-1]

    def __str__(self):
        return f'{self.filename()} - {self.upload_time}'


class User(models.Model):
    userID = models.CharField(max_length=10, null=False, unique=True)
    userName = models.CharField(max_length=50, null=False)
    userPW = models.CharField(max_length=30, null=False)
    userMail = models.CharField(max_length=50, null=False)
    userPhone = models.CharField(max_length=50, null=False)
    userDep = models.CharField(max_length=50, null=False)
    isAdmin = models.BooleanField(default=False)


class SWMember(models.Model):
    uDept = models.CharField(max_length=50, null=False)
    uFunction = models.CharField(max_length=50, null=False)
    uPosition = models.CharField(max_length=50)
    userID = models.CharField(max_length=10, null=False)
    uVietnameseName = models.CharField(max_length=50, null=False)
    uChineseName = models.CharField(max_length=50)
    uEnglishName = models.CharField(max_length=50, null=False)
    uLevel = models.CharField(max_length=50)
    uBirthday = models.CharField(max_length=50)
    uGender = models.CharField(max_length=50)
    uAddress = models.CharField(max_length=50)
    uUniversity = models.CharField(max_length=50)
    uMajor = models.CharField(max_length=50)
    uExperience = models.CharField(max_length=50)
    uLastCompany = models.CharField(max_length=50)
    uMail = models.CharField(max_length=50)
    uPhone = models.CharField(max_length=50)


class Meta:
    app_label = 'myapp'

