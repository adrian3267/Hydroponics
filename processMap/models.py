from django.db import models
from certification.models import RequiredCertificationDocuments,MeasurementSystem


class ProcessStep(models.Model):
    process_map = models.ForeignKey(RequiredCertificationDocuments, on_delete=models.PROTECT)
    step_number = models.IntegerField(default=0)
    step_name = models.CharField(max_length=50,default='Step Name')

    def __str__(self):
        return self.stepNumber + ": " + self.stepName

class ProcessControlParameter(models.Model):
    process_step = models.ForeignKey(ProcessStep, on_delete=models.PROTECT)
    measurement_system = models.ForeignKey(MeasurementSystem, on_delete=models.PROTECT)
    control_parameter = models.CharField(max_length=50,default='Control Parameter')
    tolerance = models.FloatField(default=0)
    control_frequency = models.CharField(max_length=50,default='Monthly')
    sample_size = models.IntegerField(default=1)
    record = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.control_parameter