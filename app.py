import requests

class IRCTC:
  
  def __init__ (self):
    user_input = input("""
    Welcome to Train schedule
    Type 'OK' to proceed: """)

    if user_input == "OK":
      self.train_schedule()
    else:
      print("ERROR")
      
  def train_schedule(self):
    train_no = input("Enter the Train number: ")
    self.fetch_data(train_no)
  
  def fetch_data(self, train_no):
    data = requests.get("http://indianrailapi.com/api/v2/TrainSchedule/apikey/<api_key>/TrainNumber/{}".format(train_no))
    data = data.json()
    print(data['Route'])
    
    for i in data:
      print (i['StationName'], '|', i['ArrivalTime'], '|', i['DepartureTime'], '|', i['Distance'])

object = IRCTC()
