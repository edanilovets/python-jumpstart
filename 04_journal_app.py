#
# JOURNAL APP
#


def print_header():
    print("--------------------")
    print("    JOURNAL APP")
    print("--------------------")


def run_event_loop():
    print("What do you want to do with your journal?")
    cmd = None

    while cmd != "x":
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")
        if cmd.lower().strip() == "l":
            print("L")
        elif cmd.lower().strip() == "a":
            print("A")
        elif cmd.lower().strip() != "x":
            print("Sorry, we don't understand '{}'".format(cmd))

    print("Done, goodbye.")


def main():
    print_header()
    run_event_loop()


main()
