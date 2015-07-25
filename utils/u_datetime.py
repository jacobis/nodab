from datetime import datetime
from pytz import timezone


def datetime_parser(unicode_datetime, e_format):
    if type(e_format) == list:
        for ef in e_format:
            try:
                result = datetime.strptime(unicode_datetime.encode('utf-8'), ef)
                pass
            except:
                continue
    else:
        result = datetime.strptime(unicode_datetime.encode('utf-8'), e_format)

    return result.replace(tzinfo=timezone('Asia/Seoul'))