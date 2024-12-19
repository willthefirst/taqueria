from django.db import models

class TimestampedModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

class AgeGroup(models.TextChoices):
  CHILDREN_0_5 = '0-5', 'Children (0 to 5)'
  CHILDREN_6_10 = '6-10', 'Children (6 to 10)'
  PRETEENS_11_13 = '11-13', 'Preteens (11 to 13)'
  ADOLESCENTS_14_18 = '14-18', 'Adolescents (14 to 18)'
  YOUNG_ADULTS_19_24 = '19-24', 'Young Adults (19 to 24)'
  ADULTS_25_64 = '25-64', 'Adults (25 to 64)'
  OLDER_ADULTS_65_PLUS = '65+', 'Older Adults (65 +)'
  
class Post(TimestampedModel):
  state = models.CharField(max_length=2)
  age_group = models.CharField(
    max_length=80,
    choices=AgeGroup.choices,
    default=AgeGroup.ADULTS_25_64,
  )
  
  def __str__(self):
    return f"{self.state} ({self.get_age_group_display()})"