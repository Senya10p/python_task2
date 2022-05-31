HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []
today = []
tomorrow = []
other = []

run = True

by = ''
while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    # print(tasks)
    print("Сегодня:", today)
    print("Завтра:", tomorrow)
    print("Другие:", other)
    print("Все задачи:", tasks)
  elif command == "add":
    while run:
      date = input('Введите дату: ')
      if "no" == date:
        break
      task = input("Введите название задачи: ")
      tasks.append(task)
      if "Сегодня" == date:
        today.append(task)
      elif "Завтра" == date:
        tomorrow.append(task)
      else:
        other.append(task)
      print("Задача добавлена")
  elif "exit" == command:
    by = "Спасибо за использование! "
    break
  else: 
    print("Неизвестная команда")
    break

print(by + "До свидания!")
