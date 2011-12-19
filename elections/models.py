from django.db import models

from .settings import TEST_DATA_ONLY
from .fields import TestFlagField

class TestDataManager(models.Manager):
    """
    Redefines get_query_set() to use test data based on settings switch.
    Provides "live" and "test" to specifically get those records.
    """
    
    def get_query_set(self):
        """
        if TEST_DATA_ONLY, only provide test data
        """
        qset = super(TestDataManager, self).get_query_set()
        if TEST_DATA_ONLY:
            return qset.filter(test_flag='t')
        else:
            return qset
    
    def test(self):
        """
        Return only test data
        """
        return super(TestDataManager, self).get_query_set().filter(test_flag='t')
    
    def live(self):
        """
        Return only live data
        """
        return super(TestDataManager, self).get_query_set().filter(test_flag='l')

class Candidate(models.Model):
    """
    An election candidate
    """
    test_flag = TestFlagField()
    politician_id = models.IntegerField(primary_key=True)
    ap_candidate_id = models.IntegerField(unique=True)
    candidate_number = models.IntegerField()
    first_name = models.CharField(blank=True, null=True, max_length=64)
    middle_name = models.CharField(blank=True, null=True, max_length=64)
    last_name = models.CharField(blank=True, null=True, max_length=64)
    junior = models.CharField(blank=True, null=True, max_length=16)
    use_junior = models.BooleanField(default=False)
    year_first_elected = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(blank=True, null=True, max_length=100)
    birth_state = models.CharField(blank=True, null=True, max_length=2)
    birth_province = models.CharField(blank=True, null=True, max_length=100)
    birth_country = models.CharField(blank=True, null=True, max_length=100)
    residence_place = models.CharField(blank=True, null=True, max_length=100)
    residence_state = models.CharField(blank=True, null=True, max_length=2)
    gender = models.CharField(
        blank=True, null=True, 
        max_length=1, 
        choices=(('M', 'Male'), ('F', 'Female')))
    ethnicity = models.CharField(blank=True, null=True, max_length=100)
    hispanic = models.CharField(blank=True, null=True, max_length=100)
    religion = models.CharField(blank=True, null=True, max_length=100)
    biography = models.TextField(blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    campaigns = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    @property
    def full_name(self):
        names =[]
        if self.first_name:
            names.append(self.first_name)
        if self.middle_name:
            names.append(self.middle_name)
        if self.last_name:
            names.append(self.last_name)
        name = u" ".join(names)
        if self.junior:
            name = u"%s, %s" % (name, self.junior)
        return name
    
    @models.permalink
    def get_absolute_url(self):
        """
        Get the absolute url for the candidate
        """
        return ('candidate_detail', (), {'pk': self.politician_id })
    
    objects = TestDataManager()
    
    class Meta:
        ordering = ('last_name', 'first_name')
    
    def __unicode__(self):
        return self.full_name


class RaceCounty(models.Model):
    """
    Description of an election race by county
    """
    test_flag = TestFlagField()
    race_county_id = models.BigIntegerField(primary_key=True)
    race_number = models.IntegerField()
    election_date = models.DateField()
    state_postal = models.CharField(max_length=2)
    county_number = models.IntegerField(blank=True, null=True)
    fips_code = models.IntegerField(blank=True, null=True)
    county_name = models.CharField(max_length=64)
    office_id = models.CharField(max_length=1)
    race_type_id = models.CharField(max_length=1)
    seat_number = models.IntegerField()
    office_name = models.CharField(blank=True, null=True, max_length=64)
    seat_name = models.CharField(blank=True, null=True, max_length=64)
    race_type_party = models.CharField(blank=True, null=True, max_length=16)
    race_type = models.CharField(blank=True, null=True, max_length=32)
    office_description = models.CharField(blank=True, null=True, max_length=64)
    number_of_winners = models.IntegerField()
    number_in_runoff = models.IntegerField(blank=True, null=True)
    precincts_reporting = models.IntegerField()
    total_precincts = models.IntegerField()

    objects = TestDataManager()
    
    class Meta:
        verbose_name_plural = "Race counties"

    def __unicode__(self):
        return u"RaceCounty"


class RaceDistrict(models.Model):
    """
    Description of an election race by district
    """
    test_flag = TestFlagField()
    race_district_id = models.BigIntegerField(primary_key=True)
    race_number = models.IntegerField()
    election_date = models.DateField()
    state_postal = models.CharField(max_length=2)
    district_type = models.CharField(blank=True, null=True, max_length=16)
    cd_number = models.IntegerField(blank=True, null=True)
    district_name = models.CharField(blank=True, null=True, max_length=64)
    office_id = models.CharField(max_length=1)
    race_type_id = models.CharField(max_length=1)
    seat_number = models.IntegerField()
    office_name = models.CharField(blank=True, null=True, max_length=64)
    seat_name = models.CharField(blank=True, null=True, max_length=64)
    race_type_party = models.CharField(blank=True, null=True, max_length=16)
    race_type = models.CharField(blank=True, null=True, max_length=32)
    office_description = models.CharField(blank=True, null=True, max_length=64)
    number_of_winners = models.IntegerField()
    number_in_runoff = models.IntegerField(blank=True, null=True)
    precincts_reporting = models.IntegerField()
    total_precincts = models.IntegerField()

    objects = TestDataManager()
    

    class Meta:
        pass

    def __unicode__(self):
        return u"RaceDistrict"


class CountyResult(models.Model):
    """
    Results of a county election
    """
    test_flag = TestFlagField()
    race_county = models.ForeignKey(RaceCounty)
    ap_candidate = models.ForeignKey(
        Candidate, 
        to_field='ap_candidate_id',
        related_name="county_results")
    party = models.CharField(blank=True, null=True, max_length=16)
    incumbent = models.BooleanField(default=False)
    vote_count = models.IntegerField(default=0)
    winner = models.CharField(blank=True, null=True, max_length=1)
    natl_order = models.IntegerField(blank=True, null=True)
    
    objects = TestDataManager()
    
    class Meta:
        pass
    
    def __unicode__(self):
        return u"CountyResult"

class DistrictResult(models.Model):
    """
    Results of a district election
    """
    test_flag = TestFlagField()
    race_district = models.ForeignKey(RaceDistrict)
    ap_candidate = models.ForeignKey(
        Candidate, 
        to_field='ap_candidate_id',
        related_name="district_results")
    party = models.CharField(blank=True, null=True, max_length=16)
    incumbent = models.BooleanField(default=False)
    vote_count = models.IntegerField(default=0)
    delegate_count = models.IntegerField(default=0)
    winner = models.CharField(blank=True, null=True, max_length=1)
    natl_order = models.IntegerField(blank=True, null=True)
    
    objects = TestDataManager()
    
    class Meta:
        pass

    def __unicode__(self):
        return u"DistrictResult"


class CandidateOffice(models.Model):
    """
    Record for each office and politician holding or seeking that office.
    """
    candidate = models.ForeignKey(Candidate, related_name="offices")
    office_id = models.CharField(blank=True, null=True, max_length=1)
    state = models.CharField(blank=True, null=True, max_length=2)
    district_number = models.CharField(blank=True, null=True, max_length=4)
    party_id = models.CharField(blank=True, null=True, max_length=16)
    status_id = models.CharField(blank=True, null=True, max_length=1)
    office = models.CharField(blank=True, null=True, max_length=64)
    state_name = models.CharField(blank=True, null=True, max_length=100)
    district_name = models.CharField(blank=True, null=True, max_length=32)
    party_name = models.CharField(blank=True, null=True, max_length=32)
    office_description = models.CharField(blank=True, null=True, max_length=64)
    status_description = models.CharField(blank=True, null=True, max_length=64)
    next_election = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32)
    
    def calculate_checksum(self):
        """
        Calculate the MD5 checksum for the record
        """
        import hashlib
        checksum = hashlib.md5()
        checksum.update(str(self.candidate.pk))
        checksum.update(self.office_id or '')
        checksum.update(self.state or '')
        checksum.update(self.district_number or '')
        checksum.update(self.party_id or '')
        checksum.update(self.status_id or '')
        checksum.update(self.office or '')
        checksum.update(self.state_name or '')
        checksum.update(self.district_name or '')
        checksum.update(self.party_name or '')
        checksum.update(self.office_description or '')
        checksum.update(self.status_description or '')
        checksum.update(str(self.next_election) or '')
        return checksum.hexdigest()
    
    def save(self, *args, **kwargs):
        """
        Add the checksum
        """
        self.checksum = self.calculate_checksum()
        super(CandidateOffice, self).save(*args, **kwargs)

    class Meta:
        pass

    def __unicode__(self):
        name = [
            self.party_id or '', 
            self.state or '', 
            self.office or '', 
            self.district_name or '',]
        return u" ".join(name)

class CandidateEducation(models.Model):
    """
    Record for each post-high-school educational institution attended 
    by each politician.
    """
    candidate = models.ForeignKey(Candidate, related_name="education")
    school_name = models.CharField(blank=True, null=True, max_length=64)
    school_type = models.CharField(blank=True, null=True, max_length=64)
    major = models.CharField(blank=True, null=True, max_length=64)
    degree = models.CharField(blank=True, null=True, max_length=64)
    school_city = models.CharField(blank=True, null=True, max_length=100)
    school_state = models.CharField(blank=True, null=True, max_length=2)
    school_province = models.CharField(blank=True, null=True, max_length=100)
    school_country = models.CharField(blank=True, null=True, max_length=64)
    checksum = models.CharField(max_length=32)
    
    def calculate_checksum(self):
        """
        Calculate the MD5 checksum for the record
        """
        import hashlib
        checksum = hashlib.md5()
        checksum.update(str(self.candidate.pk))
        checksum.update(self.school_name or '')
        checksum.update(self.school_type or '')
        checksum.update(self.major or '')
        checksum.update(self.degree or '')
        checksum.update(self.school_city or '')
        checksum.update(self.school_state or '')
        checksum.update(self.school_province or '')
        checksum.update(self.school_country or '')
        return checksum.hexdigest()
        
        
    class Meta:
        verbose_name_plural = 'education'
    
    def save(self, *args, **kwargs):
        """
        Add the checksum
        """
        self.checksum = self.calculate_checksum()
        super(CandidateEducation, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return u"%s's %s in %s from %s" % (self.candidate, self.degree, 
            self.major, self.school_name)


class CandidatePhone(models.Model):
    """
    Record for each voice telephone number available for each politician.
    """
    candidate = models.ForeignKey(Candidate, related_name="phones")
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    extension = models.CharField(blank=True, null=True, max_length=10)
    location = models.CharField(blank=True, null=True, max_length=64)
    detail = models.CharField(blank=True, null=True, max_length=64)
    checksum = models.CharField(max_length=32)
    
    def calculate_checksum(self):
        """
        Calculate the MD5 checksum for the record
        """
        import hashlib
        checksum = hashlib.md5()
        checksum.update(str(self.candidate.pk))
        checksum.update(self.phone_number or '')
        checksum.update(self.extension or '')
        checksum.update(self.location or '')
        checksum.update(self.detail or '')
        return checksum.hexdigest()
    
    def save(self, *args, **kwargs):
        """
        Add the checksum
        """
        self.checksum = self.calculate_checksum()
        super(CandidatePhone, self).save(*args, **kwargs)

    class Meta:
        pass

    def __unicode__(self):
        return u"%s %s: %s" % (self.candidate, self.detail, self.phone_number)

class CandidateURL(models.Model):
    """
    Record for each voice telephone number available for each politician.
    """
    candidate = models.ForeignKey(Candidate, related_name="urls")
    url = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)
    checksum = models.CharField(max_length=32)
    
    def calculate_checksum(self):
        """
        Calculate the MD5 checksum for the record
        """
        import hashlib
        checksum = hashlib.md5()
        checksum.update(str(self.candidate.pk))
        checksum.update(self.url or '')
        checksum.update(self.description or '')
        return checksum.hexdigest()
    
    def save(self, *args, **kwargs):
        """
        Add the checksum
        """
        self.checksum = self.calculate_checksum()
        super(CandidateURL, self).save(*args, **kwargs)

    class Meta:
        pass

    def __unicode__(self):
        return u"%s %s %s" % (self.candidate, self.description, self.url)

class CandidateMedia(models.Model):
    """
    Record for each voice telephone number available for each politician.
    """
    candidate = models.ForeignKey(Candidate)
    medium_type = models.CharField(blank=True, null=True, max_length=64)
    file_name = models.CharField(blank=True, null=True, max_length=255)
    file_extension = models.CharField(blank=True, null=True, max_length=10)
    checksum = models.CharField(max_length=32)
    
    def calculate_checksum(self):
        """
        Calculate the MD5 checksum for the record
        """
        import hashlib
        checksum = hashlib.md5()
        checksum.update(str(self.candidate.pk))
        checksum.update(self.medium_type or '')
        checksum.update(self.file_name or '')
        checksum.update(self.file_extension or '')
        return checksum.hexdigest()
    
    def save(self, *args, **kwargs):
        """
        Add the checksum
        """
        self.checksum = self.calculate_checksum()
        super(CandidateMedia, self).save(*args, **kwargs)

    class Meta:
        pass

    def __unicode__(self):
        return u"%s %s" % (self.candidate, self.file_name)


class CandidateMoney(models.Model):
    """
    Record for each office and politician holding or seeking that office.
    """
    candidate = models.ForeignKey(Candidate)
    fec_candidate_id = models.CharField(blank=True, null=True, max_length=64)
    fec_office_id = models.CharField(blank=True, null=True, max_length=64)
    fec_postal_id = models.CharField(blank=True, null=True, max_length=64)
    fec_district_id = models.CharField(blank=True, null=True, max_length=64)
    total_receipts = models.CharField(blank=True, null=True, max_length=100)
    candidate_loans = models.CharField(blank=True, null=True, max_length=100)
    other_loans = models.CharField(blank=True, null=True, max_length=100)
    candidate_loan_repayments = models.CharField(blank=True, null=True, max_length=64)
    other_loan_repayments = models.CharField(blank=True, null=True, max_length=100)
    individual_contributions = models.CharField(blank=True, null=True, max_length=100)
    pac_contributions = models.CharField(blank=True, null=True, max_length=100)
    ending_cash = models.CharField(blank=True, null=True, max_length=100)
    date_of_last_report = models.CharField(blank=True, null=True, max_length=100)
    total_disbursements = models.CharField(blank=True, null=True, max_length=100)
    checksum = models.CharField(max_length=32)
    
    def calculate_checksum(self):
        """
        Calculate the MD5 checksum for the record
        """
        import hashlib
        checksum = hashlib.md5()
        checksum.update(str(self.candidate.pk))
        checksum.update(self.fec_candidate_id or '')
        checksum.update(self.fec_office_id or '')
        checksum.update(self.fec_postal_id or '')
        checksum.update(self.fec_district_id or '')
        checksum.update(self.total_receipts or '')
        checksum.update(self.candidate_loans or '')
        checksum.update(self.other_loans or '')
        checksum.update(self.candidate_loan_repayments or '')
        checksum.update(self.other_loan_repayments or '')
        checksum.update(self.individual_contributions or '')
        checksum.update(self.pac_contributions or '')
        checksum.update(self.ending_cash or '')
        checksum.update(self.date_of_last_report or '')
        checksum.update(self.total_disbursements or '')
        return checksum.hexdigest()
    
    def save(self, *args, **kwargs):
        """
        Add the checksum
        """
        self.checksum = self.calculate_checksum()
        super(CandidateMoney, self).save(*args, **kwargs)
    

    class Meta:
        pass

    def __unicode__(self):
        return u"CandidateMoney"

class ElectionEvent(models.Model):
    """An event that is going to happen in an election"""
    event_code = models.CharField(primary_key=True, max_length=20)
    state = models.CharField(max_length=2)
    state_name = models.CharField(max_length=32)
    event_date = models.DateField()
    description = models.CharField(blank=True, max_length=255)
    checksum = models.CharField(max_length=32)
    
    def calculate_checksum(self):
        """
        Calculate the MD5 checksum for the record
        """
        import hashlib
        checksum = hashlib.md5()
        checksum.update(self.event_code)
        checksum.update(self.state or '')
        checksum.update(self.state_name or '')
        checksum.update(self.event_date.isoformat() or '')
        checksum.update(self.description or '')
        return checksum.hexdigest()
    
    def save(self, *args, **kwargs):
        """
        Add the checksum
        """
        self.checksum = self.calculate_checksum()
        super(ElectionEvent, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['event_date',]

    def __unicode__(self):
        return u" ".join([self.state, self.event_date.isoformat(), self.description])
