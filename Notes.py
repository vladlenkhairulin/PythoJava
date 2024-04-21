from datetime import datetime
import json
import os

id = 0
class Note:
    def __init__(self, file_name):
        self.file_name = file_name
        # Список файлов с созданными заметок нужен для того, чтобы затем передать его в метод read_all
        self.created_files = []  
    def add(self):
        global id
        id += 1
        headline = input("Введите заголовок заметки: ")
        msg = input("Введите текст заметки: ")
        date_of_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note_data = {
            "Заголовок": headline,
            "Текст заметки": msg,
            "Дата изменения": date_of_creation
        }
        with open(self.file_name, "w", encoding="utf-8") as file:
            # Без параметра ensure_ascii=False данные в файл записывались как набор кодированных символов
            json.dump(note_data, file, ensure_ascii=False)
        self.created_files.append(self.file_name)
    def read(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            note_data = json.load(file)
            print("Заголовок:", note_data["Заголовок"])
            print("Текст заметки:", note_data["Текст заметки"])
            print("Дата изменения:", note_data["Дата изменения"])
 #  def read_all(self):
 #       for file_name in self.created_files:
 #          with open(file_name, "r") as file:
 #               current_note = {}
 #                for line in file:
 #                   if line.startswith("Дата изменения:"):
 #                       '''
 #                           Преобразуем строку даты в объект datetime с помощью метода strptime, делаем сплит только 
 #                       первого символа двоеточия, чтобы метод не затрагивал символы двоеточия, которые есть в дате.
 #                           "Дата изменения", "заголовок" и "тело заметки" - это ключи словаря, у которых есть
 #                           конкретные значения в каждой заметке. Нам нужно отсортировать значения ключа "Дата изменения"
 #                        '''
 #                       current_note["Дата изменения"] = datetime.strptime(line.split(":", 1)[1].strip(), "%Y-%m-%d %H:%M:%S")
 #                   # Проверяем, остались ли ещё в файле заголовок и тело заметки
 #                   elif line:  
 #                      key, value = line.split(":", 1)
 #                      current_note[key.strip()] = value.strip()
 #               all_notes.append(current_note)  
 #       # список all_notes состоит из словарей, по одному словарю для каждой заметки. Из каждого словаря мы достаём только значение ключа "Дата изменения"        
 #       sorted_notes = sorted(all_notes, key=lambda x: x["Дата изменения"])
 #        for note in sorted_notes:
 #            print("Заголовок:", note["Заголовок"])
 #            print("Текст заметки:", note["Текст заметки"])
 #            print("Дата изменения:", note["Дата изменения"])
 #            print()
    
    # Сначала я пытался сделать заметки в формате .txt, выше код для .txt
    def read_all(self):
        all_notes = []
        for file_name in self.created_files:
            with open(file_name, "r", encoding="utf-8") as file:
                # Чтение данных из JSON файла
                note_data = json.load(file)  
                all_notes.append(note_data)

        '''
         в json файле данные представлены в виде словаря, я сортирую каждый файл по значению ключа "Дата изменения"
         strptime - метод для конвертации строкового типа в тип даты, чтобы отсортировать по дате.
        '''
        sorted_notes = sorted(all_notes, key=lambda x: datetime.strptime(x["Дата изменения"], "%Y-%m-%d %H:%M:%S"))
        for note in sorted_notes:
            print("Заголовок:", note["Заголовок"])
            print("Текст заметки:", note["Текст заметки"])
            print("Дата изменения:", note["Дата изменения"])
            print()

    def change(self):
        new_headline = input("Введите новый заголовок: ")
        new_msg = input("Введите новый текст заметки: ")
        date_of_change = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "r+", encoding="utf-8") as file:
            note_data = json.load(file)
            note_data["Заголовок"] = new_headline
            note_data["Текст заметки"] = new_msg
            note_data["Дата изменения"] = date_of_change
            # возвращаемся в начало файла с помощью команды seek(0)
            file.seek(0)
            # создаём новый файл с тем же названием, но новыми данными
            json.dump(note_data, file, ensure_ascii=False)
            # truncate нужен, чтобы обрезать все лишние байты, после того как длина сообщения в файле изменилась
            file.truncate()
        print("Заметка успешно изменена.")
    def delete(self):
        try:
            # модуль os нужен, чтобы полностью удалить файл из директории проекта
            os.remove(file_name)            
            # удаляем файл из списка созданных файлов
            if file_name in self.created_files:
                self.created_files.remove(file_name)
            print(f"Заметка '{file_name}' успешно удалена.")
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")
        except Exception as e:
            print(f"Ошибка при удалении файла {file_name}: {e}")

file_name = input("Введите название вашей заметки: ")
note = Note(file_name)

print("Выберите команду [add, read, read_all, change, delete, exit]:")
work_with_user = input()
session = True
while session:
    if work_with_user == "add":
        #note_id = id + 1
        #headline = input("Введите заголовок заметки: ")
        #msg = input("Введите тело заметки: ")
        #date_of_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #file_name = input("Введите имя файла для сохранения заметки: ")
        #note = Note(note_id, headline, msg, date_of_creation)
        note.add()
        #print("Заметка успешно сохранена.")
        print("Выберите команду [add, read, read_all, change, delete, exit]:")
        work_with_user = input()

    elif work_with_user == "read":
        #file_read_name = input("Введите имя файла для чтения заметки: ")
        #note = Note()
        note.read()
        print("Выберите команду [add, read, read_all, change, delete, exit]:")
        work_with_user = input()


    elif work_with_user == "read_all":
        #note = Note()
        note.read_all()
        print("Выберите команду [add, read, read_all, change, delete, exit]:")
        work_with_user = input()

    elif work_with_user == "change":
        #file_change_name = input("Введите имя файла для изменения заметки: ")
        #note = Note()
        #note.read(file_change_name)
        #new_headline = input("Введите новый заголовок")
        #new_msg = input("Введите новый текст заметки")
        note.change()
        print("Выберите команду [add, read, read_all, change, delete, exit]:")
        work_with_user = input()



    elif work_with_user == "delete":
         #file_delete_name = input("Введите имя файла для удаления заметки: ")
         #note = Note()
         note.delete()
         print("Выберите команду [add, read, read_all, change, delete, exit]:")
         work_with_user = input()



    elif work_with_user == "exit":
        session = False

    else:
        print("Выберите существующую команду!")
        print("Выберите команду [add, read, read_all, change, delete, exit]:")
        work_with_user = input()

