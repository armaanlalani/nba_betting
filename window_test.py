import PySimpleGUI as sg
import traceback

def main():
    try:
        layout = [
            [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

        window = sg.Window('Window Title', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            print('You entered ', values[0])
    except Exception as e:
        print("Exception caught:")
        print(e)
        traceback.print_exc()
    finally:
        window.close()

if __name__ == "__main__":
    main()