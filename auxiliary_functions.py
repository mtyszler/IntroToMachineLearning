""" This file contains auxiliary functions to be used by poi_id.py
    Created by Marcelo Tyszler
"""

def convert_to_share(data, abs_var_name, base_var_name, new_var_name):
    """ This function converts an absolute variable as share of a reference value

        It takes a dictionary as input and returns the same dictionary with the
        new variable added.

        If either the base or reference or the absolute variable are NaN, a NaN is returned
        Otherwise, it computes new_variable = absolute_variable/base_variable
    """

    # loop for all entries
    for person in data.keys():

        # check for valid values
        if data[person][abs_var_name] == "NaN" or data[person][base_var_name] == "NaN":
            data[person][new_var_name] = "NaN"
        else:
            # compute new variable
            data[person][new_var_name] = float(data[person][abs_var_name]) / float(data[person][base_var_name])

    return data

def fix_shifted_persons(data):
    """ This function is an ad-hoc fix applied to the Enron dataset
        Two persons have a problem with a data shift in columns

        This function overwrites the dictionary, correcting these entries

        It takes a dictionary as input and returns the same dictionary with the
        entries corrected
    """

    data['BHATNAGAR SANJAY'] = {'bonus': 'NaN',
                              'deferral_payments': 'NaN',
                              'deferred_income': 'NaN',
                              'director_fees': 'NaN',
                              'email_address': 'sanjay.bhatnagar@enron.com',
                              'exercised_stock_options': 15456290,
                              'expenses': 137864,
                              'from_messages': 29,
                              'from_poi_to_this_person': 0,
                              'from_this_person_to_poi': 1,
                              'loan_advances': 'NaN',
                              'long_term_incentive': 'NaN',
                              'other': 'NaN',
                              'poi': False,
                              'restricted_stock': 2604490,
                              'restricted_stock_deferred': -2604490,
                              'salary': 'NaN',
                              'shared_receipt_with_poi': 463,
                              'to_messages': 523,
                              'total_payments': 137864,
                              'total_stock_value': 15456290}

    data['BELFER ROBERT'] ={'bonus': 'NaN',
                             'deferral_payments': 'NaN',
                             'deferred_income': -102500,
                             'director_fees': 102500 ,
                             'email_address': 'NaN',
                             'exercised_stock_options': 'NaN' ,
                             'expenses': 3285,
                             'from_messages': 'NaN',
                             'from_poi_to_this_person': 'NaN',
                             'from_this_person_to_poi': 'NaN',
                             'loan_advances': 'NaN',
                             'long_term_incentive': 'NaN',
                             'other': 'NaN',
                             'poi': False,
                             'restricted_stock': 44093,
                             'restricted_stock_deferred': -44093,
                             'salary': 'NaN',
                             'shared_receipt_with_poi': 'NaN',
                             'to_messages': 'NaN',
                             'total_payments': 3285,
                             'total_stock_value': 'NaN'}

    return data