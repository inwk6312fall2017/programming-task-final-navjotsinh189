from weather import Weather
weather = Weather()
def lookuplocation(halifax):
    location = weather.lookup_by_location(halifax)
    print(location)
    condition = location.condition()    
    forecasts = location.forecast()
    while len(forecasts) > 5:
        forecasts.pop()
    
    temp = []
    for item in forecasts:
        high_temp = item['high']
        temp.append(int(high_temp))

    for item in forecasts:
        if int(item['high']) == min(temp):
            print("The day that has lowest tempeture next 5 days in halifax is %s " % (item['date']))
            print("The lowest tempeture next 5 days is %s " % (item['high']))
            print("The weather condition of the day that has lowest tempeture next 5 days is %s " % (item['text']))
        
     for item in forecasts:
        if int(item['high']) == max(temp):
            print("The day having higest tempeture next 5 days  in halifax is %s " % (item['date']))
            print("The higest tempeture next 5 days is %s " % (item['high']))
            print("The weather condition of the day having higest tempeture in next 5 days is %s " % (item['text']))

        elif item['text'] == 'rain':
            print("The day that will be rainy is " % (item['date']))



lookuplocation('halifax')
