from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

#Create your models here.
class ExamBlocks(models.Model):
    block_no = models.CharField(max_length=25)
    capacity = models.IntegerField()
    occupied = models.IntegerField()

    def __str__(self) -> str:
        return self.block_no

class Department(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class Exam(models.Model):
    sub_name = models.CharField(max_length=255)
    sub_code = models.CharField(max_length=25)
    exam_date = models.DateField()
    exam_time = models.TimeField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.sub_name + "\t" + self.sub_code


class StudentDetails(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.usn


class AssignedBlock(models.Model):
    block = models.ForeignKey(ExamBlocks, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{str(self.block)}"
    
class TakeAttendance(models.Model):
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.student) +"--"+ str(self.exam)+"--"+str(self.datetime)
    
@receiver(post_delete, sender=AssignedBlock)
def update_capacity(sender, instance, **kwargs):
    obj = ExamBlocks.objects.get(block_no=instance.block)
    obj.capacity += 1
    obj.occupied -= 1
    obj.save()
    
@receiver(post_save, sender=AssignedBlock)
def update_capacity(sender, instance, **kwargs):
    obj = ExamBlocks.objects.get(block_no=instance.block)
    obj.capacity -= 1
    obj.occupied += 1
    obj.save()
