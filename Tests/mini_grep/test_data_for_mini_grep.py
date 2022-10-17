test_case_1 = {"command": "./mini-grep -q  -e \w*a text_file.txt", "expected_result": [[1, "aaa sss"]]}

test_case_2 = {"command": "./mini-grep -q  -e \w*c ", "standart_input": "ccc", "expected_result": [[1, "ccc"]]}

test_case_3 = {"command": "./mini-grep -q  -e \w*c text_file.txt", "expected_result": [[3, "ccc hhh"], [4, "ssc lll"]]}

test_case_4 = {"command": "./mini-grep   -e \w*c text_file.txt", "expected_result": [["ccc hhh"], ["ssc lll"]]}

test_case_5 = {"command": "./mini-grep   -e \w*c empty_file.txt", "expected_result": []}