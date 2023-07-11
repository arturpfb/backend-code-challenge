import re


class Formatter(object):
    @staticmethod
    def format_cursor(cursor, camel_case) -> list:
        resp_list = []
        names_list = []

        if camel_case:
            names_list = [
                Formatter.camel_case_name(value.name)
                for value in cursor.description
            ]
        else:
            names_list = [value.name for value in cursor.description]

        for row in cursor:
            resp_list.append(dict(zip(names_list, row)))

        return Formatter.clear_nulls(resp_list)

    @staticmethod
    def camel_case_name(name) -> str:
        return re.sub("_.", lambda x: x.group()[1].upper(), name)

    @staticmethod
    def clear_nulls(dict_list) -> list:
        for obj in dict_list:
            for k, v in obj.items():
                if isinstance(v, str) and v.lower() == "null":
                    obj[k] = None

        return dict_list
