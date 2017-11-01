import pickle
import sys

from preprocess import feature_format,targetFeatureSplit

data_dict = pickle.load(open("data_files/formated_data.pkl","r"))

print data_dict

feature_list = ["GTM", "filing_status"]

data = feature_format(data_dict,feature_list)
print data