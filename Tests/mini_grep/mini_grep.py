import logging
import re
import pytest
import test_data_for_mini_grep as td


def get_parsed_command_as_dict(command, test_case):
    command_as_list = command.split()
    parsed_dic = {}
    i = 0
    parsed_dic["base_command"] = command_as_list[i]
    i += 1
    if command_as_list[i] == "-q":
        parsed_dic["numbers"] = True
        i += 2
    else:
        i += 1
    parsed_dic["pattern"] = command_as_list[i]

    try:
        parsed_dic["file"] = command_as_list[i + 1]
    except IndexError:
        parsed_dic["standart_input"] = test_case["standart_input"]
    return parsed_dic


def output_list_of_lines(parsed_dic):
    if parsed_dic.get("file"):
        with open(parsed_dic["file"], "r") as f:
            lines = [line.rstrip() for line in f.readlines()]
    else:
        lines = [parsed_dic["standart_input"]]

    lst = [[number, line] for number, line in enumerate(lines, start=1) if re.match(parsed_dic["pattern"], line)] \
        if parsed_dic.get("numbers") else [[line] for line in lines if re.match(parsed_dic["pattern"], line)]

    return lst


class TestMiniGrep:
    logger = logging.getLogger()

    @pytest.mark.parametrize("test_case", [td.test_case_1, td.test_case_2, td.test_case_3, td.test_case_4, td.test_case_5])
    def test1(self, test_case):
        actual_result = output_list_of_lines(get_parsed_command_as_dict(test_case["command"], test_case))
        expected_result = test_case['expected_result']
        self.logger.info(f"{actual_result=}\n   {expected_result=}")
        assert actual_result == test_case["expected_result"]
