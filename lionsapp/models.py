from django.db import models

class Club(models.Model):
    club_id = models.IntegerField(primary_key=True, db_column='club_id')
# assuming this is the PK
    ClubName = models.CharField(max_length=255, blank=True, null=True)
    ClubType = models.CharField(max_length=50, blank=True, null=True)

    
    InauguratedOn = models.DateField(blank=True, null=True)
    CharteredOn = models.DateField(blank=True, null=True)
    SponsoredClub1 = models.CharField(max_length=255, null=True, blank=True)
    SponsoredClub2 = models.CharField(max_length=255, null=True, blank=True)
    ExtensionChairperson1 = models.CharField(max_length=50, blank=True, null=True)
    ExtensionChairperson2 = models.CharField(max_length=50, blank=True, null=True)
    GuidingLion1 = models.CharField(max_length=50, blank=True, null=True)
    GuidingLion2 = models.CharField(max_length=50, blank=True, null=True)
    MeetsOn = models.CharField(max_length=50, blank=True, null=True)
    MeetsAt = models.CharField(max_length=255, blank=True, null=True)
    Status = models.CharField(max_length=255, blank=True, null=True)
    StatusDate = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'ClubDetails'

    def __str__(self):
        return self.club_name or f"Club {self.club_id}"


class ClubOfficers(models.Model):
    OfficialTitle = models.CharField(max_length=255, blank=True, null=True, db_column='Official Title')
    StartDate = models.DateTimeField(blank=True, null=True, db_column='Start Date')
    EndDate = models.CharField(max_length=255, blank=True, null=True, db_column='End Date')

    MemberID = models.CharField(max_length=255, primary_key=True, db_column='Member: Member ID')
    MemberSalutation = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Salutation')
    MemberFirstName = models.CharField(max_length=255, blank=True, null=True, db_column='Member: First Name')
    MemberMiddleName = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Middle Name')
    MemberLastName = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Last Name')
    MemberSuffix = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Suffix')

    MemberPrimaryAddressType = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Primary Address Type')
    MemberMailingAddressLine1 = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Mailing Address Line 1')
    MemberMailingAddressLine2 = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Mailing Address Line 2')
    MemberMailingAddressLine3 = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Mailing Address Line 3')
    MemberMailingCity = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Mailing City')
    MemberMailingStateProvince = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Mailing State/Province')
    MemberMailingZipPostalCode = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Mailing Zip/Postal Code')
    MemberMailingCountry = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Mailing Country')

    MemberPreferredEmail = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Preferred Email')
    MemberPersonalEmail = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Personal Email')
    MemberWorkEmail = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Work Email')
    MemberAlternateEmail = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Alternate Email')

    MemberPreferredPhone = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Preferred Phone')
    MemberMobile = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Mobile')
    MemberHomePhone = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Home Phone')
    MemberWorkPhone = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Work Phone')
    MemberFax = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Fax')

    AccountNameLocal = models.CharField(max_length=255, blank=True, null=True, db_column='Account Name (Local)')
    MemberFirstNameLocal = models.CharField(max_length=255, blank=True, null=True, db_column='Member: First Name (Local)')
    MemberMiddleNameLocal = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Middle Name (Local)')
    MemberLastNameLocal = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Last Name (Local)')
    MemberLocalAddress = models.CharField(max_length=255, blank=True, null=True, db_column='Member: Local Address')

    Type = models.CharField(max_length=255, blank=True, null=True, db_column='Type')
    LionID = models.CharField(max_length=255, blank=True, null=True, db_column='Lion ID')
    ParentRegion = models.CharField(max_length=255, blank=True, null=True, db_column='Parent Region')
    ParentZone = models.CharField(max_length=255, blank=True, null=True, db_column='Parent Zone')

    AccountID = models.CharField(max_length=255, blank=True, null=True, db_column='Account ID')
    ParentId = models.CharField(max_length=255, blank=True, null=True, db_column='Parent Id')
    ParentParentId = models.CharField(max_length=255, blank=True, null=True, db_column='Parent Parent Id')
    ParentDistrictId = models.CharField(max_length=255, blank=True, null=True, db_column='Parent District Id')
    ParentMultipleDistrictId = models.CharField(max_length=255, blank=True, null=True, db_column='Parent Multiple District Id')
    DEPLionsAffiliateId = models.CharField(max_length=255, blank=True, null=True, db_column='DEP-Lions Affiliate Id')
    ParentMultipleDistrict = models.CharField(max_length=255, blank=True, null=True, db_column='Parent Multiple District')
    ParentDistrict = models.CharField(max_length=255, blank=True, null=True, db_column='Parent District')
    AccountName = models.CharField(max_length=255, blank=True, null=True, db_column='Account Name')

    class Meta:
        db_table = 'ClubOfficers'
        managed = False

    def __str__(self):
        return self.OfficialTitle or f'Officer {self.MemberID}'
class ContestRules(models.Model):
    Qno = models.FloatField(primary_key=True)  # Mark Qno as PK if applicable
    Item = models.CharField(max_length=255, null=True, blank=True)
    MaxPoints = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'ContestRules'

    def __str__(self):
        return f"{self.Item} ({self.Qno})"


class DistrictCabinet(models.Model):
    display_order = models.FloatField(null=True, blank=True)
    Position = models.CharField(max_length=255, null=True, blank=True)
    Name = models.CharField(max_length=255, null=True, blank=True)
    member_id = models.FloatField(primary_key=True)  # primary key specified here
    Mobile = models.FloatField(null=True, blank=True)
    Club = models.CharField(max_length=255, null=True, blank=True)
    club_id = models.FloatField(null=True, blank=True)
    LionisticYear = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'DistrictCabinet'

    def __str__(self):
        return self.Name or ''


class DistrictLeaders(models.Model):
    member_id = models.IntegerField(primary_key=True)  # int NOT NULL, primary key
    name = models.CharField(max_length=50, null=True, blank=True)
    mjf = models.CharField(max_length=10, null=True, blank=True)
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    address3 = models.TextField(null=True, blank=True)
    mobile1 = models.CharField(max_length=10, null=True, blank=True)
    mobile2 = models.CharField(max_length=10, null=True, blank=True)
    phone1 = models.CharField(max_length=50, null=True, blank=True)
    phone2 = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    home_club = models.TextField(null=True, blank=True)
    club_id = models.IntegerField(null=True, blank=True)
    present_position = models.CharField(max_length=50, null=True, blank=True)
    other_position = models.CharField(max_length=50, null=True, blank=True)
    past_position = models.CharField(max_length=50, null=True, blank=True)
    spouse_name = models.CharField(max_length=50, null=True, blank=True)
    family_photo_path = models.TextField(null=True, blank=True)
    theme = models.CharField(max_length=50, null=True, blank=True)
    logo_path = models.TextField(null=True, blank=True)
    year_of_dg = models.CharField(max_length=50, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    display_order = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'DistrictLeaders'

    def __str__(self):
        return self.name or ''
class DistrictOfficers(models.Model):
    official_title = models.CharField(max_length=255, null=True, blank=True, db_column='[Official Title]')
    start_date = models.DateTimeField(null=True, blank=True, db_column='[Start Date]')
    end_date = models.CharField(max_length=255, null=True, blank=True, db_column='[End Date]')
    member_id = models.CharField(max_length=255, primary_key=True, db_column='[Member: Member ID]')
    member_salutation = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Salutation]')
    member_first_name = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: First Name]')
    member_middle_name = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Middle Name]')
    member_last_name = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Last Name]')
    member_suffix = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Suffix]')
    member_primary_address_type = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Primary Address Type]')
    member_mailing_address_line_1 = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Mailing Address Line 1]')
    member_mailing_address_line_2 = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Mailing Address Line 2]')
    member_mailing_address_line_3 = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Mailing Address Line 3]')
    member_mailing_city = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Mailing City]')
    member_mailing_state_province = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Mailing State/Province]')
    member_mailing_zip_postal_code = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Mailing Zip/Postal Code]')
    member_mailing_country = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Mailing Country]')
    member_preferred_email = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Preferred Email]')
    member_personal_email = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Personal Email]')
    member_work_email = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Work Email]')
    member_alternate_email = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Alternate Email]')
    member_preferred_phone = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Preferred Phone]')
    member_mobile = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Mobile]')
    member_home_phone = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Home Phone]')
    member_work_phone = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Work Phone]')
    member_fax = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Fax]')
    account_name_local = models.CharField(max_length=255, null=True, blank=True, db_column='[Account Name (Local)]')
    member_first_name_local = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: First Name (Local)]')
    member_middle_name_local = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Middle Name (Local)]')
    member_last_name_local = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Last Name (Local)]')
    member_local_address = models.CharField(max_length=255, null=True, blank=True, db_column='[Member: Local Address]')
    type = models.CharField(max_length=255, null=True, blank=True, db_column='[Type]')
    lion_id = models.CharField(max_length=255, null=True, blank=True, db_column='[Lion ID]')
    parent_region = models.CharField(max_length=255, null=True, blank=True, db_column='[Parent Region]')
    parent_zone = models.CharField(max_length=255, null=True, blank=True, db_column='[Parent Zone]')
    account_id = models.CharField(max_length=255, null=True, blank=True, db_column='[Account ID]')
    parent_id = models.CharField(max_length=255, null=True, blank=True, db_column='[Parent Id]')
    parent_parent_id = models.CharField(max_length=255, null=True, blank=True, db_column='[Parent Parent Id]')
    parent_district_id = models.CharField(max_length=255, null=True, blank=True, db_column='[Parent District Id]')
    parent_multiple_district_id = models.CharField(max_length=255, null=True, blank=True, db_column='[Parent Multiple District Id]')
    dep_lions_affiliate_id = models.CharField(max_length=255, null=True, blank=True, db_column='[DEP-Lions Affiliate Id]')
    parent_multiple_district = models.CharField(max_length=255, null=True, blank=True, db_column='[Parent Multiple District]')
    parent_district = models.CharField(max_length=255, null=True, blank=True, db_column='[Parent District]')
    account_name = models.CharField(max_length=255, null=True, blank=True, db_column='[Account Name]')

    class Meta:
        db_table = 'DistrictOfficers'
        managed = False


class MemberDetails(models.Model):
    lion_id = models.CharField(max_length=255, null=True, blank=True, db_column='Lion ID')
    type = models.CharField(max_length=255, null=True, blank=True, db_column='Type')
    parent_region = models.CharField(max_length=255, null=True, blank=True, db_column='Parent Region')
    parent_zone = models.CharField(max_length=255, null=True, blank=True, db_column='Parent Zone')
    membership_full_type = models.CharField(max_length=255, null=True, blank=True, db_column='Membership Full Type')
    membership_type = models.CharField(max_length=255, null=True, blank=True, db_column='Membership Type')
    membership_category = models.CharField(max_length=255, null=True, blank=True, db_column='Membership Category')
    program = models.CharField(max_length=255, null=True, blank=True, db_column='Program')
    
    contact_member_id = models.CharField(db_column='Contact: Member ID', max_length=255, primary_key=True)
    contact_salutation = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Salutation')
    contact_first_name = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: First Name')
    contact_middle_name = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Middle Name')
    contact_last_name = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Last Name')
    contact_suffix = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Suffix')
    contact_nickname = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Nickname')
    
    contact_mailing_address_line_1 = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Mailing Address Line 1')
    contact_mailing_address_line_2 = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Mailing Address Line 2')
    contact_mailing_address_line_3 = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Mailing Address Line 3')
    contact_mailing_city = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Mailing City')
    contact_mailing_state_province = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Mailing State/Province')
    contact_mailing_zip_postal_code = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Mailing Zip/Postal Code')
    contact_mailing_country = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Mailing Country')
    
    account_name_local = models.CharField(max_length=255, null=True, blank=True, db_column='Account Name (Local)')
    contact_first_name_local = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: First Name (Local)')
    contact_middle_name_local = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Middle Name (Local)')
    contact_last_name_local = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Last Name (Local)')
    contact_local_address = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Local Address')
    
    contact_preferred_email = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Preferred Email')
    contact_personal_email = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Personal Email')
    contact_work_email = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Work Email')
    contact_alternate_email = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Alternate Email')
    
    contact_preferred_phone = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Preferred Phone')
    contact_mobile = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Mobile')
    contact_home_phone = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Home Phone')
    contact_other_phone = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Other Phone')
    contact_fax = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Fax')
    
    contact_spouse_name = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Spouse Name')
    contact_spouse_status = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Spouse Status')
    contact_birthdate = models.DateTimeField(null=True, blank=True, db_column='Contact: Birthdate')
    contact_gender = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Gender')
    contact_occupation = models.CharField(max_length=255, null=True, blank=True, db_column='Contact: Occupation')
    
    lion_join_date = models.DateTimeField(null=True, blank=True, db_column='Lion Join Date')
    membership_sponsor_name = models.CharField(max_length=255, null=True, blank=True, db_column='Membership Sponsor Name')
    club_branch = models.CharField(max_length=255, null=True, blank=True, db_column='Club Branch')
    parent_multiple_district = models.CharField(max_length=255, null=True, blank=True, db_column='Parent Multiple District')
    parent_district = models.CharField(max_length=255, null=True, blank=True, db_column='Parent District')
    account_name = models.CharField(max_length=255, null=True, blank=True, db_column='Account Name')

    class Meta:
        db_table = 'MemberDetails'
        managed = False  # Set to False if this table is already managed outside Django


class MJF(models.Model):
    display_order = models.IntegerField(blank=True, null=True)
    member_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    club = models.CharField(max_length=255, blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    DOMJF = models.CharField(max_length=50, blank=True, null=True)
    PMJF = models.CharField(max_length=50, blank=True, null=True)
    DOPMJF = models.CharField(max_length=50, blank=True, null=True)
    demised = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'MJF'

    def __str__(self):
        return self.name or f"Member {self.member_id}"


class Signup(models.Model):
    member_id = models.IntegerField(primary_key=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    account_status = models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'signup'  # explicitly map to your 'signup' table

    def __str__(self):
        return f"{self.member_id} - {self.mobile}"


class ActivityReport(models.Model):
    activity_number = models.IntegerField(primary_key=True)
    club_id = models.IntegerField(blank=True, null=True)
    reported_by = models.IntegerField(blank=True, null=True)
    activity_name = models.CharField(max_length=100, blank=True, null=True)
    activity_date = models.DateField(blank=True, null=True)
    activity_type = models.CharField(max_length=50, blank=True, null=True)
    signature_activity = models.BooleanField(blank=True, null=True)
    funded_lcif = models.BooleanField(blank=True, null=True)
    cause = models.CharField(max_length=50, blank=True, null=True)
    project_type = models.CharField(max_length=100, blank=True, null=True)
    people_served = models.IntegerField(blank=True, null=True)
    total_volunteers = models.IntegerField(blank=True, null=True)
    total_volunteer_hours = models.IntegerField(blank=True, null=True)
    additional_metrics = models.BooleanField(blank=True, null=True)
    funds_donated = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    funds_raised = models.IntegerField(blank=True, null=True)
    trees_planted = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    featured_photo = models.TextField(blank=True, null=True)
    addlphoto1 = models.TextField(blank=True, null=True)
    addlphoto2 = models.TextField(blank=True, null=True)
    addlphoto3 = models.TextField(blank=True, null=True)
    addlphoto4 = models.TextField(blank=True, null=True)
    addlphoto5 = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'ActivityReport'

    def __str__(self):
        return f"{self.activity_name} ({self.activity_number})"


class ContestClaim(models.Model):
    club_id = models.IntegerField(primary_key=True)
    reported_by = models.IntegerField(null=True, blank=True)
    MonthYear = models.CharField(max_length=50)
    FinalSubmission = models.CharField(max_length=50, null=True, blank=True)
    SubmissionDate = models.DateTimeField(null=True, blank=True)

    c1 = models.IntegerField(null=True, blank=True)
    r1 = models.CharField(max_length=50, null=True, blank=True)
    c2 = models.IntegerField(null=True, blank=True)
    r2 = models.CharField(max_length=50, null=True, blank=True)
    c3 = models.IntegerField(null=True, blank=True)
    r3 = models.CharField(max_length=50, null=True, blank=True)
    c4 = models.IntegerField(null=True, blank=True)
    r4 = models.CharField(max_length=50, null=True, blank=True)
    c5 = models.IntegerField(null=True, blank=True)
    r5 = models.CharField(max_length=50, null=True, blank=True)
    c6 = models.IntegerField(null=True, blank=True)
    r6 = models.CharField(max_length=50, null=True, blank=True)
    c7 = models.IntegerField(null=True, blank=True)
    r7 = models.CharField(max_length=50, null=True, blank=True)
    c8 = models.IntegerField(null=True, blank=True)
    r8 = models.CharField(max_length=50, null=True, blank=True)
    c9 = models.IntegerField(null=True, blank=True)
    r9 = models.CharField(max_length=50, null=True, blank=True)
    c10 = models.IntegerField(null=True, blank=True)
    r10 = models.CharField(max_length=50, null=True, blank=True)
    c11 = models.IntegerField(null=True, blank=True)
    r11 = models.CharField(max_length=50, null=True, blank=True)
    c12 = models.IntegerField(null=True, blank=True)
    r12 = models.CharField(max_length=50, null=True, blank=True)
    c13 = models.IntegerField(null=True, blank=True)
    r13 = models.CharField(max_length=50, null=True, blank=True)
    c14 = models.IntegerField(null=True, blank=True)
    r14 = models.CharField(max_length=50, null=True, blank=True)
    c15 = models.IntegerField(null=True, blank=True)
    r15 = models.CharField(max_length=50, null=True, blank=True)
    c16 = models.IntegerField(null=True, blank=True)
    r16 = models.CharField(max_length=50, null=True, blank=True)
    c17 = models.IntegerField(null=True, blank=True)
    r17 = models.CharField(max_length=50, null=True, blank=True)
    c18 = models.IntegerField(null=True, blank=True)
    r18 = models.CharField(max_length=50, null=True, blank=True)
    c19 = models.IntegerField(null=True, blank=True)
    r19 = models.CharField(max_length=50, null=True, blank=True)
    c20 = models.IntegerField(null=True, blank=True)
    r20 = models.CharField(max_length=50, null=True, blank=True)
    c21 = models.IntegerField(null=True, blank=True)
    r21 = models.CharField(max_length=50, null=True, blank=True)
    c22 = models.IntegerField(null=True, blank=True)
    r22 = models.CharField(max_length=50, null=True, blank=True)
    c23 = models.IntegerField(null=True, blank=True)
    r23 = models.CharField(max_length=50, null=True, blank=True)
    c24 = models.IntegerField(null=True, blank=True)
    r24 = models.CharField(max_length=50, null=True, blank=True)
    c25 = models.IntegerField(null=True, blank=True)
    r25 = models.CharField(max_length=50, null=True, blank=True)
    c26 = models.IntegerField(null=True, blank=True)
    r26 = models.CharField(max_length=50, null=True, blank=True)
    c27 = models.IntegerField(null=True, blank=True)
    r27 = models.CharField(max_length=50, null=True, blank=True)
    c28 = models.IntegerField(null=True, blank=True)
    r28 = models.CharField(max_length=50, null=True, blank=True)
    c29 = models.IntegerField(null=True, blank=True)
    r29 = models.CharField(max_length=50, null=True, blank=True)
    c30 = models.IntegerField(null=True, blank=True)
    r30 = models.CharField(max_length=50, null=True, blank=True)
    c31 = models.IntegerField(null=True, blank=True)
    r31 = models.CharField(max_length=50, null=True, blank=True)
    c32 = models.IntegerField(null=True, blank=True)
    r32 = models.CharField(max_length=50, null=True, blank=True)
    c33 = models.IntegerField(null=True, blank=True)
    r33 = models.CharField(max_length=50, null=True, blank=True)
    c34 = models.IntegerField(null=True, blank=True)
    r34 = models.CharField(max_length=50, null=True, blank=True)
    c35 = models.IntegerField(null=True, blank=True)
    r35 = models.CharField(max_length=50, null=True, blank=True)
    c36 = models.IntegerField(null=True, blank=True)
    r36 = models.CharField(max_length=50, null=True, blank=True)
    c37 = models.IntegerField(null=True, blank=True)
    r37 = models.CharField(max_length=50, null=True, blank=True)
    c38 = models.IntegerField(null=True, blank=True)
    r38 = models.CharField(max_length=50, null=True, blank=True)
    c39 = models.IntegerField(null=True, blank=True)
    r39 = models.CharField(max_length=50, null=True, blank=True)
    c40 = models.IntegerField(null=True, blank=True)
    r40 = models.CharField(max_length=50, null=True, blank=True)
    c41 = models.IntegerField(null=True, blank=True)
    r41 = models.CharField(max_length=50, null=True, blank=True)
    c42 = models.IntegerField(null=True, blank=True)
    r42 = models.CharField(max_length=50, null=True, blank=True)
    c43 = models.IntegerField(null=True, blank=True)
    r43 = models.CharField(max_length=50, null=True, blank=True)
    c44 = models.IntegerField(null=True, blank=True)
    r44 = models.CharField(max_length=50, null=True, blank=True)
    c45 = models.IntegerField(null=True, blank=True)
    r45 = models.CharField(max_length=50, null=True, blank=True)
    c46 = models.IntegerField(null=True, blank=True)
    r46 = models.CharField(max_length=50, null=True, blank=True)
    c47 = models.IntegerField(null=True, blank=True)
    r47 = models.CharField(max_length=50, null=True, blank=True)
    c48 = models.IntegerField(null=True, blank=True)
    r48 = models.CharField(max_length=50, null=True, blank=True)
    c49 = models.IntegerField(null=True, blank=True)
    r49 = models.CharField(max_length=50, null=True, blank=True)
    c50 = models.IntegerField(null=True, blank=True)
    r50 = models.CharField(max_length=50, null=True, blank=True)
    c51 = models.IntegerField(null=True, blank=True)
    r51 = models.CharField(max_length=50, null=True, blank=True)
    c52 = models.IntegerField(null=True, blank=True)
    r52 = models.CharField(max_length=50, null=True, blank=True)
    c53 = models.IntegerField(null=True, blank=True)
    r53 = models.CharField(max_length=50, null=True, blank=True)
    c54 = models.IntegerField(null=True, blank=True)
    r54 = models.CharField(max_length=50, null=True, blank=True)
    c55 = models.IntegerField(null=True, blank=True)
    r55 = models.CharField(max_length=50, null=True, blank=True)
    c56 = models.IntegerField(null=True, blank=True)
    r56 = models.CharField(max_length=50, null=True, blank=True)
    c57 = models.IntegerField(null=True, blank=True)
    r57 = models.CharField(max_length=50, null=True, blank=True)
    c58 = models.IntegerField(null=True, blank=True)
    r58 = models.CharField(max_length=50, null=True, blank=True)
    c59 = models.IntegerField(null=True, blank=True)
    r59 = models.CharField(max_length=50, null=True, blank=True)
    c60 = models.IntegerField(null=True, blank=True)
    r60 = models.CharField(max_length=50, null=True, blank=True)
    c61 = models.IntegerField(null=True, blank=True)
    r61 = models.CharField(max_length=50, null=True, blank=True)
    c62 = models.IntegerField(null=True, blank=True)
    r62 = models.CharField(max_length=50, null=True, blank=True)
    c63 = models.IntegerField(null=True, blank=True)
    r63 = models.CharField(max_length=50, null=True, blank=True)
    c64 = models.IntegerField(null=True, blank=True)
    r64 = models.CharField(max_length=50, null=True, blank=True)
    c65 = models.IntegerField(null=True, blank=True)
    r65 = models.CharField(max_length=50, null=True, blank=True)
    c66 = models.IntegerField(null=True, blank=True)
    r66 = models.CharField(max_length=50, null=True, blank=True)
    c67 = models.IntegerField(null=True, blank=True)
    r67 = models.CharField(max_length=50, null=True, blank=True)
    c68 = models.IntegerField(null=True, blank=True)
    r68 = models.CharField(max_length=50, null=True, blank=True)
    c69 = models.IntegerField(null=True, blank=True)
    r69 = models.CharField(max_length=50, null=True, blank=True)
    c70 = models.IntegerField(null=True, blank=True)
    r70 = models.CharField(max_length=50, null=True, blank=True)
    c71 = models.IntegerField(null=True, blank=True)
    r71 = models.CharField(max_length=50, null=True, blank=True)
    c72 = models.IntegerField(null=True, blank=True)
    r72 = models.CharField(max_length=50, null=True, blank=True)
    c73 = models.IntegerField(null=True, blank=True)
    r73 = models.CharField(max_length=50, null=True, blank=True)
    c74 = models.IntegerField(null=True, blank=True)
    r74 = models.CharField(max_length=50, null=True, blank=True)
    c75 = models.IntegerField(null=True, blank=True)
    r75 = models.CharField(max_length=50, null=True, blank=True)
    c76 = models.IntegerField(null=True, blank=True)
    r76 = models.CharField(max_length=50, null=True, blank=True)
    c77 = models.IntegerField(null=True, blank=True)
    r77 = models.CharField(max_length=50, null=True, blank=True)
    c78 = models.IntegerField(null=True, blank=True)
    r78 = models.CharField(max_length=50, null=True, blank=True)
    c79 = models.IntegerField(null=True, blank=True)
    r79 = models.CharField(max_length=50, null=True, blank=True)
    c80 = models.IntegerField(null=True, blank=True)
    r80 = models.CharField(max_length=50, null=True, blank=True)
    c81 = models.IntegerField(null=True, blank=True)
    r81 = models.CharField(max_length=50, null=True, blank=True)
    c82 = models.IntegerField(null=True, blank=True)
    r82 = models.CharField(max_length=50, null=True, blank=True)
    c83 = models.IntegerField(null=True, blank=True)
    r83 = models.CharField(max_length=50, null=True, blank=True)
    c84 = models.IntegerField(null=True, blank=True)
    r84 = models.CharField(max_length=50, null=True, blank=True)
    c85 = models.IntegerField(null=True, blank=True)
    r85 = models.CharField(max_length=50, null=True, blank=True)
    c86 = models.IntegerField(null=True, blank=True)
    r86 = models.CharField(max_length=50, null=True, blank=True)
    c87 = models.IntegerField(null=True, blank=True)
    r87 = models.CharField(max_length=50, null=True, blank=True)
    c88 = models.IntegerField(null=True, blank=True)
    r88 = models.CharField(max_length=50, null=True, blank=True)
    c89 = models.IntegerField(null=True, blank=True)
    r89 = models.CharField(max_length=50, null=True, blank=True)
    c90 = models.IntegerField(null=True, blank=True)
    r90 = models.CharField(max_length=50, null=True, blank=True)
    c91 = models.IntegerField(null=True, blank=True)
    r91 = models.CharField(max_length=50, null=True, blank=True)
    c92 = models.IntegerField(null=True, blank=True)
    r92 = models.CharField(max_length=50, null=True, blank=True)
    c93 = models.IntegerField(null=True, blank=True)
    r93 = models.CharField(max_length=50, null=True, blank=True)
    c94 = models.IntegerField(null=True, blank=True)
    r94 = models.CharField(max_length=50, null=True, blank=True)
    c95 = models.IntegerField(null=True, blank=True)
    r95 = models.CharField(max_length=50, null=True, blank=True)
    c96 = models.IntegerField(null=True, blank=True)
    r96 = models.CharField(max_length=50, null=True, blank=True)
    c97 = models.IntegerField(null=True, blank=True)
    r97 = models.CharField(max_length=50, null=True, blank=True)
    c98 = models.IntegerField(null=True, blank=True)
    r98 = models.CharField(max_length=50, null=True, blank=True)
    c99 = models.IntegerField(null=True, blank=True)
    r99 = models.CharField(max_length=50, null=True, blank=True)
    c100 = models.IntegerField(null=True, blank=True)
    r100 = models.CharField(max_length=50, null=True, blank=True)
    c101 = models.IntegerField(null=True, blank=True)
    r101 = models.CharField(max_length=50, null=True, blank=True)
    c102 = models.IntegerField(null=True, blank=True)
    r102 = models.CharField(max_length=50, null=True, blank=True)
    c103 = models.IntegerField(null=True, blank=True)
    r103 = models.CharField(max_length=50, null=True, blank=True)
    c104 = models.IntegerField(null=True, blank=True)
    r104 = models.CharField(max_length=50, null=True, blank=True)
    c105 = models.IntegerField(null=True, blank=True)
    r105 = models.CharField(max_length=50, null=True, blank=True)
    c106 = models.IntegerField(null=True, blank=True)
    r106 = models.CharField(max_length=50, null=True, blank=True)
    c107 = models.IntegerField(null=True, blank=True)
    r107 = models.CharField(max_length=50, null=True, blank=True)
    c108 = models.IntegerField(null=True, blank=True)
    r108 = models.CharField(max_length=50, null=True, blank=True)
    c109 = models.IntegerField(null=True, blank=True)
    r109 = models.CharField(max_length=50, null=True, blank=True)
    c110 = models.IntegerField(null=True, blank=True)
    r110 = models.CharField(max_length=50, null=True, blank=True)
    c111 = models.IntegerField(null=True, blank=True)
    r111 = models.CharField(max_length=50, null=True, blank=True)
    c112 = models.IntegerField(null=True, blank=True)
    r112 = models.CharField(max_length=50, null=True, blank=True)
    c113 = models.IntegerField(null=True, blank=True)
    r113 = models.CharField(max_length=50, null=True, blank=True)
    c114 = models.IntegerField(null=True, blank=True)
    r114 = models.CharField(max_length=50, null=True, blank=True)
    c115 = models.IntegerField(null=True, blank=True)
    r115 = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'ContestClaim'

    def __str__(self):
        return f'ContestClaim - Club ID: {self.club_id} MonthYear: {self.MonthYear}'


class MemberAdditionalDetails(models.Model):
    member_id = models.IntegerField(primary_key=True)
    member_name = models.CharField(max_length=50, null=True, blank=True)
    club_id = models.IntegerField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Spouse = models.CharField(max_length=50, null=True, blank=True)
    DOM = models.DateField(null=True, blank=True)
    Children = models.IntegerField(null=True, blank=True)
    BloodGroup = models.CharField(max_length=10, null=True, blank=True)
    MobileNumber1 = models.CharField(max_length=50, null=True, blank=True)
    MobileNumber2 = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Address1 = models.CharField(max_length=50, null=True, blank=True)
    Address2 = models.CharField(max_length=50, null=True, blank=True)
    Address3 = models.CharField(max_length=50, null=True, blank=True)
    AddressCity = models.CharField(max_length=50, null=True, blank=True)
    PIN = models.IntegerField(null=True, blank=True)
    PostsHeld = models.TextField(null=True, blank=True)
    LionisticAwards = models.TextField(null=True, blank=True)
    reported_by = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'MemberAdditionalDetails'
        managed = False  # if the table already exists in your database


class MemberPhoto(models.Model):
    member_id = models.IntegerField(primary_key=True)
    single_photo = models.TextField(null=True, blank=True)  # nvarchar with -1 length means TEXT
    family_photo = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'MemberPhoto'

    def __str__(self):
        return f"MemberPhoto {self.member_id}"
