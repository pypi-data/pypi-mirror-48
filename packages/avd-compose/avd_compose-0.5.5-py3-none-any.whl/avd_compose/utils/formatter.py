import os
import sys


def options_as_a_string(options, option_prefix="--"):
    string_option_pattern = "{option_name} \"{option_value}\" " if os.name == "nt" else "{option_name} '{option_value}' "
    options_string = ""
    for k, v in options.items():
        option = option_prefix
        if type(v) == str:
            option += string_option_pattern.format(option_name=k, option_value=v)
        elif type(v) == bool and v is True:
            option += "{option_name} ".format(option_name=k)
        else:
            sys.exit("We just support string and bool types for '{}' field".format(k))

        options_string += option

    return options_string
