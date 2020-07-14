# You don't have to use these classes, but we recommend them as a good place to start!
import pandas as pd
import matplotlib.pyplot as plt
import pymongo

class MongoHandler():
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.mydb = self.myclient['football_database']
        self.myCollection = self.mydb['football_collection'] 

    def upload(df,myCollection):
        
        list = []
        for x in df.index:
            team_entry = {'Team': x, \
                          "Total Goals Scored": df.at[x,'TotalGoalsScored'], \
                          "Total Wins": df.at[x,'TotalWins'], \
                          "Win Percentage In Rain": df.at['Aachen','WinPercentageInRain']}
        list.append(team_entry)
        
        print("Dataframe uploaded into MongoDB!")


# class WeatherGetter(object):

# 	def __init__(self):
#         self.lat = "52.5200"
#         self.long = "13.4050"

        
    
  
    
#     def weather(lat,long,year,month,day,hours,minutes,seconds):
        
#         resp = requests.get('https://api.darksky.net/forecast/{}/{},{},{}-{}-{}T{}:{}:{}?units=si&exclude=daily,minutely,hourly,alerts,flags'.format(token,lat,long,year,month,day,hours,minutes,seconds))
        
#         weather_data = resp.json()
        
#         return weather_data
    
    
    
    
#     def raincheck(x):
        
#         list = ['Possible Drizzle','Possible Light Rain','Light Rain','rain']
        
#         if weather_data['WeatherSummary'][x] in list:
#             return True
#         else:
#             return False

        
def winplot(team_name, df):
 
    plt.style.use('ggplot')

    wins = df.loc["{}".format(team_name),"TotalWins"]
    losses = df.loc["{}".format(team_name),"TotalLosses"]
    data = [wins,losses]

    labels = ["Wins","Losses"]
    x_pos = [i for i, _ in enumerate(labels)]

    plt.bar(x_pos, data, color='green')

    plt.ylabel("Games")
    plt.title("{}".format(team_name))

    plt.xticks(x_pos, labels)

    plt.show()
