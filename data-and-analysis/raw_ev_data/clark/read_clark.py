# read_clark.py

import pandas as pd
import os

def read_clark(): 

    clark_ev_files = [
        'EV20161022'
        , 'EV20161023'
        , 'EV20161024'
        , 'EV20161025'
        , 'EV20161026'
        , 'EV20161027'
        , 'EV20161028'
        , 'EV20161029'
        , 'EV20161030'
        , 'EV20161031'
        , 'EV20161101'
        , 'EV20161102'
        , 'EV20161103'
        , 'EV20161104'
    ]

    clark_header = [x.lower() for x in [
        'IDNUMBER'
        , 'NAME'
        , 'PRECINCT'
        , 'PARTY'
        , 'PARTY_ABBR'
        , 'CONGRESS'
        , 'ASSEMBLY'
        , 'SENATE'
        , 'COMMISSION'
        , 'EDUCATION'
        , 'REGENT'
        , 'SCHOOL'
        , 'CITY'
        , 'WARD'
        , 'TOWNSHIP'
        , 'STATUS'
        , 'EV_SITE'
        , 'ELECTION_CODE'
        , 'ACTIVITY_DATE'
        ]]

    dfs = {}

    for i, f in enumerate(clark_ev_files): 
        file_to_read = 'raw_ev_data/clark/' + f + '.txt'

        if os.path.isfile(file_to_read): 
            dfs[f] = pd.read_csv(file_to_read, header=None, names=clark_header)
            dfs[f]['ev_day_number'] = i+1
            print 'Clark file read: {}, voters = {:,}'.format(f, len(dfs[f]))
        else: 
            print 'Clark file does not yet exist: ' + f
            break

    ev = pd.concat(dfs)
    ev['soscountyid'] = ev['idnumber']
    ev['county_name'] = 'Clark'

    return ev[['county_name', 'soscountyid', 'ev_day_number']]