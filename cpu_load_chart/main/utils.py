from django.db.models import QuerySet



def get_avg_load(data_list):
    sum = 0
    for i in data_list:
        sum += i
    avg_load = sum / 12
    return round(avg_load, 2)



def prepare_data_for_template(data_from_db: QuerySet):
    load_list = list()
    added_at_list = list()
    for data in data_from_db:
        load_list.append(data['load'])
        added_at_list.append(data['added_at'])

   
    intermediate_list = list()
    avg_load_list = list()
    counter = 0
    for i in range(len(load_list)):
        intermediate_list.append(load_list[i])
        counter += 1
        if counter == 12:
            avg_load_list.append(get_avg_load(intermediate_list))
            intermediate_list.clear()
            counter = 0

    data_for_template = dict()
    data_for_template['cpu_load'] = load_list
    data_for_template['added_at'] = added_at_list
    data_for_template['avg_cpu_load'] = avg_load_list

    return data_for_template
