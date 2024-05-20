import TkEasyGUI as eg


def main():
    with eg.Window(
        "test",
        layout=[
            [eg.Text("The rest of me is a mere appendix.")],
            [eg.Button("OK")],
        ],
    ) as window:
        for event, values in window.event_iter():
            if event == "OK":
                eg.print("Thank you.")
                break


if __name__ == "__main__":
    main()
