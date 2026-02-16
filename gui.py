import FreeSimpleGUI as sg

label = sg.Text("Напишіть задачу:")
input_box = sg.InputText(tooltip="Впешіть задачу")
add_botton = sg.Button("Додати")

window = sg.Window('My To-do App', layout=[[label] ,[input_box, add_botton]])
window.read()
window.close()

