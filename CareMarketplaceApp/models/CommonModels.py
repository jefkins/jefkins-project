from django.db import models
from django.contrib.auth.models import User


class MatchingTable(models.Model):
    careGiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_giver_matching_tables')
    careHome = models.ForeignKey(User, on_delete=models.CASCADE, related_name='care_home_matching_tables')
    isAccepted = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(auto_now_add=False)
    dateModified = models.DateTimeField(auto_now_add=True)
    modfiedBy = models.CharField(max_length=50, blank=True, null=True, default='Admin')

    def __str__(self):
        return f"{self.careGiver}_{self.careHome}"
    