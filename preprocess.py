import numpy as np
from sklearn.preprocessing import  LabelEncoder
def feature_format(dictionary, features, remove_null = True, remove_all_zeroes= True, remove_any_zeroes= False,sort_keys=False):

    lb = LabelEncoder()

    return_list = []
    transform_list = []
    i=0


    # Key order - first branch is for Python 3 compatibility on mini-projects,
    # second branch is for compatibility on final project.
    if isinstance(sort_keys, str):
        import pickle
        keys = pickle.load(open(sort_keys, "rb"))
    elif sort_keys:
        keys = sorted(dictionary.keys())
    else:
        keys = dictionary.keys()

    for key in keys:
        tmp_list = []
        for feature in features:
            try:
                dictionary[key][feature]

            except KeyError:
                print "error: key ", feature, " not present"
                return
            value = dictionary[key][feature]
            if value == 'NULL' and remove_null:
                dictionary[key][feature] = 0

            #get integer lables for string values in feature
            try:
                float(value)
            except:
                if ValueError():
                    if value not in transform_list:
                        transform_list.append(value)
    string_labels = lb.fit_transform(transform_list)
    print string_labels
    print transform_list

            #try:
                #tmp_list.append(float(value))
    for key in keys:
        tmp_list = []
        for feature in features:
            try:
                dictionary[key][feature]

            except KeyError:
                print "error: key ", feature, " not present"
                return
            value = dictionary[key][feature]


            try:
                tmp_list.append(float(value))
            except:
                if ValueError():
                    index = transform_list.index(value)
                    value = string_labels[index]
                    tmp_list.append(float(value))


        # Logic for deciding whether or not to add the data point.
        append = True
        # exclude 'poi' class as criteria.
        if features[0] == 'GTM':
            test_list = tmp_list[1:]
        else:
            test_list = tmp_list
        ### if all features are zero and you want to remove
        ### data points that are all zero, do that here
        if remove_all_zeroes:
            append = False
            for item in test_list:
                if item != 0 and item != "NULL":
                    append = True
                    break
        ### if any features for a given data point are zero
        ### and you want to remove data points with any zeroes,
        ### handle that here
        if remove_any_zeroes:
            if 0 in test_list or "NULL" in test_list:
                append = False
        ### Append the data point if flagged for addition.
        if append:
            #return_list.append(np.array(tmp_list))
            return_list.append((tmp_list))

   # for k in range(len(return_list)):
    #    for j in range(len(return_list[0])):
     #       if isinstance(return_list[0][j], str):
      #          la.append(return_list[k][j])
    #print "this is: ",  la
    #int_mapped= lb.fit_transform(la)
    #for k in range(len(return_list)):
     #  for j in range(len(return_list[0])):
     #       la[k] = [return_list[k][0] , int_mapped[k]]
    #print la
    #print int_mapped
    print return_list
    return np.array(return_list)

def targetFeatureSplit( data ):
    """
        given a numpy array like the one returned from
        featureFormat, separate out the first feature
        and put it into its own list (this should be the
        quantity you want to predict)

        return targets and features as separate lists

        (sklearn can generally handle both lists and numpy arrays as
        input formats when training/predicting)
    """

    target = []
    features = []
    for item in data:
        target.append( item[0] )
        features.append( item[1:] )

    return target, features

if __name__ == '__main__':
    dict = {'Anupam': {'GTM': 1, 'wife': 'NULL', 'CTM' : "Anu"}, 'Amar': {'GTM': '33', 'wife': 'Nidhi', 'CTM' : "Ama"},
            'Dev': {'GTM': '11', 'wife': 'raman' , 'CTM' : "Anu"}, 'ashu': {'GTM': '1098', 'wife': 'aiysha' , 'CTM' : "Ama"}}
    feature_list = ["GTM", "wife", "CTM"]
    feature_format(dict, feature_list)
