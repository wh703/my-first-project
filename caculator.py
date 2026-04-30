# 简易Python计算器
def calculator():
    print("===== Python 计算器 =====")
    print("支持：+ - * / () 小数点")
    print("输入 'quit' 退出\n")

    while True:
        # 获取用户输入
        expression = input("请输入计算式：")

        # 退出条件
        if expression.lower() == "quit":
            print("退出计算器～")
            break

        try:
            # 计算结果
            result = eval(expression)
            print(f"结果：{result}\n")

        except ZeroDivisionError:
            print("错误：不能除以0！\n")
        except SyntaxError:
            print("错误：输入格式不正确！\n")
        except:
            print("错误：无法计算，请检查输入！\n")

# 运行计算器
if __name__ == "__main__":
    calculator()