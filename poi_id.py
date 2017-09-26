#!/usr/bin/python

import sys
import pickle
#sys.path.append("../tools/")
sys.path.append("./tools/") # use local folder due to github repo

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from auxiliary_functions  import *

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

features_list = ['poi', 'exercised_stock_options', 'bonus', 'expenses', 'other',
                 'share_shared_receipt_with_poi', 'share_from_this_person_to_poi']#


### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop('TOTAL',0)
data_dict.pop('THE TRAVEL AGENCY IN THE PARK',0)
data_dict.pop('LOCKHART EUGENE E',0)
fix_shifted_persons(data_dict)

### Task 3: Create new feature(s)
data_dict = convert_to_share(data_dict, 'shared_receipt_with_poi', 'to_messages', 'share_shared_receipt_with_poi')
data_dict = convert_to_share(data_dict, 'from_this_person_to_poi', 'from_messages', 'share_from_this_person_to_poi')
data_dict = convert_to_share(data_dict, 'from_poi_to_this_person', 'to_messages', 'share_from_poi_to_this_person')

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Task 5: Tune your classifier to achieve better than .3 precision and recall 
## See Project notes for testing, comparisons and tuning
## this is the best option:

from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(learning_rate = 2, n_estimators = 13)


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)