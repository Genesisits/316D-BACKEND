from rest_framework import viewsets
from .models import Club
from .serializers import ClubSerializer

class ClubViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
from rest_framework import viewsets
from .models import ClubOfficers
from .serializers import ClubOfficersSerializer

class ClubOfficersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClubOfficers.objects.all()
    serializer_class = ClubOfficersSerializer
from rest_framework import viewsets
from .models import ContestRules
from .serializers import ContestRulesSerializer

class ContestRulesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing ContestRules.
    ReadOnlyModelViewSet provides `list` and `retrieve` actions.
    """
    queryset = ContestRules.objects.all()
    serializer_class = ContestRulesSerializer
from rest_framework import viewsets
from .models import DistrictCabinet
from .serializers import DistrictCabinetSerializer

class DistrictCabinetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DistrictCabinet.objects.all()
    serializer_class = DistrictCabinetSerializer
from rest_framework import viewsets
from .models import DistrictLeaders
from .serializers import DistrictLeadersSerializer

class DistrictLeadersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DistrictLeaders.objects.all()
    serializer_class = DistrictLeadersSerializer
from rest_framework import viewsets
from .models import DistrictOfficers
from .serializers import DistrictOfficersSerializer

class DistrictOfficersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DistrictOfficers.objects.all()
    serializer_class = DistrictOfficersSerializer
from rest_framework import viewsets
from .models import MemberDetails
from .serializers import MemberDetailsSerializer

class MemberDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MemberDetails.objects.all()
    serializer_class = MemberDetailsSerializer
# views.py
from rest_framework import viewsets
from .models import MJF
from .serializers import MJFSerializer

class MJFViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MJF.objects.all()
    serializer_class = MJFSerializer
from rest_framework import viewsets
from .models import Signup
from .serializers import SignupSerializer

class SignupViewSet(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer
# views.py
from rest_framework import viewsets
from .models import ActivityReport
from .serializers import ActivityReportSerializer

class ActivityReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActivityReport.objects.all()
    serializer_class = ActivityReportSerializer
from rest_framework import viewsets
from .models import ContestClaim
from .serializers import ContestClaimSerializer

class ContestClaimViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing ContestClaim data.
    """
    queryset = ContestClaim.objects.all()
    serializer_class = ContestClaimSerializer
from rest_framework import viewsets
from .models import MemberAdditionalDetails
from .serializers import MemberAdditionalDetailsSerializer

class MemberAdditionalDetailsViewSet(viewsets.ModelViewSet):
    queryset = MemberAdditionalDetails.objects.all()
    serializer_class = MemberAdditionalDetailsSerializer
# views.py
from rest_framework import viewsets
from .models import MemberPhoto
from .serializers import MemberPhotoSerializer

class MemberPhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MemberPhoto.objects.all()
    serializer_class = MemberPhotoSerializer
