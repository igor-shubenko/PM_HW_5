import json
from datetime import datetime as dt
from collections import Counter
import os


def read_jsonl(file_path: str = 'data.jsonl') -> tuple:
    """Reads user data from jsonl-file.
        Converts 'time_created' field to datetime type.
        Add user data to tuple"""
    readed_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                data = json.loads(line)
                data['time_created'] = dt.fromtimestamp(data['time_created'])
                readed_data.append(data)
    except FileNotFoundError:
        print("Wrong filename or file not exists\n")
        main()
    except Exception as e:
        print("Exception: ", e, '\n')

    print(f"Readed {len(readed_data)} records")

    return tuple(readed_data)


def duplicate_remove(data: tuple) -> tuple:
    """Function reads records from tuple and
        return another tuple without duplicates."""
    temp = {}
    for record in data:
        key = (record['name'], record['time_created'])
        if key not in temp:
            temp[key] = record

    print(f"Removed {len(data) - len(temp)} duplicates")

    return tuple([v for v in temp.values()])


def get_fields_list(data: tuple) -> dict:
    """Returns full amount of fields"""
    fields = {}
    for record in data:
        for key in record.keys():
            if key not in fields.keys():
                fields[key] = {}


    print("All fields are: ", end='\n\t')
    print(*fields, sep=', ')

    return fields


def get_fields_type(fields: set, data: tuple) -> dict:
    """Add type of field data to fields information dict"""
    empty_fields = {}
    for key in fields:
        for record in data:
            if record.get(key, None):
                empty_fields[key] = {}
                empty_fields[key]['data_type'] = type(record[key])
                break

    return empty_fields


def get_str_default(data: list) -> str:
    b = Counter(data)
    return max(b, key=b.get)


def get_int_default(data: list) -> int:
    return sum(data) // len(data)


def get_float_default(data: list) -> float:
    return sum(data) / len(data)


def get_field_default_value(fields: dict, data: tuple) -> dict:
    """Add default values to empty_fields information dict"""
    for key in fields:
        if fields[key]['data_type'] is str:
            fields[key]['default_value'] = get_str_default([v[key] for v in data if v.get(key)])
        elif fields[key]['data_type'] is int:
            fields[key]['default_value'] = get_int_default([v[key] for v in data if v.get(key)])
        elif fields[key]['data_type'] is float:
            fields[key]['default_value'] = get_float_default([v[key] for v in data if v.get(key)])
        else:
            fields[key]['default_value'] = None

    print("Empty fields info:")
    for key in fields:
        print(f"\t- Fieldname: {key} -> Field data type: {fields[key]['data_type']} -> "
              f"Default value: {fields[key]['default_value']}")

    return fields


def get_empty_fields(fields: dict, data: tuple) -> set:
    """Get set of empty fields."""
    empty_fields = set()
    for record in data:
        record_fields = [v for v in record if record[v] is not None]
        empty_fields.update(set(fields) - set(record_fields))

    if not empty_fields:
        print("No empty fields found")

    return empty_fields


def fill_existing_fields(data: tuple, fields: dict) -> dict:
    """Inserts default values to empty fields in each record.
        converts datetime to timestamp. Adding records to dict values
        with key by date created."""
    full_data = {}
    for record in data:
        temp_record = {}
        for key in fields:
            if key not in record.keys() or record[key] is None:
                temp_record[key] = fields[key]['default_value']
            elif key == 'time_created':
                date_created = record['time_created'].strftime('%Y-%m-%d')
                temp_record['time_created'] = int(dt.timestamp(record['time_created']))
            else:
                temp_record[key] = record[key]

        if date_created not in full_data:
            full_data[date_created] = [temp_record]
        else:
            full_data[date_created].append(temp_record)

    return full_data


def write_data(data: dict) -> None:
    """Creates folder for user_data files if not exists.
        Writes user data into .jsonl files.
        File names are dates of creation records in it."""
    try:
        os.mkdir('users_data')
    except FileExistsError:
        pass

    counter = 0

    for date_created in data:
        # with open('users_data/' + date_created + '.jsonl', 'w', encoding='utf-8') as f:
        with open ('processed_data.jsonl', 'a', encoding='utf-8') as f:
            for record in data[date_created]:
                f.write(json.dumps(record) + '\n')
                counter += 1

    print(f"\nUser data processing successful!. {counter} records made.")


def main():
    """Calls other functions in order"""
    hello = input("If filename is 'data.jsonl' and it in same directory with this module - press Enter\n"
                  "Else write path to file and press Enter. Enter 'q' to exit program:\n")

    if hello == 'q':
        print('Bye')
        return

    raw_data = read_jsonl(hello) if hello else read_jsonl()

    if not raw_data:
        print("File is empty, nothing to process!")
        return

    unique_data = duplicate_remove(raw_data)
    all_fields = get_fields_list(unique_data)
    empty_fields_data = get_empty_fields(all_fields, unique_data)

    if empty_fields_data:
        empty_fields_data = get_fields_type(empty_fields_data, unique_data)
        empty_fields_data = get_field_default_value(empty_fields_data, unique_data)
        for key in empty_fields_data:
            all_fields[key].update(empty_fields_data[key])

    unique_data_full = fill_existing_fields(unique_data, all_fields)
    write_data(unique_data_full)


if __name__ == '__main__':
    main()
