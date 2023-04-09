import argparse

parser = argparse.ArgumentParser(description='这是一个示例脚本，用于演示如何添加注释信息。')
parser.add_argument("arg_name", help="help message for arg_name") # 可以直接输入参数，不需要 --arg_name ** 。
parser.add_argument('--input', help='输入文件路径')
args = parser.parse_args()

print(args.arg_name)
print(args.input)