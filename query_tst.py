from collections import OrderedDict
from urllib.parse import urlencode

'''
 "params": "query=Materiais de Constru%C3%A7%C3%A3o&page=0&highlightPreTag=__ais-highlight__&highlightPostTag=__/ais-highlight__&filters=hide_prices:false AND available:true AND (campus_city:"Aracaju" OR campus_virtual:true) AND (campus_state_abbr:"SE" OR campus_virtual:true) AND offered_price<=10000&facets=["level","simplified_kind","simplified_level","simplified_shift","searchable_enrollment_semester","great_area","benefits"]&tagFilters="
                
'''

query_param = {
    "query": "Materiais de Constru%C3%A7%C3%A3o",
    "page": "0",
    "highlightPreTag": "__ais-highlight__",
    "highlightPostTag": "__/ais-highlight__",
    "filters": 'hide_prices:false AND available:true AND (campus_city:"Aracaju" OR campus_virtual:true) AND (campus_state_abbr:"SE" OR campus_virtual:true) AND offered_price<=10000',
    "facets": '["level","simplified_kind","simplified_level","simplified_shift","searchable_enrollment_semester","great_area","benefits"]',
    "tagFilters": ""
}

query_param = OrderedDict(
    [
        ("query", "Materiais de Constru%C3%A7%C3%A3o"),
        ("page", "0"),
        ("highlightPreTag", "__ais-highlight__"),
        ("highlightPostTag", "__/ais-highlight__"),
        ("filters", 'hide_prices:false AND available:true AND (campus_city:"Aracaju" OR campus_virtual:true) AND (campus_state_abbr:"SE" OR campus_virtual:true) AND offered_price<=10000'),
        ("facets", '["level","simplified_kind","simplified_level","simplified_shift","searchable_enrollment_semester","great_area","benefits"]'),
        ("tagFilters", ""),
    ]
)

print(urlencode(query_param).replace("+", "%20"))
