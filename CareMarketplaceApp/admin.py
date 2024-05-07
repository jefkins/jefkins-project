from django.contrib import admin
from .models.CareGiverModels import CareGiverBioDataProfile, CareGiverEducationProfile, CareGiverWorkExperienceProfile, CareGiverWorkExperienceTrainingProfile
from .models.CareHomeModels import CareHomeProfile
from .models.CommonModels import MatchingTable
# Register your models here.
admin.site.register(CareGiverBioDataProfile)
admin.site.register(CareGiverEducationProfile)
admin.site.register(CareGiverWorkExperienceProfile)
admin.site.register(CareGiverWorkExperienceTrainingProfile)
admin.site.register(CareHomeProfile)
admin.site.register(MatchingTable)
