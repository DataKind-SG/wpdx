
# coding: utf-8

# In[7]:


import pandas as pd

# UDF will skim through category lists of words that belong to either Partially Functional, Functional, Not Functional.
# UDF goes through sequentially via list_partlydamaged, list_functional1, list_notfunctional, list_functional2
# List of words were obtained by testing samples after filtering from top 10 countries that provided cumulative 85% of data.

# list of functional or not functional or unknown
list_partlydamaged = (
"partly damaged",
"yes but",
"yes- but",
"yes - but",
"partially functional")

list_functional1 = (
    "not developed mechanical problems",
    "not breakdown",
    ":functional", 
    "yes – functional", 
    "no damages", 
    "no damage")

list_notfunctional = (
'not function',
'poor',
'dry',
'problem',
'not delivering',
'problem',
'plugged',
'abandoned',
'non-operational',
'partially functional',
'non-functional',
'broken',
'with problems',
'spoiled',
'damaged ',
'damage',
'not giving',
'defective',
'not well dug',
'malfunction',
'stolen',
'fault',
'spoilt',
'spoiled',
'spoid',
'spioled',
'rusting',
'weak',
'limited',
'breaking',
'not completed',
'not working',
'stolen',
'not commissioned',
'undeveloped',
'incomplete',
'lack of',
'non- functional',
'in bad shape',
'technical breakdown',
'faulty',
'in bad state',
'no operation',
'dried',
'no water',
'fallen',
'chocked',
'choked',
'no funds',
'lack of funds',
'no hundle',
'not cpmplete',
'stop flowing',
'breakdown',
'broking',
'not complete',
'serious',
'no head',
'contaminated',
'yet to be completed',
'broken down',
'leakage',
'disconnected',
'stopped',
'does not flow',
'long time',
'not well function',
'disconnection',
'no money',
'dirty',
'brakage',
'worn out',
'brokedown',
'water stops',
'no connection',
'removed',
'sunk',
'did not work',
'too oldbreackdown',
'collapse',
'break',
'stolen',
'not installed',
'under construction',
'dried',
'dysfunction',
'desamorsage')

list_functional2 = (
"functional",
"fair",
"good",
"ok",
"operational",
"working",
"satisfaisant"
)

# UDF has several nested for loops, which will break upon first occurence of words from categorised list (partially functional, functional, not functional)
# This is to reduce processing time.

def udf_status(x):
    answer = "Unknown"
    for h in list_partlydamaged:
        if h in x:
            answer = "Partially Functional with Damages"
            break
        else:
            # if we reach end of primary partlydamaged list
            if h == list_partlydamaged[-1]:

                # Start with primary functional list
                for i in list_functional1:
                    if i in x:
                        answer = "Functional"
                        break
                    else:
                        # if we reach end of primary functional list
                        if i == list_functional1[-1]:

                            # Start with primary non functional list
                            for j in list_notfunctional:
                                if j in x:
                                    answer = "Non Functional"
                                    break
                                else:
                                    # if we reach end of non functional list
                                    if j == list_notfunctional[-1]:

                                        # Start with secondary functional list
                                        for k in list_functional2:
                                            if k in x:
                                                answer = "Functional"
                                                break
                                        else:
                                            break

    return(answer)

def clean_STATUS(input_name, output_name):
    
    # For SAMPLE data which has 1 empty row
    dat = pd.read_csv(input_name, skiprows=1)
    # For COMPLETE data
    # dat = pd.read_csv(input_name)
    
    # Preprocessing clean up
    # Remove all NaNs by converting into string text "Not Available"
    ## For SAMPLE DATA
    dat['status'] = dat['status'].apply(lambda x: "Not Available" if isinstance(x, float) else x)
    ## For COMPLETE DATA with "#" in its columns
    # dat['#status'] = dat['#status'].apply(lambda x: "Not Available" if isinstance(x, float) else x)

    # Convert to lower character
    ## For SAMPLE DATA
    dat['status'] = dat['status'].apply(lambda x: x.lower())
    ## For COMPLETE DATA with "#" in its columns
    # dat['#status'] = dat['#status'].apply(lambda x: x.lower())
    
    # Apply UDF
    ## For SAMPLE DATA
    dat['status'] = dat['status'].apply(lambda x: udf_status(x))
    ## For COMPLETE DATA with "#" in its columns
    # dat['#status'] = dat['#status'].apply(lambda x: udf_status(x))
    
    dat.to_csv(output_name)

if __name__ == '__main__':
    ## For SAMPLE DATA
    clean_STATUS('wpdx_sample_data.csv', 'cleaned_wpdx_sample_data_STATUS.csv')
    ## For COMPLETE DATA
    # clean_STATUS('Water_Point_Data_Exchange_Complete_Dataset.csv', 'cleaned_wpdx_COMPLETE_data_STATUS.csv')

