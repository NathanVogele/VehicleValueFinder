#################################################################
## WORK IN PROGRESS ... GUI will be coming in a future release.##
#################################################################



# import PySimpleGUI as sg
# import models
# import sheetworker

# sg.theme("DarkTeal2")
# choose_file = [[sg.T("")], [sg.Text("Choose a xlsx File: "), sg.Input(key="+-" ,change_submits=True), sg.FileBrowse(key="-IN-")],[sg.Button("Process")]]
# save_layout = [[sg.T("")], [sg.Text("Where do you want to export?: "), sg.Input(key="-IN3-" ,change_submits=True), sg.FolderBrowse()],[sg.Button("Submit")]]
# done_layout = sg.Window('Thank You, please check the file before you print')
# api_warning = sg.Window('Please Note, there are only X # API Calls Per Month Available.'), sg.Button("Ok")

# ###Building Window
# window = sg.Window('Where is your list of vins?', choose_file, size=(600,150))
# warning_window = sg.Window('Please Read', api_warning, size=(600,150))
# save_window = sg.Window('Where do you want to save your file?', save_layout, size=(600,150))
# done_window = sg.Window('Your file has been processed', done_layout, size=(600,150))

# while True:
#     event, values = window.read()
#     print(values["-IN2-"])
#     vinFileLocation = values["-IN2-"]
#     if event == sg.WIN_CLOSED or event=="Exit":
#         break
#     elif event == "Process":
#         event, values = save_window.read()
#         print(values["-IN3-"])
#         vinSaveLocation = values["-IN3-"]
#         if event == sg.WIN_CLOSED or event=="Exit":
#             break
#         elif event == "Submit":
#             print(vinFileLocation)
#             print(vinSaveLocation)