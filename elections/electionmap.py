# n.races[0].reporting_units[0].results
from elections.ap import AP
from elections.settings import FTP_USER, FTP_PASSWORD
import json
import pprint

colors = ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', '#FDB462', 
'#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD', '#CCEBC5', '#FFED6F', ]
county_results = {} # key = county number
county_winners = {} # key = county number, 
candidate_colors = {}
legend_tmpl = "<tr><td style='width=32px;background-color:%s'>&nbsp;</td><td>%s</td></tr>"
legend = ['<table id="legendtable">']

# Use county_winners to color states using candidate_colors
client = AP(FTP_USER, FTP_PASSWORD)
n = client.get_nation('20120103')

for i, cand in enumerate(n.races[0].candidates):
    candidate_colors[cand.ap_pol_number] = colors[i]
    legend.append(legend_tmpl % (colors[i], cand.name))
legend.append('</table>')

# Detail county results
for county in n.races[0].reporting_units:
    winning_votes = 0
    county_results[county.fips] = []
    for result in county.results:
        if county.is_state:
            continue
        county_results[county.fips].append({
            "name": result.candidate.name,
            "vote_total": result.vote_total,
            "vote_total_percent": round(result.vote_total_percent, 1)
        })
        if result.vote_total > winning_votes:
            winning_votes = result.vote_total
            county_winners[county.fips] = result.candidate.ap_pol_number
    county_results[county.fips].sort(key=lambda x: x['vote_total'], reverse=True)
f = open("election.json", "w")
f.write(json.dumps({
    "candidate_colors": candidate_colors, 
    "legend": "".join(legend),
    "county_results": county_results,
    "county_winners": county_winners}))
f.close()