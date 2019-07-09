import os
import sys
import requests

#Function to calculate success rate
def rate(succ, req):
  succ = float(succ)
  req = float(req)
  
  #Calculate the percentage upto 2 decimals
  succ_rate = '{0:.2f}'.format((succ / req * 100))
  return succ_rate

#Function to print to standard output and file
def out_file(app, ver, succ_rate):
    print app + "\t\t" + ver + "\t\t" + succ_rate + "\n"
    with open ("file.txt", "a") as file:
        file.write(app + "\t\t" + ver + "\t\t" + succ_rate + "\n")

if __name__=='__main__':
  print "App" + "\t\t" + "Version" + "\t\t" + "Success_Rate"

  with open ("file.txt", "a") as file:
    file.write("App" + "\t\t" + "Version" + "\t\t" + "Success_Rate" + "\n")

  #Reading the servers file line by line
  with open("servers.txt") as f:
    for line in f:
      resp = requests.get(line)
      
      #The requests library should return a dictionary similar to the below:
      #resp = {"Application":"Cache2","Version":"1.0.1","Uptime":4637719417,
      #        "Request_Count":5194800029,"Error_Count":1042813251,"Success_Count":4151986778}

      #resp = resp.json()                 #This line is required only if response not in json

      succ = resp["Success_Count"]
      req = resp["Request_Count"]
      
      #Function to calculate success rate
      succ_rate = rate(succ, req)

      app = resp["Application"]
      ver = resp["Version"]
      
      #Function to print to standard output and file
      out_file(app, ver, succ_rate)

