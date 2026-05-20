import os
import csv

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grades):
        self.grades.append(grades)

class StudentsManager:
    def __init__(self):
        self.students = {}

    def add_students(self,name):
        if name not in self.students:
            self.students[name] = Student(name)
        else:
            print("学生已经存在")

    def add_grade_to_student(self,name,grade):
        student = self.students.get(name)
        if student is None:
            print("该学生不存在")
            return
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                student.add_grades(grade)
            else:
                print("成绩必须在0-100之间！")
        except ValueError:
            print(f"错误：{grade}输入不是有效成绩，请输入数字！")

    def save_to_file(self,filename="students.csv"):
        with open(filename, "w", newline='',encoding="utf-8") as f:
            writer = csv.writer(f)
            for name, student in self.students.items():
                grades_str = ",".join(str(g) for g in student.grades)
                writer.writerow([name, grades_str])

    def load_from_file(self, filename="students.csv"):
        if not os.path.exists(filename):
            return
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                self.students[name] = Student(name)
                if row[1]:
                    for g in row[1].split(","):
                        self.students[name].grades.append(float(g))


    def remove_student(self,name):
        student = self.students.get(name)
        if student is not None:
            del self.students[name]
            print(f"已删除学生：{name}")
        else:
            print("该学生不存在")

    def show_students(self):
        for name, student in self.students.items():
            print(f"学生:{name}的成绩是： {student.grades}")

def main():
    manager = StudentsManager()
    manager.load_from_file()
    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 添加学生")
        print("2. 添加学生成绩")
        print("3. 删除学生")
        print("4. 查看所有学生成绩")
        print("5. 退出系统")
        choice = input("请输入你的选择(1-5):")
        if choice == "1":
            name = input("请输入学生姓名:")
            manager.add_students(name)

        elif choice == "2":
            name = input("请输入想要添加成绩的学生姓名:")
            if manager.students.get(name) is not None:
                grade = input("请输入成绩：")
                manager.add_grade_to_student(name, grade)
            else:
                print("输入的学生不存在！")

        elif choice == "3":
            name = input("请输入想要删除成绩的学生姓名:")
            manager.remove_student(name)

        elif choice == "4":
            manager.show_students()


        elif choice == "5":
            manager.save_to_file()
            print("退出系统！")
            break

        else:
            print("输入无效！请输入1-5整数！")
main()





