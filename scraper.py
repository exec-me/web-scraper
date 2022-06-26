import requests


def get_structure(url):
    res = requests.get(url)
    response_text = res.text
    result = dict()
    if res.status_code == 200:
        body_start_index = response_text.find('<body>')
        body_end_index = response_text.find(r'</body>')
        response_text = response_text[body_start_index:body_end_index + 1]

        # TODO indexes and results
        time_index_start = response_text.find('title="Time"')
        time_index_offset = response_text[time_index_start:].find(r'</span>')

        time_str_list = response_text[time_index_start:time_index_start + time_index_offset].split()
        result['time'] = ''.join(time_str_list[time_str_list.index(r'data-container="body">') + 1:])

        subject_index_start = response_text.find('title="Subject"')
        subject_index_offset = response_text[subject_index_start:].find(r'</span>')

        subject_str_list = response_text[subject_index_start:subject_index_start + subject_index_offset].split()

        result['subject'] = ' '.join(subject_str_list[subject_str_list.index(r'data-container="body">') + 1:])

        return result

    else:
        print("sorry, couldn't connect to url")

