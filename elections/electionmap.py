# n.races[0].reporting_units[0].results
from elections.ap import AP
from elections.settings import FTP_USER, FTP_PASSWORD, MAP_RESULTS_DEST
import os
try:
    import json
except ImportError:
    import simplejson as json

colors = ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', 
'#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD', '#CCEBC5', '#FFED6F', '#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', 
'#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD', '#CCEBC5', '#FFED6F','#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', 
'#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD', '#CCEBC5', '#FFED6F','#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', 
'#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD', '#CCEBC5', '#FFED6F','#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', 
'#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD', '#CCEBC5', '#FFED6F',]
legend_tmpl = "<tr><td style='width=32px;background-color:%(color)s'>&nbsp;</td><td>%(name)s</td><td>%(vote_total)s</td><td>%(vote_percent)#.2f%%</td></tr>"


def parse_race(race):
    """
    Loop through the reporting units and return a dict for output
    """
    county_results = {} # key = county number
    county_winners = {} # key = county number, 
    candidate_colors = {}
    legend = ['<table id="legendtable">']
    candidates = []
    total_votes = 0
    
    for i, cand in enumerate(race.candidates):
        cand_vote_total = getattr(cand, 'vote_total', 0)
        total_votes += cand_vote_total
        candidate_colors[cand.ap_natl_number] = colors[i]
        candidates.append({
            'name': cand.name, 
            'color': colors[i], 
            'vote_total': cand_vote_total, 
            'vote_percent': 0, 
            'delegates': cand.delegates,
        })
    
    candidates.sort(key=lambda x: x['vote_total'], reverse=True)
    for cand in candidates:
        if total_votes:
            cand['vote_percent'] = round(cand['vote_total']/float(total_votes) * 100, 1) 
        else:
            cand['vote_percent'] = 0.0
        legend.append(legend_tmpl % cand)
    legend.append('</table>')
    
    for county in race.counties:
        winning_votes = 0
        county_results[county.fips] = {
            "name": county.name,
            "precincts_reporting": county.precincts_reporting,
            "precincts_reporting_percent": county.precincts_reporting_percent,
            "precincts_total": county.precincts_total,
            "results": []
        }
        for result in county.results:
            county_results[county.fips]['results'].append({
                "ap_natl_number": result.candidate.ap_natl_number,
                "name": result.candidate.name,
                "vote_total": result.vote_total,
                "vote_total_percent": round(result.vote_total_percent, 1),
            })
            if result.vote_total > winning_votes:
                winning_votes = result.vote_total
                county_winners[county.fips] = result.candidate.ap_natl_number
        county_results[county.fips]['results'].sort(key=lambda x: x['vote_total'], reverse=True)
    
    return {
        "candidate_colors": candidate_colors, 
        "legend": "".join(legend),
        "county_results": county_results,
        "county_winners": county_winners
    }

def write_results(electiondate):
    # Use county_winners to color states using candidate_colors
    client = AP(FTP_USER, FTP_PASSWORD)
    n = client.get_nation(electiondate)
    
    
    # Detail county results
    for race in n.races:
        party = race.party
        state = race.state.abbrev
        results = parse_race(race)
        f = open(os.path.join(MAP_RESULTS_DEST, "%s-%s-%s.json" % (electiondate, party, state)), "w")
        f.write(json.dumps(results))
        f.close()