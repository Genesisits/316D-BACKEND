from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'  # serialize all fields
from rest_framework import serializers
from .models import ClubOfficers

class ClubOfficersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubOfficers
        fields = '__all__'
from rest_framework import serializers
from .models import ContestRules

class ContestRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestRules
        fields = '__all__'
from rest_framework import serializers
from .models import DistrictCabinet

class DistrictCabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictCabinet
        fields = '__all__'
from rest_framework import serializers
from .models import DistrictLeaders

class DistrictLeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictLeaders
        fields = '__all__'
from rest_framework import serializers
from .models import DistrictOfficers

class DistrictOfficersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictOfficers
        fields = '__all__'
from rest_framework import serializers
from .models import MemberDetails

class MemberDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberDetails
        fields = '__all__'
# serializers.py
from rest_framework import serializers
from .models import MJF

class MJFSerializer(serializers.ModelSerializer):
    class Meta:
        model = MJF
        fields = '__all__'
from rest_framework import serializers
from .models import Signup

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'
# serializers.py
from rest_framework import serializers
from .models import ActivityReport

class ActivityReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityReport
        fields = '__all__'
from rest_framework import serializers
from .models import ContestClaim

class ContestClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestClaim
        fields = '__all__'  # include all fields; or list explicitly if you want
from rest_framework import serializers
from .models import MemberAdditionalDetails

class MemberAdditionalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberAdditionalDetails
        fields = '__all__'
# serializers.py
from rest_framework import serializers
from .models import MemberPhoto

class MemberPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberPhoto
        fields = '__all__'
