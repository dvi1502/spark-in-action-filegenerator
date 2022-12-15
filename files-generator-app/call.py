from datetime import datetime
from random import randrange
from random import randint
import json

# ----------------------------------------------------------
# How to overcome "datetime.datetime not JSON serializable"?
# ----------------------------------------------------------
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)
# ----------------------------------------------------------

# case-class описывающий входящий вызов
class PhoneCall:

    def __init__(self, call_time=None, duration=0, call_phone="", caller=""):
        self.call_time = call_time
        self.duration = duration
        self.call_phone = call_phone
        self.caller = caller

    def json(self):
        return json.dumps(vars(self), cls=DateTimeEncoder)

# Генератор звонков, поступающих от вымышленных абонентов
def PhoneCallBuilder(args):

    # x=1000000
    # while( x > 0):
    while True:
        duration = randint(1,3600)
        call_phone = get_phone_number()
        caller = next(get_name_caller(args))
        yield PhoneCall (
                datetime.now(),
                duration,
                call_phone,
                caller
            )
        # x-=1

def get_phone_number():
    ph_no = []

    # the first number should be in the range of 6 to 9
    ph_no.append(randint(6, 9))

    # the for loop is used to append the other 9 numbers.
    # the other 9 numbers can be in the range of 0 to 9.
    for i in range(1, 10):
        ph_no.append(randint(0, 9))

    return "".join(str(x) for x in ph_no );


#TODO: доделать функцию чтоб было случайное чтение из female_first_names.txt

def get_name_caller(args=None):

    if args is None:
        resource_path = "resources"
    else:
        resource_path = args.resource

    with open("{0}/female_first_names.txt".format(resource_path), "r") as f :
        first_name = f.read().splitlines()

    with open("{0}/last_names.txt".format(resource_path), "r") as f :
        last_name = f.read().splitlines()

    while True:
        first_name_index = randint(0, len(first_name)-1)
        last_name_index = randint(0, len(last_name)-1)
        yield "{0} {1}".format(
            str(first_name[first_name_index]),
            str(last_name[last_name_index])
        )



if __name__ == "__main__":
    for i in range(5):
        print(get_phone_number())

    for i in range(5):
        print(next(get_name_caller(None)))

    for i in range(8):
        call = next(PhoneCallBuilder(None))
        print(call.json())
