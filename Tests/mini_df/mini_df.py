import logging
import shutil
from pathlib import Path
import pytest
import test_data_for_mini_df as td


def get_parsed_command_as_dict(command):
    command_as_list = command.split()
    parsed_dic = {}
    i = 0
    parsed_dic["base_command"] = command_as_list[i]
    parsed_dic["human_readable"] = False
    i += 1
    try:
        if command_as_list[i] == "-h":
            parsed_dic["human_readable"] = True
            i += 1

        try:
            parsed_dic["dir_path"] = command_as_list[i]
        except IndexError:
            pass

    except IndexError:
        pass

    return parsed_dic


def get_output(parsed_dic):
    if parsed_dic.get("dir_path"):
        total, used, free = shutil.disk_usage(parsed_dic.get("dir_path"))
        if parsed_dic["human_readable"]:
            total, used, free = total // (2 ** 30), used // (2 ** 30), free // (2 ** 30)
        return [total, used, free]
    else:
        root_directory = Path("../../")
        res = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
        if parsed_dic["human_readable"]:
            res = res / 1024
        return res


class TestMiniDf:
    logger = logging.getLogger()

    @pytest.mark.parametrize("test_case", [td.test_case_1, td.test_case_2, td.test_case_3, td.test_case_4, td.test_case_5])
    def test1(self, test_case):
        actual_result = get_output(get_parsed_command_as_dict(test_case["input_data"]))
        expected_result = test_case['expected_result']
        self.logger.info(f"{actual_result=}\n   {expected_result=}")
        assert actual_result == test_case["expected_result"]
