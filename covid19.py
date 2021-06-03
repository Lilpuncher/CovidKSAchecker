import sys
from pip._vendor import requests
import json
import datetime
input = sys.argv
counter1 = 0
for n in input:
    n = n.upper()
    input[counter1] = n
    counter1 += 1
def main(input):

    # If the user type too many or little arguments or the first(technically second because the first is the source file) argument is help
    if (len(input) != 2 or input[1] == "help"):
        print('Usage: "py covid19.py [active, confirmed, deaths, recoveries, tests]"')
        return
    api = requests.get('https://services6.arcgis.com/bKYAIlQgwHslVRaK/arcgis/rest/services/Cumulative_Date_Grouped_ViewLayer/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    apiser = json.loads(api.text)
    counter = 0
    tests = 0
    # Get the latest info
    for i in apiser['features']:
            
        confirmed = apiser['features'][counter]['attributes']['Confirmed']
        deaths = apiser['features'][counter]['attributes']['Deaths']
        recovered = apiser['features'][counter]['attributes']['Recovered']
        tests += apiser['features'][counter]['attributes']['Tested']
        time = apiser['features'][counter]['attributes']['Reportdt']
        counter += 1
    active = confirmed - (recovered + deaths)
    time = datetime.datetime.fromtimestamp(time / 1000)

    if (input[1] == "ACTIVE"):
        activedif = (apiser['features'][counter - 2]['attributes']['Confirmed']) - ((apiser['features'][counter - 1]['attributes']['Recovered'])+(apiser['features'][counter - 1]['attributes']['Deaths']))
        activedif = active - activedif
        print("Active cases in KSA are", active, ". Difference of", activedif,"from yesterday. Last updated:", time)
        return
    elif (input[1] == "CONFIRMED"):
        confirmeddif = confirmed - (apiser['features'][counter - 2]['attributes']['Confirmed'])
        print("Confirmed cases in KSA are", confirmed, ". Difference of", confirmeddif,"from yesterday. Last updated:", time)
        return
    elif (input[1] == "DEATHS"):
        deathsdif = deaths - apiser['features'][counter - 2]['attributes']['Deaths']
        print("Deaths in KSA are", deaths, ". Difference of", confirmeddif,"from yesterday. Last updated:", time)
        return
    elif (input[1] == "RECOVERIES"):
        recovereddif = recovered - apiser['features'][counter - 2]['attributes']['Recovered']
        print("Recoveries in KSA are", recovered, ". Difference of", recovereddif,"from yesterday. Last updated:", time)
        return
    elif (input[1] == "TESTS"):
        print("PCR tests taken in KSA are", tests , ". Last updated:", time)
        return
    else:
        print('Usage: "python main.py [active, confirmed, deaths, recoveries, tests]"')
        return
        
main(input)
