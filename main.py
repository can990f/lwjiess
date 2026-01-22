#!/usr/bin/env python3
"""
简单的待办事项管理应用
"""

import json
import os
from datetime import datetime


class TodoApp:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        """从文件加载待办事项"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_todos(self):
        """保存待办事项到文件"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)

    def add_todo(self, task):
        """添加新的待办事项"""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ 已添加: {task}")

    def list_todos(self):
        """列出所有待办事项"""
        if not self.todos:
            print("暂无待办事项")
            return
        
        print("\n待办事项列表:")
        print("-" * 60)
        for todo in self.todos:
            status = "✓" if todo['completed'] else "○"
            print(f"{status} [{todo['id']}] {todo['task']}")
            print(f"   创建时间: {todo['created_at']}")
        print("-" * 60)

    def complete_todo(self, todo_id):
        """标记待办事项为完成"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✓ 已完成: {todo['task']}")
                return
        print(f"未找到ID为 {todo_id} 的待办事项")

    def delete_todo(self, todo_id):
        """删除待办事项"""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                deleted = self.todos.pop(i)
                self.save_todos()
                print(f"✓ 已删除: {deleted['task']}")
                return
        print(f"未找到ID为 {todo_id} 的待办事项")


def show_menu():
    """显示菜单"""
    print("\n=== 待办事项管理系统 ===")
    print("1. 查看所有待办")
    print("2. 添加待办")
    print("3. 完成待办")
    print("4. 删除待办")
    print("5. 退出")
    print("=" * 25)


def main():
    """主函数"""
    app = TodoApp()
    
    while True:
        show_menu()
        choice = input("\n请选择操作 (1-5): ").strip()
        
        if choice == '1':
            app.list_todos()
        elif choice == '2':
            task = input("请输入待办事项: ").strip()
            if task:
                app.add_todo(task)
            else:
                print("待办事项不能为空")
        elif choice == '3':
            try:
                todo_id = int(input("请输入要完成的待办ID: "))
                app.complete_todo(todo_id)
            except ValueError:
                print("请输入有效的数字")
        elif choice == '4':
            try:
                todo_id = int(input("请输入要删除的待办ID: "))
                app.delete_todo(todo_id)
            except ValueError:
                print("请输入有效的数字")
        elif choice == '5':
            print("再见!")
            break
        else:
            print("无效的选择，请重试")


if __name__ == '__main__':
    main()
