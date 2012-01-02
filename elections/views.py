from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _


from .models import (Candidate, RaceCounty, RaceDistrict, CountyResult, 
                    DistrictResult, CandidateOffice, CandidateEducation, 
                    CandidateOffice, CandidatePhone, CandidateURL, 
                    ElectionEvent)

def state_detail(request, state):
    """
    Get a list of stuff for the state
    """
    offices = CandidateOffice.objects.filter(state=state, status_id__in=["I", "Q"])
    events = ElectionEvent.objects.filter(state=state)
    if offices:
        return render_to_response(
            "elections/state_detail.html", 
            {
                "offices": offices,
                "state": offices[0].state_name,
                "events": events,
            },
            context_instance=RequestContext(request))
    else:
        raise Http404

def lc_state_redirect(request, state):
    """
    Redirect a mixed- or lower- case state into an upper case state
    """
    return HttpResponseRedirect(reverse('state_election_details', kwargs={'state': state.upper()}))
    