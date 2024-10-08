import re

report = """
**用例执行详情**
<font color=black>1_添加道具：</font> <font color='red'>FAILURE</font>
-判断是否在1_添加道具：<font color="warning">FAIL, 在时间内定位页面未出现，可能卡死或者其他异常情况导致 </font>
<font color=black>2_打开背包：</font><font color="green">SUCCESS</font>
-判断是否在2_打开背包：<font color="warning">FAIL, 在时间内定位页面未出现，可能卡死或者其他异常情况导致 </font>
<font color=black>3_切换背包页签：</font><font color="green">SUCCESS</font>
<font color=black>4_切换背包页签：</font><font color="green">SUCCESS</font>
<font color=black>5_选择道具：</font><font color="green">SUCCESS</font>
<font color=black>6_丢弃道具：</font><font color="green">SUCCESS</font>
<font color=black>7_关闭背包：</font><font color="green">SUCCESS</font>
<font color=black>8_打开背包：</font><font color="green">SUCCESS</font>
<font color=black>9_选择道具：</font><font color="green">SUCCESS</font>
<font color=black>10_拆分道具：</font><font color="green">SUCCESS</font>
<font color=black>11_选择道具：</font><font color="green">SUCCESS</font>
<font color=black>12_销毁道具：</font><font color="green">SUCCESS</font>
<font color=black>13_整理背包：</font><font color="green">SUCCESS</font>
<font color=black>14_关闭背包：</font><font color="green">SUCCESS</font>
<font color=black>背包模块：</font><font color="green">SUCCESS</font>"""


def parse_game_rt(data):
    results = {}
    # 提取用例执行详情
    case_details = re.findall(r"<font color=black>(.*?)：</font>\s*<font color='(.*?)'>(.*?)</font>", data)
    details = []

    # Create a dictionary to hold case names and their results
    case_dict = {case[0].strip(): {'statuscolor': case[1].strip(), 'result': case[2].strip(), 'description': ''} for
                 case in case_details}

    # Extract descriptions
    description_pattern = r"-判断是否在(.*?):<font color=\"warning\">(.*?)</font>"
    descriptions = re.findall(description_pattern, data)

    for case_name, description in descriptions:
        case_name = case_name.strip()
        description = description.strip()
        if case_name in case_dict:
            case_dict[case_name]['description'] = description

    # Convert the dictionary back to a list for the final output
    for case_name, info in case_dict.items():
        print(case_name)
        details.append({
            'case_name': case_name,
            'statuscolor': info['statuscolor'],
            'result': info['result'],
            'description': info['description']
        })

    results['case_details'] = details

    return results


if __name__ == "__main__":
    parsed_results = parse_game_rt(report)
    print(parsed_results)