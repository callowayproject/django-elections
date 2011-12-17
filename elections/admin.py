from django.contrib import admin
from .models import (Candidate, RaceCounty, RaceDistrict, CountyResult, 
                    DistrictResult, CandidateOffice, CandidateEducation, 
                    CandidateOffice, CandidatePhone, CandidateURL, 
                    ElectionEvent)

class EducationInline(admin.TabularInline):
    model = CandidateEducation
    fields = ('degree', 'major', 'school_name', 'school_type')
    extra = 0


class OfficeInline(admin.TabularInline):
    model = CandidateOffice
    fields = ('office',)
    extra = 0

class PhoneInline(admin.TabularInline):
    model = CandidatePhone
    fields = ('phone_number',)
    extra = 0

class URLInline(admin.TabularInline):
    model = CandidateURL
    fields = ('url',)
    extra = 0

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'timestamp',)
    list_filter = ('gender', 'religion', 'ethnicity',)
    search_fields = ('last_name', 'first_name')
    
    fieldsets = (
        (None, {
            'fields': (('first_name', 'middle_name', 'last_name', 'junior'), ('residence_place', 'residence_state')),
        }),
        ('Demographics', {
            'fields': ('gender', ('ethnicity', 'hispanic'), 'religion',)
        }),
        ('Birth Info', {
            'fields': ('birth_date', ('birth_place', 'birth_state', 'birth_country'), 'birth_province',)
        }),
        ('Other Info', {
            'fields': ('year_first_elected', 'biography', 'profile', 'campaigns')
        })
    )
    
    inlines = [
        EducationInline, OfficeInline, PhoneInline, URLInline,
    ]

class ElectionEventAdmin(admin.ModelAdmin):
    list_display = ('state', 'event_date', 'description')
    list_filter = ('state',)
    date_hierarchy = 'event_date'
    search_fields = ('state', 'description')


admin.site.register(RaceCounty)
admin.site.register(RaceDistrict)
admin.site.register(CountyResult)
admin.site.register(DistrictResult)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(ElectionEvent, ElectionEventAdmin)
# admin.site.register(CandidateOffice)
# admin.site.register(CandidateEducation)
# admin.site.register(CandidatePhone)
