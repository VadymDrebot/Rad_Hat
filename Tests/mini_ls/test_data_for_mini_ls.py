test_case_1 = {"input_data": "./mini-ls  owners.json",
               "expected_result": {'Kate': {'Permission': 'False', 'Modified Time': '11/23/2022'},
                                   'Vadym': {'Permission': 'True', 'Modified Time': '10/25/2022'}}}
test_case_2 = {"input_data": "./mini-ls -r owners.json",
               "expected_result": {'Vadym': {'Permission': 'True', 'Modified Time': '10/25/2022'},
                                   'Kate': {'Permission': 'False', 'Modified Time': '11/23/2022'}}}
test_case_3 = {"input_data": "./mini-ls ",
               "expected_result": ['mini_ls.py', 'owners.json', 'test_data_for_mini_ls.py']}

test_case_4 = {"input_data": "./mini-ls -r",
               "expected_result": ['test_data_for_mini_ls.py', 'owners.json', 'mini_ls.py']}
