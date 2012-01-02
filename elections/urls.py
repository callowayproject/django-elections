from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from .models import (Candidate, RaceCounty, RaceDistrict, CountyResult, 
                    DistrictResult, CandidateOffice, CandidateEducation, 
                    CandidateOffice, CandidatePhone, CandidateURL)

urlpatterns = patterns('',
    # url(r'^$', 'views.index', name='index'),
    url(r'^candidates/$', ListView.as_view(model=Candidate), name='candidate_list'),
    url(r'^candidates/(?P<pk>\d+)/$', 
        DetailView.as_view(model=Candidate), 
        name='candidate_detail'),
    # url(r'^state/$'),
    # url(r'^state/districts/$'),
    # url(r'^state/pacs/$'),
    
)

urlpatterns += patterns('',
    url(r'^(?P<state>[A-Z][A-Z])/$', 'elections.views.state_detail', name="state_election_details"),
    url(r'^(?P<state>\w\w)/$', 'elections.views.lc_state_redirect', name="lc_state_redirect"),
    
)