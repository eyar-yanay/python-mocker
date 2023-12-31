import os
from dotenv import load_dotenv

load_dotenv()

MODE_ENV = os.getenv("MODE_ENV")


class Mock:
    def mock(self, req_class):
        def dec(func: classmethod):
            def wrapper(*args, **kwargs):
                print(func.__name__)
                if (MODE_ENV == "stage"):
                    return self.handle_request(req_class)
                else:
                    return func()

            return wrapper

        return dec

    def mimic_res(self, attr: dict):
        for key, value in attr.items():
            type_str = str(type(value))
            if 'str' in type_str:
                attr[key] = 'random string'
            if 'bool' in type_str:
                attr[key] = False
            if 'float' in type_str:
                attr[key] = 0.66
            if 'dict' in type_str:
                print('found dict: ', value)
                self.mimic_res(value)
        return attr

    def handle_request(self, req_class):
        print("handling request... -> request class: ", req_class)
        req_instance = req_class()
        fake_res = self.mimic_res(vars(req_instance))
        return fake_res
