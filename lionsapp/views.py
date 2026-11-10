from datetime import date, datetime
from decimal import Decimal

from django.db import connection
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from .models import (
    Club,
    ClubOfficers,
    ContestRules,
    DistrictCabinet,
    DistrictLeaders,
    DistrictOfficers,
    MemberDetails,
    MJF,
    Signup,
    ActivityReport,
    ContestClaim,
    MemberAdditionalDetails,
    MemberPhoto,
)

from .serializers import (
    ClubSerializer,
    ClubOfficersSerializer,
    ContestRulesSerializer,
    DistrictCabinetSerializer,
    DistrictLeadersSerializer,
    DistrictOfficersSerializer,
    MemberDetailsSerializer,
    MJFSerializer,
    SignupSerializer,
    ActivityReportSerializer,
    ContestClaimSerializer,
    MemberAdditionalDetailsSerializer,
    MemberPhotoSerializer,
)


# --------------------------------------------------
# RAW SQL SERIALIZER
# --------------------------------------------------

class RawSQLSerializer(serializers.Serializer):

    def to_representation(self, instance):
        result = {}

        for key, value in instance.items():
            if isinstance(value, (date, datetime)):
                value = value.isoformat()
            elif isinstance(value, Decimal):
                value = str(value)

            result[key] = value

        return result


# --------------------------------------------------
# COMMON READ-ONLY SQL VIEWSET
# --------------------------------------------------

class RawSQLReadOnlyViewSet(viewsets.ViewSet):

    table_name = None
    model_class = None

    def list(self, request):

        if not self.table_name:
            return Response(
                {"error": "Database table is not configured"},
                status=500
            )

        # Map SQL Server column names to Django field names.
        # This helps preserve the existing API response structure.
        field_mapping = {}

        if self.model_class:
            for field in self.model_class._meta.concrete_fields:
                column_name = field.column.strip("[]").casefold()
                field_mapping[column_name] = field.attname

        with connection.cursor() as cursor:

            # Table names are fixed in the ViewSet classes below.
            cursor.execute(
                f"SELECT * FROM [dbo].[{self.table_name}]"
            )

            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

        records = []

        for row in rows:
            record = {}

            for column, value in zip(columns, row):
                api_name = field_mapping.get(
                    column.strip("[]").casefold(),
                    column
                )

                record[api_name] = value

            records.append(record)

        serializer = RawSQLSerializer(records, many=True)

        return Response(serializer.data)


# --------------------------------------------------
# CLUB API
# --------------------------------------------------

class ClubViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


# --------------------------------------------------
# CLUB OFFICERS API
# --------------------------------------------------

class ClubOfficersViewSet(RawSQLReadOnlyViewSet):
    table_name = "ClubOfficersLCI"
    model_class = ClubOfficers


# --------------------------------------------------
# CONTEST RULES API
# --------------------------------------------------

class ContestRulesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContestRules.objects.all()
    serializer_class = ContestRulesSerializer


# --------------------------------------------------
# DISTRICT CABINET API
# --------------------------------------------------

class DistrictCabinetViewSet(RawSQLReadOnlyViewSet):
    table_name = "DistrictCabinet"
    model_class = DistrictCabinet


# --------------------------------------------------
# DISTRICT LEADERS API
# --------------------------------------------------

class DistrictLeadersViewSet(RawSQLReadOnlyViewSet):
    table_name = "DistrictLeaders"
    model_class = DistrictLeaders


# --------------------------------------------------
# DISTRICT OFFICERS API
# --------------------------------------------------

class DistrictOfficersViewSet(RawSQLReadOnlyViewSet):
    table_name = "DistrictOfficersLCI"
    model_class = DistrictOfficers


# --------------------------------------------------
# MEMBER DETAILS API
# --------------------------------------------------

class MemberDetailsViewSet(RawSQLReadOnlyViewSet):
    table_name = "MemberDetailsLCI"
    model_class = MemberDetails


# --------------------------------------------------
# MJF API
# --------------------------------------------------

class MJFViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MJF.objects.all()
    serializer_class = MJFSerializer


# --------------------------------------------------
# SIGNUP API
# --------------------------------------------------

class SignupViewSet(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer


# --------------------------------------------------
# ACTIVITY REPORT API
# --------------------------------------------------

class ActivityReportViewSet(RawSQLReadOnlyViewSet):
    table_name = "ClubActivityReport"
    model_class = ActivityReport


# --------------------------------------------------
# CONTEST CLAIM API
# --------------------------------------------------

class ContestClaimViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContestClaim.objects.all()
    serializer_class = ContestClaimSerializer


# --------------------------------------------------
# MEMBER ADDITIONAL DETAILS API
# --------------------------------------------------

class MemberAdditionalDetailsViewSet(RawSQLReadOnlyViewSet):
    table_name = "MemberDetailsActual"
    model_class = MemberAdditionalDetails


# --------------------------------------------------
# MEMBER PHOTO API
# --------------------------------------------------

class MemberPhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MemberPhoto.objects.all()
    serializer_class = MemberPhotoSerializer
