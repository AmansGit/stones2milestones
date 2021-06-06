from django.db import models

# Create your models here.
class Student(models.Model):
	id = models.AutoField(primary_key=True, auto_created=True)
	name = models.CharField(max_length=200)
	grade_choice = (
		("O", "O"),
		("A", "A"),
		("B", "B"),
		("C", "C"),
		("D", "D"),
		("F", "F")
	)
	grade = models.CharField(max_length=1,choices=grade_choice)
	status_choices = (
		("Enabled", "Enabled"),
		("Disabled", "Disabled")
	)
	status = models.CharField(max_length=8, choices=status_choices)

	def __str__(self):
		return self.name


class Teacher(models.Model):
	id = models.AutoField(primary_key=True, auto_created=True)
	name = models.CharField(max_length=100)
	experience = models.IntegerField()
	student_assigned = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		return self.name