# Python 待办事项管理系统

一个简单的命令行待办事项管理应用，使用Python编写。

## 功能特性

- ✅ 添加待办事项
- ✅ 查看所有待办事项
- ✅ 标记待办事项为完成
- ✅ 删除待办事项
- ✅ 数据持久化存储（JSON格式）

## 项目结构

```
lwjiess/
├── main.py              # 主程序文件
├── utils.py             # 工具函数模块
├── requirements.txt     # 项目依赖
├── .gitignore          # Git忽略文件
└── README.md           # 项目说明
```

## 快速开始

### 环境要求

- Python 3.6 或更高版本

### 安装步骤

1. 克隆或下载本项目

2. （可选）创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

### 运行程序

```bash
python main.py
```

## 使用说明

运行程序后，您将看到一个交互式菜单：

```
=== 待办事项管理系统 ===
1. 查看所有待办
2. 添加待办
3. 完成待办
4. 删除待办
5. 退出
=========================
```

按照提示输入数字选择相应功能即可。

## 数据存储

所有待办事项都保存在 `todos.json` 文件中，程序会自动创建和更新此文件。

## 开发说明

- `main.py`: 包含主要的业务逻辑和TodoApp类
- `utils.py`: 包含辅助工具函数

## 许可证

MIT License