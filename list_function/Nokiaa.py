def mainmenu():
    menu = """
    1.Phone Book
    2.Message
    3.Chat
    4.Call Register
    5.Tone
    6.Setting
    7.Call divert
    8.Game
    9.Calculator
    10.Reminder
    11.Clock
    12.Profile
    13.SIM services"""
    print(menu)
    menu = int(input())
    match menu:
        case 1:
            phonebook()
        case 2:
            messagess()
        case 3:
            chats()
        case 4:
            callregister()
        case 5:
            tone()
        case 6:
            setting()
        case 7:
            calldivert()
        case 8:
            game()
        case 9:
            calculator()
        case 10:
            reminder()
        case 11:
            clock()
        case 12:
            profile()
        case 13:
            SIMservice()
        case _:
            print("Invalid input""Bye bye")


def phonebook():
    phone = """
    1.Search
    2.Services Nos
    3.Add name
    4.Erase
    5.Assign
    6.Assign tone
    7.Send b'card
    8.Option
    9.Speed dials
    10.Voice tags"""
    print(phone)
    phone = int(input())
    match phone:
        case 1:
            print("Search")
        case 2:
            print("Service Nos")
        case 3:
            print("Add name")
        case 4:
            print("Erase")
        case 5:
            print("Edit")
        case 6:
            print("Assign tone")
        case 7:
            print("Send b' card")
        case 8:
            print("""
                1.Type of message
                2.Mermory status
                3.Go back 
                4.main menu""")
            option = int(input())
            match option:
                case 1:
                    print("Type of menu")
                case 2:
                    print("Mermory status")
                case 3:
                    phonebook()
                case 4:
                    mainmenu()
                case _:
                    print("Invalid input""Bye bye")
        case 9:
            print("Speed dial")
        case 10:
            print("Voice tags")
        case 11:
            mainmenu()
        case _:
            print("Invalid input""Bye bye")


def messagess():
    messages = """
1.Write Messages
2.Inbox
3.Outbox
4.Picture Message
5.Template
6.Smileys
7.Message Setting
8.Info Services
9.Voice mailbox Number
10.Service Command editor
11.Main menu
            """
    print(messages)
    message = int(input())
    match message:
        case 1:
            print("Write Message")
        case 2:
            print("Inbox")
        case 3:
            print("Outbox")
        case 4:
            print("Picture Messages")
        case 5:
            print("Template")
        case 6:
            print("Smiley")
        case 7:
            print("Message Setting");
            print("""
                    1.Set 1
                    2.Common
                    3.Go back
                    4.Main menu""")

            setting = int(input())
            match setting:
                case 1:
                    print("""
                            1.Message center number
                            2.Message sent as
                            3.Message validity
                            4.Go back
                            5.Main Menu""")

                    settingTwo = int(input())
                    match settingTwo:
                        case 1:
                            print("Message center number")
                        case 2:
                            print("Message sent as")
                        case 3:
                            print("Message validity")
                        case 4:
                            messagess()
                        case 5:
                            mainmenu()
                        case _:
                            print("Invalid input""Bye bye")

                case 2:
                    print("""
                            1.Delivery report
                            2.Reply via same center
                            3.Character support
                            4.Go back
                            5.Main menu""")
                    common = int(input())
                    match common:
                        case 1:
                            print("Delivery report")
                        case 2:
                            print("Reply via same setter")
                        case 3:
                            print("Charater support")
                        case 4:
                            messagess()
                        case 5:
                            mainmenu()
                        case 3:
                            messagess()
                        case 4:
                            mainmenu()
                        case _:
                             print("Invalid input""Bye bye")
        case 8:
            print("Info Services")
        case 9:
            print("Voice mailbox number")
        case 10:
            print("Service Command editor")
        case 11:
            mainmenu()
        case _:
            print("Invalid input""Bye bye")


def chats():
    chat = """
            1.Chat
            2.Main menu"""
    print(chat)
    chat = int(input())
    match chat:
        case 1:
            print("Chat")
        case 2:
            mainmenu()
        case _:
            print("Invalid input""Bye bye")


def callregister():
    call = """
    1.Missed calls
    2.Received calls
    3.Dialled numbers
    4.Erase recent call lists
    5.Show call duration
    6.Show call costs
    7.Call cost setting
    8.Prepaid credit
    9.Main menu
    """
    print(call)
    call = int(input())
    match call:
        case 1:
            print("Missed calls")
        case 2:
            print("Received calls")
        case 3:
            print("Dailled numbers")
        case 4:
            print("Erase recent call lists")
        case 5:
            print("""
                    1.Last call duration
                    2.All calls cost
                    3.Received calls duration
                    4.Dialled calls duration
                    5.Clear timer
                    6.Go back
                    7.Main menu""")
            callTwo = int(input())
            match callTwo:
                case 1:
                    print("Last call duration")
                case 2:
                    print("All calls cost")
                case 3:
                    print("Received calls duration")
                case 4:
                    print("Dialled calls duration")
                case 5:
                    print("Clear timer")
                case 6:
                    callregister()
                case 7:
                    mainmenu()
                case _:
                    print("Invalid input""Bye bye")
        case 6:
            print("""
                    1.Last calls cost
                    2.All calls cost
                    3.Clear counter
                    4.Go back
                    5.main menu""")
            callthree = int(input())
            match callthree:
                case 1:
                    print("Last call cost")
                case 2:
                    print("All calls cost")
                case 3:
                    print("Clear counter")
                case 4:
                    callregister()
                case 5:
                    mainmenu()
                case 7:
                    print("""
                            1.Calls limit
                            2.Show cost in
                            3.Go back
                            4.main menu""")
                    callfour = int(input())
                    match callfour:
                        case 1:
                            print("Call limit ")
                        case 2:
                            print("Show cost in")
                        case 3:
                            callregister()
                        case 4:
                            mainmenu()
        case 8:
            print("Prepaid credits ")
        case 9:
            mainmenu()
        case _:
            print("Invalid input""Bye bye")


def tone():
    tones = """
    1.Ringing tone
    2.Ringing volume
    3.Incoming call alert
    4.Composer
    5.Message alert tone
    6.Keypad tones
    7.Warning and game tones
    8.Vibrating alert
    9.Screen saver
    10.Main menu"""
    print(tones)
    tone = int(input())
    match tone:
        case 1:
            print("Ringing tone")
        case 2:
            print("Ringing volume")
        case 3:
            print("Incoming call alert")
        case 4:
            print("Composer")
        case 5:
            print("Message alert tone")
        case 6:
            print("Keypad tones")
        case 7:
            print("Warning and game tones")
        case 8:
            print("Vibrating alert")
        case 9:
            print("Screen saver")
        case 10:
            mainmenu()


def setting():
    settings = """
    1.Call setting
    2.Phone setting
    3.Security setting
    4.Restore factory settings
    5.Go back
    6.Main menu
    """
    print(settings)
    settingss = int(input())
    match settingss:
        case 1:
            print("""
            1.Automatic redial
            2.Speed dial
            3.Call waiting option
            4.Call waiting option
            5.Phone
            6.Automatic answer
            7.Go back
            8.Main menu""")
            callsetting = int(input())
            match callsetting:
                case 1:
                    print("Automatic redial")
                case 2:
                    print("Speed dialling")
                case 3:
                    print("Call waiting")
                case 4:
                    print("Own number sending")
                case 5:
                    print("Phone line in use")
                case 6:
                    print("Automatic answer")
                case 7:
                    setting()
                case 8:
                    mainmenu()
        case 2:
            """
        1.Language
        2.Cell info display
        3.Welcome note
        4.Network selection
        5.Light
        6.Confirm SIM service actions
        7.Go back
        8.Main menu"""
            callregisters = int(input())
            match callregisters:
                case 1:
                    print("Language")
                case 2:
                    print("Cell info display")
                case 3:
                    print("Welcome note")
                case 4:
                    print("Network selection")
                case 5:
                    print("Light")
                case 6:
                    print("Confirm Sim services action")
        case 3:
            securesetting = """
            1.PIN code request
            2.Call barring service
            3.Fixed dailling
            4.Closed user group
            5.Phone security
            6.Change access codes
            7.Go back
            8.Main menu
            """
            print(securesetting)
            securitysetting = int(input())
            match securitysetting:
                case 1:
                    print("PIN code request")
                case 2:
                    print("Call barring service")
                case 3:
                    print("Closed usr group")
                case 4:
                    print("Phone security")
                case 5:
                    print("Change access codes")
                case 6:
                    setting()
                case 7:
                    mainmenu()
        case 4:
            print("Restore factory setting")
        case _:
            print("Invalid input""Bye bye")


def calldivert():
    calldiv = """
    1.Call divert
    2.Main menu"""
    print(calldiv)
    divert = int(input())
    match divert:
        case 1:
            print("Call divert");
        case 2:
            mainmenu()
        case _:
            print("Invalid input""Bye bye")


def game():
    playgame = """
    1.Game
    2.Main menu"""
    print(playgame)
    games = int(input())
    match games:
        case 1:
            print("Game")
        case 2:
            mainmenu()
        case _:
            print("Invalid input")


def calculator():
    calcu = """
1.Calculator
2.Main menu"""
    print(calcu)
    calculatorr = int(input())
    match calculatorr:
        case 1:
            print("Calculator")
        case 2:
            mainmenu()
        case _:
            print("Invalid input")


def reminder():
    rem = """
    1.Reminder
    2.Main menu"""
    print(rem)
    reminders = int(input())
    match reminders:
        case 1:
            print("Reminder")
        case 2:
            mainmenu()
        case _:
            print("Invalid input""Bye_bye")


def clock():
    clo = """
    1.Clock
    2.Main menu
    3.Date setting
    4.Stopwatch
    5.Countdown
    6.Auto update of date and time
    7.Go back
    8.Main menu"""
    print(clo)
    clocks = int(input())
    match clocks:
        case 1:
            print("Alarm clocl")
        case 2:
            print("Clock setting")
        case 3:
            print("Date setting")
        case 4:
            print("Stopwatch")
        case 5:
            print("Countdown timer")
        case 6:
            print("Auto update of date and time")
        case 7:
            clock()
        case 8:
            mainmenu()
        case _:
            print("Invalid input""Bye-bye")


def profile():
    pro = """
    1.Profile
    2.Go back
    3.Main menu
    """
    print(pro)
    profiles = int(input())
    match profiles:
        case 1:
            print("Profile")
        case 2:
            profile()
        case 3:
            mainmenu()
        case _:
            print("Invalid input""Bye bye")


def SIMservice():
    sim = """
    1.SIM service
    2.Go back
    3.Main menu
    """
    print(sim)
    simservives = int(input())
    match simservives:
        case 1:
            print("SIM services")
        case 2:
            mainmenu()
        case _:
            print("Invalid input""Bye bye")
