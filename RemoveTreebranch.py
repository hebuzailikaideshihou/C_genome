#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse
from ete3 import Tree

# 创建解析器
parser = argparse.ArgumentParser(description="Remove branch lengths from a Newick tree.")

# 添加输入文件参数
parser.add_argument("--input", "-i", required=True, help="Input tree file in Newick format")

# 添加输出文件参数
parser.add_argument("--output", "-o", required=True, help="Output tree file without branch lengths")

# 解析命令行参数
args = parser.parse_args()

# 从输入文件中读取Newick格式的树
with open(args.input, 'r') as f:
    tree_str = f.read()

# 将树解析为ete3对象
t = Tree(tree_str)

# 去掉树中的分支长度
for node in t.traverse():
    node.dist = 0

# 将结果写入输出文件
with open(args.output, 'w') as f:
    f.write(t.write())

print("分支长度已经去掉，并已写入文件:", args.output)
