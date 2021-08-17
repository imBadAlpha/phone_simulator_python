from Message import Message


class Contacts:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
        self.message = []
        self.msgID = 0

    def add_message(self, text):
        self.msgID += 1
        self.message.append(Message(self.msgID, text))

    def show_all_message(self):
        for msg in self.message:
            print("ID: ", msg.id_num, "\n" + msg.text + "\n" +
                  "*********************************")

    def get_details(self):
        print("Name: " + self.name + " " +
              "\nNumber: " + self.number + " " +
              "\nEmail: " + self.email + "\n")
