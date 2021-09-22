from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import sys

ZomatoData = pd.read_csv('zomato.csv',encoding="latin1")
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine,Price):
    TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
    if Price.lower()=='under300':
        TEMP1 = TEMP[TEMP['Average Cost for two']<300]
    elif Price.lower() == 'between300to700':
        TEMP1 = TEMP[(TEMP['Average Cost for two']>=300) & (TEMP['Average Cost for two']<=700)]
    else:
        TEMP1 = TEMP[TEMP['Average Cost for two']>700]
    TEMP2 = TEMP1[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]
    TEMP2.sort_values(by='Aggregate rating',ascending=False,inplace=True)
    return TEMP2[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        #config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        loc = tracker.get_slot('location').lower()
        cuisine = tracker.get_slot('cuisine').lower()
        price = tracker.get_slot('price').lower()
        
        operatingCities = [x.lower() for x in WeOperate]
        if loc.lower() in operatingCities:
            
            results = RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
            response=""
            if results.shape[0] <5:
                response= "Please try different selections? We do not have results for these values."
            else:
                response = "Displaying top restaurants as per selection: \n"
               # print("Showing top rated restaurants as per your selections: \n")
                for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
                    restaurant = restaurant[1]
                    
                    response=response + F"\n Found: {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']}. \n\n"
                emailRequest = "\n\nDo you want the results to be sent to you as an email?"
                response=response + emailRequest
        else:
            response = "We do not serve in this area yet."
        dispatcher.utter_message("-----"+response)
        return [SlotSet('location',loc)]

class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher,tracker,domain):
        
        loc = tracker.get_slot('location').lower()
        cuisine = tracker.get_slot('cuisine').lower()
        price = tracker.get_slot('price').lower()
        response = RestaurantSearch(loc,cuisine,price).iloc[:10]
        
        EmailConfirmation=tracker.get_slot('emailConfirmation').lower()
        Recipient = tracker.get_slot('to')#"tejaswinishreyadsc23@gmail.com"
        print("Recipient is ",Recipient)
        if EmailConfirmation=='yes':
            if Recipient == None:
                dispatcher.utter_message("Please enter email ID")
            else:
                msg = MIMEMultipart()
                msg['Subject'] = 'Top rated restaurants'
                msg['From'] = 'tejaswinishreyadsc23@gmail.com'
                msg['To']=Recipient
                
                html = """\
                <html>
                  <head></head>
                  <body>
                    {0}
                  </body>
                </html>
                """.format(response.to_html())
                
                part1 = MIMEText(html, 'html')
                
                msg.attach(part1)
                
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                
                server.login("tejaswinishreyadsc23@gmail.com", "chatB0T!")  
                server.sendmail(msg['From'], msg['To'] , msg.as_string())
                
               
                server.quit()  
        
                dispatcher.utter_message("Message sent successfully. Bon apetit!")
                return [SlotSet("to",Recipient)]
        else:
            dispatcher.utter_message("Good day. Bon apetit!")



