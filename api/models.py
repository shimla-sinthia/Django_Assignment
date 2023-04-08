from django.db import models

size_choice = (
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
)
friendliness_choice = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)

trainability_choice = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)
sheddingamount_choice = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)

exerciseneeds_choice = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)


class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=size_choice)
    friendliness = models.CharField(max_length=10, choices=friendliness_choice)
    trainability = models.CharField(max_length=10, choices=trainability_choice)
    sheddingamount = models.CharField(max_length=10, choices=sheddingamount_choice)
    exerciseneeds = models.CharField(max_length=10, choices=exerciseneeds_choice)

    def __str__(self):
        return self.name

gender_choices = (
    ("male", "male"),
    ("female", "female"),
    ("None", "None"),
)


class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=gender_choices)
    color = models.CharField(max_length=30)
    favorite_food = models.CharField(max_length=40)
    favorite_toy = models.CharField(max_length=30)

    def __str__(self):
        return self.name