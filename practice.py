dict = {'Anupam':{'GTM': 1, 'wife': 'swati'}, 'Amar' : {'GTM': 0, 'wife': 'Nidhi'}, 'Dev' : {'GTM': 2, 'wife': 'Garima'} }


from sklearn.preprocessing import LabelEncoder

print float(dict['Anupam']['wife'])
lb = LabelEncoder()
tmp = []
i = 0
for key in dict.keys():
    for feature in dict.values()[0].keys():
        if isinstance(dict[key][feature], str):
            tmp.append(dict[key][feature])
            print tmp
            tmp_lable = lb.fit_transform(tmp)
            print tmp_lable





print lb.inverse_transform(tmp_lable)

#for key in range(len(dict.keys())):
    #print dict.values()[key]
    #lt.append(dict.values()[key].values()[1])
    #print lb.fit_transform(dict.values()[key].values())

#tp = lb.fit_transform(lt)
#print tp, dict
#print lb.inverse_transform(tp)




