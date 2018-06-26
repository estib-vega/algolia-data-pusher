"""
Entry point - main.py

starts up the UI and asks for:
- Index name
- Api key
- App Id

then it asks for the information files to be transmitted


"""
import server_ui

def main():
    # startup ui
    server_ui.start(1234)


if __name__ == "__main__":
    main()