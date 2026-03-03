import FreeSimpleGUI as sg
import functions

label = sg.Text("Напишіть задачу:")
input_box = sg.InputText(tooltip="Впешіть задачу", key="Завдання")
add_botton = sg.Button("Додати")

window = sg.Window('My To-do App',
                   layout=[[label] ,[input_box, add_botton]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()

