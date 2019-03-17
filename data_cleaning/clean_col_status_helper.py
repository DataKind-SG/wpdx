"""
UDF will skim through category lists of words that belong to either Partially Functional, Functional, Not Functional.
UDF goes through sequentially via list_partlydamaged, list_functional1, list_notfunctional, list_functional2
List of words were obtained by testing samples after filtering from top 10 countries that provided cumulative 85% of
data.

UDF has several nested for loops, which will break upon first occurrence of words from categorised list (partially
functional, functional, not functional)
This is to reduce processing time.
"""

def categorise_status(x):

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
                                    answer = "Not Functional"
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

    return answer
