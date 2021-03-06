from sensor import timer
from io import StringIO
import sys
import time

class Alert():
  def __init__(self, name="Default"):
    self.name = name
    # sensor data
    self.data = {'blood_pressure_low':0,'blood_pressure_high':0,'blood_oxygen':0,'heart_rate':0,'awRR':0}
    # threshold 
    self.thres_bp_high = 0
    self.thres_bp_low = 0
    self.thres_bo = [0,0]
    self.thres_hr = [0,0]
    self.thres_awRR = [0,0]
    # previoud data
    self.previous_data = {}
    # alert message
    self.alert = []
    # time
    self.time_hr_large = []

  def check(self, data={'blood_pressure_low':80,'blood_pressure_high':120,'blood_oxygen':99,'heart_rate':90,'awRR':18}):
    self.data = data
    self.alert = []
    # orthostatic hypotension
    # if (self.previous_data != {}):
    #   dec_blood_pressure_low = self.previous_data['blood_pressure_low'] - data['blood_pressure_low']
    #   if dec_blood_pressure_low > 20:
    #     w1 = "Warning: orthostatic hypotension"
    #     self.alert.append(w1)
    #     print(w1)

    # normal hypertension and isolated systolic Hypertension
    if data['blood_pressure_high'] > 140 and data['blood_pressure_low'] > 90:
      w2 = "Warning: Hypertension"
      if w2 not in self.alert:
        self.alert.append(w2)
      # print(w2)
    elif data['blood_pressure_high'] > 140 and data['blood_pressure_low'] < 90:
      w3 = "Warning: isolated systolic Hypertension"
      if w3 not in self.alert:
        self.alert.append(w3)
      # print(w3)

    # heart rate
    # if data['heart_rate'] > 100 and self.previous_data['heart_rate'] > 100:
    if data['heart_rate'] > 100 :
      w4 = "Warning: Tachycardia"
      if w4 not in self.alert:
        self.alert.append(w4)
      # print(w4)
    elif data['heart_rate'] < 60 :
      w5 = "Warning: Bradycardia"
      if w5 not in self.alert:
        self.alert.append(w5)
      # print(w5)

    # blood oxygen 
    if data['blood_oxygen'] < 75:
      w6 = "Emergency: blood oxygen < 75% , may lose conscious"
      if w6 not in self.alert:
        self.alert.append(w6)
      # print(w6)
    elif data['blood_oxygen'] < 80:
      w7 = "Emergency: blood oxygen < 80% , may impair mental function"
      if w7 not in self.alert:
        self.alert.append(w7)
      # print(w7)
    elif data['blood_oxygen'] < 90:
      w8 = "Warning: blood oxygen < 90% , may cause hypoxia"
      if w8 not in self.alert:
        self.alert.append(w8)
      # print(w8)

    # awRR or respiratory rate
    if data['awRR'] < 12:
      w9 = "Warning: hard to breathe"
      if w9 not in self.alert:
        self.alert.append(w9)
      # print(w9)

    # self.previous_data = data
    return self.alert

if __name__ == '__main__':
  a = Alert('new');
  while True :
    print(a.check(timer(0,0,1)))
