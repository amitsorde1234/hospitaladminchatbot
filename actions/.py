# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
import requests
from requests.packages import urllib3
import pyrebase
import pandas as pd
print(urllib3.__file__)
print(urllib3.__version__)

firebaseConfig = {
    "apiKey": "AIzaSyAhPizzv5U4iv7eVj5Y8A6OZPSxV6Zl7Ck",
    "authDomain": "hospitalchatbot-9346d.firebaseapp.com",
    "databaseURL": "https://hospitalchatbot-9346d.firebaseio.com",
    "projectId": "hospitalchatbot-9346d",
    "storageBucket": "hospitalchatbot-9346d.appspot.com",
    "messagingSenderId": "919546343363",
    "appId": "1:919546343363:web:beed86bf39932b66ab1776",
    "measurementId": "G-T0LZM54LQ4"
  }
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
cred = credentials.Certificate('C:/Users/amit/OneDrive/Desktop/new/healthadmin/actions/hospital.json')
firebase_admin.initialize_app(cred) 
db = firestore.client()
doc_ref = db.collection(u'hospital_chatbot').document(u'actions1')

doc = doc_ref.get()
data=doc.to_dict()
#appoi=data["appointment_list"]
#appoi=pd.DataFrame(appoi)
#appoi["status"].loc[appoi["user_id"]=="12334"]="cancel"
#appo={"name":list(appoi["name"]),"user_id":list(appoi["user_id"]),"Doctor":list(appoi["Doctor"]),"Specialist":list(appoi["Specialist"]),"schedule":list(appoi["schedule"]),"status":list(appoi["status"])}
#doc_ref.update({"appointment_list":appo})
#print(pd.DataFrame(appo))


class User(object):
    def __init__(self):
        self.name=" "
    def __set__(self, instance, name):
        self.name=name
    def __get__(self, instance, owner):
        return self.name
    def __delete__(self, instance):
        print("deleted in descriptor object")
        del self.name


class username(object):
    user=User()
uname=username()

class unumber(object):
    def __init__(self):
        self.number=" "
    def __set__(self, instance, number):
        self.number=number
    def __get__(self, instance, owner):
        return self.number
    def __delete__(self, instance):
        print("deleted in descriptor object")
        del self.number

class usernumber(object):
    no=unumber()
unumber=usernumber()

del unumber.no
del uname.user

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_i_admin"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            try:
                person = tracker.get_slot('PERSON')
                dispatcher.utter_message(text=person+" tell your username")
            except:
                dispatcher.utter_message(text="please tell your name")
                dispatcher.utter_message(template="action_i_admin")

            return []

class use(Action):
    def name(self) -> Text:
        return "action_username"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            user1 = tracker.get_slot('user')
            uname.user=user1
            dispatcher.utter_message(text=" your password please" )
            return []


class passw(Action):
    def name(self) -> Text:
        return "action_password"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            phone = tracker.get_slot('phonenumber')            
            try:
                unumber.no=phone
                password=unumber.no
                print(password)
                logname=uname.user
                print(logname)
                print(unumber.no)
                login = auth.sign_in_with_email_and_password(logname,password) 
                dispatcher.utter_message(text="ok "+ logname +" this are the options")
                dispatcher.utter_message(buttons = [
                   {"payload": "/to_schedule", "title": "today's schedule"},
                   {"payload": "/tomar_schedule", "title": "tommorrow's schedule"},
                   {"payload": "/user_data", "title": "User data"},
                   {"payload": "/update_data", "title": "update"},
                   {"payload": "/cancel_appointment", "title": "cancel_appointment"}
                   ])
            except:
                try:
                    dispatcher.utter_message(text="there may be your username or password worng")
                    del unumber.no
                    del uname.user
                except:
                    dispatcher.utter_message(text="please give me again email amd password aagin")
            return []



class today(Action):
    def name(self) -> Text:
        return "action_get_schedule"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            doc = doc_ref.get()
            try:
                unumber.no
                uname.user
                if doc.exists:
                    data=doc.to_dict()
                    print(pd.DataFrame(data['today_list']))
                    x=pd.DataFrame(data['today_list'])
                    dispatcher.utter_message(text="username "+ uname.user)
                    data=[]
                    for i in range(0,len(x)):
                        dispatcher.utter_message(text=x["time_and_data"][i]+"."+"="+"."+x["user"][i])
                else:
                    print(u'No such document!')           
            except:
                dispatcher.utter_message(text="please login to get the data first give username and password")
                       
            return []

class tomarro(Action):
    def name(self) -> Text:
        return "action_get_tomarro_schedule"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            doc = doc_ref.get()
            try:
                unumber.no
                uname.user
                if doc.exists:
                    data=doc.to_dict()
                    print(pd.DataFrame(data['today_list']))
                    x=pd.DataFrame(data['today_list'])
                    dispatcher.utter_message(text="username "+ uname.user)
                    data=[]
                    for i in range(0,len(x)):
                        dispatcher.utter_message(text=x["time_and_data"][i]+"."+"="+"."+x["user"][i])
                else:
                    print(u'No such document!')              
            except:
                dispatcher.utter_message(text="please login to get the data first give username and password")
            return []


class user_da(Action):
    def name(self) -> Text:
        return "action_user_data"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            doc = doc_ref.get()
            try:
                unumber.no
                uname.user
                if doc.exists:
                    data=doc.to_dict()
                    print(data['user_data'])
                    x=pd.DataFrame(data['user_data'])
                    data=[]
                    for i in x.keys():
                         data.append([i,"=",x[i][0]])
                    dat=pd.DataFrame(data)
                    dispatcher.utter_message(text="username "+uname.user)
                    dispatcher.utter_message(text=str(dat))
                else:
                    print(u'No such document!')           
            except:
                dispatcher.utter_message(text="please login to get the data")
            return []

class updatee(Action):
    def name(self) -> Text:
        return "action_update"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            try:
                print(unumber.no)
                print(uname.user)
                dispatcher.utter_message(text="you can update your name ,modile number, cancal the appointment \n example \n 1. change my name OLD NAME_to_NEW NAME \n 1. change my number OLD NUMBER_to_NEW NUMBER")
            except:
                dispatcher.utter_message(text="please login to update") 
            return []


class upname(Action):
    def name(self) -> Text:
        return "action_change_name"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            doc = doc_ref.get()
            try:
                unumber.no
                uname.user
                phone = tracker.get_slot('upname')
                namee=phone.split("_")
                try:
                    doc_ref.update({"doctor_list.Doctor":[namee[2]]})
                    dispatcher.utter_message(text="your name is changed")
                except:
                    dispatcher.utter_message(text="you are giving new name in wrong fromate\n type OLD NAME__to__NEW NAME")
            except:       
                dispatcher.utter_message(text="please login to update") 
            
            if doc.exists:
                data=doc.to_dict()
                print(data['doctor_list'])
                x=pd.DataFrame(data['doctor_list'],index=None)
                print(x)
                dispatcher.utter_message(text=str(x))
            return []

class number(Action):
    def name(self) -> Text:
        return "action_change_number"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            try:
                unumber.no
                uname.user
                phone = tracker.get_slot('upnumber')
                namee=phone.split("_")
                try:
                    doc_ref.update({"doctor_list.contact_detail":[namee[2]]})
                    dispatcher.utter_message(text="your mobile number is changed")
                except:
                    dispatcher.utter_message(text="you are giving new name in wrong fromate\n type OLD NAME__to__NEW NAME")
            except:       
                dispatcher.utter_message(text="please login to update") 
            if doc.exists:
                data=doc.to_dict()
                print(data['doctor_list'])
                x=pd.DataFrame(data['doctor_list'],index=None)
                dispatcher.utter_message(text=str(x))
            return []

class appoint(Action):
    def name(self) -> Text:
        return "action_appointment"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            try:
                unumber.no
                uname.user
                dispatcher.utter_message(text="cancal the appointment type \n user_id_123445")
            except:       
                dispatcher.utter_message(text="please login to update") 
            return []

class user_id(Action):
    def name(self) -> Text:
        return "action_appointment_user_id"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            doc = doc_ref.get()
            data=doc.to_dict()
            try:
                unumber.no
                uname.user
                user = tracker.get_slot('user_id')
                print(user)
                user=user.split("_")
                print(user)
                try:
                    appoi=data["appointment_list"]
                    appoi=pd.DataFrame(appoi)
                    appoi["status"].loc[appoi["user_id"]==user[2]]="cancel"
                    appo={"name":list(appoi["name"]),"user_id":list(appoi["user_id"]),"Doctor":list(appoi["Doctor"]),"Specialist":list(appoi["Specialist"]),"schedule":list(appoi["schedule"]),"status":list(appoi["status"])}
                    doc_ref.update({"appointment_list":appo})
                    dispatcher.utter_message(text="appointment is cancel")
                except:
                    dispatcher.utter_message(text="you have enter wrong user id")
            except:       
                dispatcher.utter_message(text="please login to update") 
            appoi=pd.DataFrame(appoi)
            dispatcher.utter_message(text=str(appoi))
            return []


class signouu(Action):
    def name(self) -> Text:
        return "action_signout"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            del unumber.no
            del uname.user
            return []


class help(Action):
    def name(self) -> Text:
        return "action_help"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            helpp="for geting start typ username secound password \n for end the session signout \n you can get todays timetable,tomorrow timeble ,user data\n you can update  name,mobile number (old name_to_new name),(old number_to_new number)\n for cancel the apointment give the user id of patient(user_id_123223)"
            dispatcher.utter_message(text=str(helpp))
            return []
