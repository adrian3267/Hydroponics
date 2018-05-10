from django.db import models
from certification.models import RequiredCertificationDocuments

class AppendedDocument(models.Model):
    document = models.OneToOneField(RequiredCertificationDocuments, on_delete=models.PROTECT)
    appended_file = models.FileField(upload_to='/static/appended-documents/')

    def __str__(self):
        return self.document