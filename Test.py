import  csv
import pickle
csv_file = open("data_files/30thoct.csv", 'r')
reader = csv.reader(csv_file)

email_list = []
filing_status_list = []
mid_list = []
for row in reader:
    mid_list.append(row[0])
    filing_status_list.append(row[1])
    email_list.append(row[2])

mid_list, filing_status_list, email_list = mid_list[1:], filing_status_list[1:], email_list[1:]

data_dict = {}
for i in range(len(email_list)):
    data_dict[email_list[i]] = ({'filing_staus' : filing_status_list[i], 'mid_status' : mid_list[i]} )
print data_dict


pickle.dump(data_dict, open("data_files/formated_data.pkl", "w"))



