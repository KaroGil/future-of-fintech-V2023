import json

f = open('future-of-fintech-V2023\data\providers.json')
f2 = open('future-of-fintech-V2023\data\consumption.json')

provider_data = json.load(f)
consumption_data = json.load(f2)

for i in consumption_data:
    if i['consumptionUnit'] != "kWh":
        print(i)    #doesnt print out anything 

f.close()