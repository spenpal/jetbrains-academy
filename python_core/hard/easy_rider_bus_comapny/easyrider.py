# IMPORTS #
import json
import re

import pandas as pd

# GLOBALS #
FIELD_VALIDATOR = {
    'bus_id': (lambda x: isinstance(x, int)),
    'stop_id': (lambda x: isinstance(x, int)),
    'stop_name': (lambda x: isinstance(x, str)),
    'next_stop': (lambda x: isinstance(x, int)),
    'stop_type': (lambda x: isinstance(x, str) and len(x) == 1),
    'a_time': (lambda x: isinstance(x, str))
}
FORMAT_VALIDATOR = {
    'stop_name': (lambda x: re.match(r'^([A-Z][a-z]+ )+(Road|Avenue|Boulevard|Street)$', x) is not None),
    'stop_type': (lambda x: re.match(r'^[SOF]$', x) is not None),
    'a_time': (lambda x: re.match(r'^[0-2]\d:[0-5]\d$', x) is not None)
}
REQUIRED_ARG = {
    'bus_id': True,
    'stop_id': True,
    'stop_name': True,
    'next_stop': True,
    'stop_type': False,
    'a_time': True
}


# FUNCTIONS #
def validation(database, validator):
    errors = dict.fromkeys(validator.keys(), 0)

    for data in database:
        for field in validator.keys():
            value = data[field]
            if REQUIRED_ARG.get(field) is True:
                errors[field] += (value == "") or (not validator[field](value))
            elif REQUIRED_ARG.get(field) is False:
                errors[field] += (value != "") and (not validator[field](value))

    return errors


def print_validation_errors(errors, val_type):
    if val_type == 'field':
        print('Type and required field validation: ', end='')
    elif val_type == 'format':
        print('Format validation: ', end='')

    print(f'{sum(errors.values())} error{"s" if errors != 1 else ""}')
    for field, error_num in errors.items():
        print(f'{field}: {error_num}')


def print_bus_info(df):
    print('Line names and number of stops:')
    for bus_id, stops in df['bus_id'].value_counts().iteritems():
        print(f'bus_id: {bus_id}, stops: {stops}')


def validate_bus_stop_types(df):
    bus_id_grp = df.groupby('bus_id')

    for bus_id, bus_id_df in bus_id_grp:
        stop_type_counts = bus_id_df['stop_type'].value_counts()
        start_stop_count = stop_type_counts.get('S', 0)
        final_stop_count = stop_type_counts.get('F', 0)

        if not (start_stop_count == 1 == final_stop_count):
            print(f'There is no start or end stop for the line: {bus_id}.')
            return False

    return True


def print_bus_stops(df):
    start_stop_names = df[df['stop_type'] == 'S']['stop_name'].sort_values().unique().tolist()
    stop_name_counts = df['stop_name'].value_counts()
    transfer_stop_names = stop_name_counts[stop_name_counts > 1].index.sort_values().unique().tolist()
    finish_stop_names = df[df['stop_type'] == 'F']['stop_name'].sort_values().unique().tolist()

    print(f'Start stops: {len(start_stop_names)} {start_stop_names}')
    print(f'Transfer stops: {len(transfer_stop_names)} {transfer_stop_names}')
    print(f'Finish stops: {len(finish_stop_names)} {finish_stop_names}')


def validate_arrival_times(df):
    bus_id_grp = df.groupby('bus_id')
    no_errors = True
    print('Arrival time test:')

    for bus_id, bus_id_df in bus_id_grp:
        start_stop = bus_id_df[bus_id_df['stop_type'] == 'S']
        prev_stop_id, prev_a_time, = start_stop['stop_id'].item(), start_stop['a_time'].item()
        curr_stop_id = start_stop['next_stop'].item()

        while curr_stop_id != 0:
            curr_stop = bus_id_df[bus_id_df['stop_id'] == curr_stop_id]
            curr_a_time = curr_stop['a_time'].item()
            if curr_a_time <= prev_a_time:
                print(f'bus_id line {bus_id}: wrong time on station {curr_stop["stop_name"].item()}')
                no_errors = False
                break

            prev_stop_id, prev_a_time = curr_stop['stop_id'].item(), curr_a_time
            curr_stop_id = curr_stop['next_stop'].item()

    if no_errors:
        print('OK')


def validate_on_demand_stops(df):
    stop_name_counts = df['stop_name'].value_counts()
    transfer_stop_names = stop_name_counts[stop_name_counts > 1].index.tolist()
    demand_stops = df[df['stop_type'] == 'O']['stop_name'].tolist()

    wrong_stops = list(sorted(set(transfer_stop_names) & set(demand_stops)))

    print('On demand stops test:')
    print(f'Wrong stop type: {wrong_stops}' if wrong_stops else 'OK')


# MAIN #
database = json.loads(input())
df = pd.json_normalize(database)

validate_on_demand_stops(df)
