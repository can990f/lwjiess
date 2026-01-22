"""
工具函数模块
"""


def format_date(date_string):
    """格式化日期字符串"""
    from datetime import datetime
    try:
        dt = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%Y年%m月%d日 %H:%M')
    except ValueError:
        return date_string


def validate_input(prompt, input_type=str):
    """验证用户输入"""
    while True:
        try:
            user_input = input(prompt).strip()
            if input_type == int:
                return int(user_input)
            elif input_type == str:
                if user_input:
                    return user_input
                else:
                    print("输入不能为空，请重试")
            else:
                return input_type(user_input)
        except ValueError:
            print(f"无效的输入，请输入{input_type.__name__}类型")
        except KeyboardInterrupt:
            print("\n操作已取消")
            return None
