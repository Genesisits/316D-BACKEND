from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'clubs', ClubViewSet, basename='club')
router.register(r'clubofficers', ClubOfficersViewSet, basename='clubofficers')
router.register(r'contestrules', ContestRulesViewSet, basename='contestrules')
router.register(r'districtcabinet', DistrictCabinetViewSet, basename='districtcabinet')
router.register(r'districtleaders', DistrictLeadersViewSet, basename='districtleaders')
router.register(r'districtofficers', DistrictOfficersViewSet, basename='districtofficers')
router.register(r'memberdetails', MemberDetailsViewSet, basename='memberdetails')
router.register(r'mjf', MJFViewSet, basename='mjf')
router.register(r'signup', SignupViewSet, basename='signup')
router.register(r'activityreport', ActivityReportViewSet, basename='activityreport')
router.register(r'contestclaims', ContestClaimViewSet, basename='contestclaim')
router.register(r'memberadditionaldetails', MemberAdditionalDetailsViewSet, basename='memberadditionaldetails')
router.register(r'memberphotos', MemberPhotoViewSet, basename='memberphoto')

urlpatterns = [
    path('', include(router.urls)),
    
]
