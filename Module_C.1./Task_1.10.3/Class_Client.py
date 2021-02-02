#                                     ("\(O_o)/")
class Client:
    def __init__(self, name="---", wallet_balance=0):
        self.name = name
        self.wallet_balance = wallet_balance

    def list_processing(self, client_info):
        self.name = client_info.get("Name")
        if isinstance(client_info.get("Wallet"), float):
            self.wallet_balance = "$ " + str(client_info.get("Wallet"))
        else:
            return print("Incorrect value.", client_info.get("Wallet"))

    def show_info(self):
        return f"Client: {self.name} \nWallet balance: {self.wallet_balance}"

client_list = [
    {
        "Name": "Ivan Petrov",
        "Wallet": 50.0
    },
    {
        "Name": "Vladimir Pupkin",
        "Wallet": 0.99999
    },
    {
        "Name": "Donald Trump",
        "Wallet": 999999.0
    }
]

for i in client_list:
    c = Client()
    c.list_processing(i)
    print(c.show_info())