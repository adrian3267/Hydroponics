from django.db import models
from certification.models import RequiredCertificationDocuments
from authentication.models import EmbracoProfile, SupplierProfile

class GroupOfCharacteristics(models.Model):
    evaluationreport = models.ForeignKey(RequiredCertificationDocuments, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.group_name

class Characteristics(models.Model):
    evaluationreport = models.ForeignKey(RequiredCertificationDocuments, on_delete=models.PROTECT)
    group = models.ForeignKey(GroupOfCharacteristics, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField(unique=True, default=0)
    characteristic = models.CharField(max_length=40, default='')
    coordinates = models.CharField(max_length=4, default='')
    type = models.CharField(max_length=5, default='')
    limits_type = models.CharField(max_length=20, default='')
    nominalValue = models.FloatField(default=0)
    lower_limit = models.FloatField(default=0)
    upper_limit = models.FloatField(default=0)
    target_cpk = models.FloatField(default=0)
    sample_size = models.IntegerField(default=0)

    def __str__(self):
        return self.characteristic

class Evaluation(models.Model):
    characteristic = models.ForeignKey(Characteristics, on_delete=models.PROTECT)
    evaluation_number = models.IntegerField(default=0)
    responsible = models.CharField(max_length=50,default='')

    def __str__(self):
        return "Evaluation " + self.evaluation_number

class Measurement(models.Model):
    evaluation = models.ForeignKey(Evaluation,on_delete=models.PROTECT)
    value = models.FloatField(default=0)
    def __str__(self):
        return self.value

class Results(models.Model):
    evaluation = models.OneToOneField(Evaluation, on_delete=models.PROTECT)
    cp = models.FloatField(default=0)
    cpk = models.FloatField(default=0)
    average = models.FloatField(default=0)
    min_value = models.FloatField(default=0)
    max_value = models.FloatField(default=0)
    sigma = models.FloatField(default=0)
    amplitude = models.FloatField(default=0)
    result = models.BooleanField(default=False)
    comments = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.result

class EvaluationApproval(models.Model):
    evaluation_result = models.OneToOneField(Results, on_delete=models.PROTECT)
    responsible = models.ForeignKey(EmbracoProfile, on_delete=models.PROTECT)
    approved = models.BooleanField(default=False)
    date = models.DateField(default=0)

    def __str__(self):
        return approved




