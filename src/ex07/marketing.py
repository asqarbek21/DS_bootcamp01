import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com']

participants = ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

def get_sets():
    return set(clients), set(participants), set(recipients)

def call_center():
    clients_set, _, recipients_set = get_sets()
    return clients_set - recipients_set

def potential_clients():
    clients_set, participants_set, _ =  get_sets()
    return participants_set - clients_set

def loyalty_program():
    clients_set, participants_set, _ = get_sets()
    return clients_set - participants_set


def main():
    if len(sys.argv) != 2:
        return
    task = sys.argv[1]

    try:
        if task == 'call_center':
            result = call_center()

        elif task == 'potential_clients':
            result = potential_clients()

        elif task == 'loyalty_program':
            result = loyalty_program()

        else:
            raise Exception("Invalid task name")


        for email in result:
            print(email)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()                            