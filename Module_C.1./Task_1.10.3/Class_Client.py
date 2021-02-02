#                                     ("\(O_o)/")
client_list = [{"Name": "Ivan Petrov", "Wallet": 50.0}]

class Client:
    def __init__(self, name, wallet_balance, ):
        self.name = name
        self.wallet_balance = wallet_balance

    def list_processing(self, client_info):
        self.name = client_info.get("Name")
        self.wallet_balance = client_info.get("Wallet")
        if isinstance(client_info.get("Wallet"), float):
            self.wallet_balance = "$", str(client_info.get("Wallet"))
        else:
            return print("Incorrect value.", client_info.get("Wallet"))

    def show_info(self):
        return f"""Client: {self.name} \nWallet balance: {self.wallet_balance}"""

    def add_client(self):
        client_list.append({"Name": {self.name}, "Wallet": {self.wallet_balance}})