import csv
import datetime as dt
import sys
from datetime import datetime

def days_diff(date1, date2):
    d1 = datetime.strptime(str(date1), "%m/%d/%Y")
    d2 = datetime.strptime(str(date2), "%m/%d/%Y")
    return abs((d2 - d1).days)

def process_file(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        fraudCheck = {}
        priorPurch = {}
        fraudReport = {}
        for row in reader:
            # Example code: You can parse the date from a record with:
            date = dt.datetime.strptime(row[0], "%m/%d/%Y")
            acnt_id = row[1]
            event_type = row[2]
            if priorPurch.__contains__(acnt_id):
                priorPurch[acnt_id] = priorPurch[acnt_id] + 1
            else:
                priorPurch[acnt_id] = 0
            if event_type == "PURCHASE":
                if fraudReport.__contains__(acnt_id):
                    print(str(date.date()) + "," + acnt_id + ",FRAUD_HISTORY"+":"+str(fraudReport[acnt_id]))
                else:
                    if fraudCheck.__contains__(acnt_id):
                        try:
                            tempDate = sorted(fraudCheck[acnt_id])
                            if days_diff(tempDate[0],date.strftime('%m/%d/%Y')) > 90:
                                count = 0
                                for d in fraudCheck[acnt_id]:
                                    if days_diff(d,date.strftime('%m/%d/%Y')) > 90:
                                        count = count+1
                                print(str(date.date()) + "," + acnt_id + ",GOOD_HISTORY"+":"+str(count))
                            else:
                                print(str(date.date()) + "," + acnt_id + ",UNCONFIRMED_HISTORY"+":"+str(priorPurch[acnt_id]))
                            temp1 = fraudCheck[acnt_id]
                            temp1.append(date.strftime('%m/%d/%Y'))
                            fraudCheck[acnt_id] = temp1
                        except:
                            print("acnt_id : "+acnt_id)
                    else:
                        temp=[]
                        temp.append(date.strftime('%m/%d/%Y'))
                        fraudCheck[acnt_id] =  temp
                        print(str(date.date()) + "," + acnt_id + ",NO_HISTORY")
            elif event_type == "FRAUD_REPORT":
                fraudReport[acnt_id] = 1
                if fraudReport.__contains__(acnt_id):
                    fraudReport[acnt_id] = fraudReport[acnt_id] + 1
                else:
                    fraudReport[acnt_id] = 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expecting a singular file argument.")
    else:
        process_file(sys.argv[1])