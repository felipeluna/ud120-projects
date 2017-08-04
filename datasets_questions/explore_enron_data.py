#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint

pp = pprint.PrettyPrinter(depth=6)
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print enron_data
# pois = open("../final_project/poi_names.txt").read().split('\n')[2:-1]
# print pois
poi = {k: v for k, v in enron_data.iteritems() if v['poi'] == True }
salary = {k: v for k, v in enron_data.iteritems() if v['salary'] != 'NaN' }
salary = {k: v for k, v in enron_data.iteritems() if v['salary'] != 'NaN' }
email = {k: v for k, v in enron_data.iteritems() if v['email_address'] != 'NaN' }
missing_payments = {k: v for k, v in enron_data.iteritems() if v['total_payments'] == 'NaN' }
have = {k: v for k, v in enron_data.iteritems() if v['total_payments'] != 'NaN' }
poi_missing_payments = {k: v for k, v in enron_data.iteritems() if v['total_payments'] == 'NaN'  and v['poi'] == True}
print len(salary.keys())
print len(email.keys()) 
print len(missing_payments.keys())
print len(have.keys())
print len(poi_missing_payments.keys())
print len(enron_data)
print len(poi.keys())
# pp.pprint(missing_payments)
