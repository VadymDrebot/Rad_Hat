import json
import logging
import os
import test_data_for_mini_ls as td

import pytest


def get_parsed_command_as_dict(command):
    command_as_list = command.split()
    parsed_dic = {}
    i = 0
    parsed_dic["base_command"] = command_as_list[i]
    parsed_dic["reverse_flag"] = False
    i += 1
    try:
        if command_as_list[i] == "-r":
            parsed_dic["reverse_flag"] = True
            i += 1

        try:
            parsed_dic["file_name"] = command_as_list[i]
        except IndexError:
            pass

    except IndexError:
        pass

    return parsed_dic


def get_output(parsed_dic):
    if parsed_dic.get("file_name"):
        with open(parsed_dic["file_name"], "r") as f:
            json_data = json.load(f)
        return dict(sorted(json_data.items(), reverse=parsed_dic["reverse_flag"]))

    else:
        return sorted(os.listdir(), reverse=parsed_dic["reverse_flag"])


class TestMiniLs:
    logger = logging.getLogger()

    @pytest.mark.parametrize("test_case", [td.test_case_1, td.test_case_2, td.test_case_3, td.test_case_4])
    def test1(self, test_case):
        actual_result = get_output(get_parsed_command_as_dict(test_case["input_data"]))
        expected_result = test_case['expected_result']
        self.logger.info(f"{actual_result=}\n   {expected_result=}")
        assert actual_result == test_case["expected_result"]
