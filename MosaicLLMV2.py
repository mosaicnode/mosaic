from typing import Dict, Any
import re

class MosaicLLM:
    def __init__(self):
        """
        Initialize the MosaicLLM with command patterns and a simulated blockchain interaction layer.
        """
        # Dictionary to map natural language commands to blockchain operations
        self.command_patterns = {
            r"send (\d+(?:\.\d+)?) SOL to ([A-Za-z0-9]{32,44})": self.send_sol,
            r"query balance of ([A-Za-z0-9]{32,44})": self.query_balance,
            r"get transaction history for ([A-Za-z0-9]{32,44})": self.get_transaction_history,
            # Add more patterns as needed
        }
        
        # Simulated blockchain interaction layer
        self.blockchain = {
            'balances': {
                'ExampleAddress1': 1000000000,  # 1 SOL in lamports
                'ExampleAddress2': 500000000    # 0.5 SOL in lamports
            },
            'transactions': {
                'ExampleAddress1': ['tx1', 'tx2', 'tx3'],
                'ExampleAddress2': ['tx4', 'tx5']
            }
        }

    def process_command(self, user_input: str) -> str:
        """
        Process natural language input to execute blockchain operations.

        :param user_input: User's natural language command
        :return: Response after processing the command
        """
        for pattern, action in self.command_patterns.items():
            match = re.match(pattern, user_input, re.IGNORECASE)
            if match:
                return action(*match.groups())
        
        return "I'm sorry, I didn't understand that command. Please try again or ask for help."

    def send_sol(self, amount: str, recipient: str) -> str:
        """
        Simulates sending SOL to a recipient address.

        :param amount: Amount of SOL to send
        :param recipient: Recipient's public key
        :return: Confirmation message
        """
        # Convert amount to lamports (1 SOL = 1 billion lamports)
        amount_lamports = int(float(amount) * 1e9)
        
        # Check if the sender has enough balance (simulated sender is 'ExampleAddress1')
        if 'ExampleAddress1' in self.blockchain['balances'] and self.blockchain['balances']['ExampleAddress1'] >= amount_lamports:
            self.blockchain['balances']['ExampleAddress1'] -= amount_lamports
            if recipient in self.blockchain['balances']:
                self.blockchain['balances'][recipient] += amount_lamports
            else:
                self.blockchain['balances'][recipient] = amount_lamports
            
            # Simulate adding transaction to history
            self.blockchain['transactions']['ExampleAddress1'].append(f"Sent {amount} SOL to {recipient}")
            return f"Successfully sent {amount} SOL to {recipient}."
        else:
            return "Insufficient balance to complete the transaction."

    def query_balance(self, address: str) -> str:
        """
        Simulates querying the balance of a given address.

        :param address: The address to query
        :return: Balance information
        """
        if address in self.blockchain['balances']:
            balance = self.blockchain['balances'][address] / 1e9  # Convert lamports to SOL
            return f"The balance of {address} is {balance} SOL."
        else:
            return f"Address {address} not found or has no balance."

    def get_transaction_history(self, address: str) -> str:
        """
        Simulates retrieving the transaction history for an address.

        :param address: The address to get transaction history for
        :return: Transaction history
        """
        if address in self.blockchain['transactions']:
            history = self.blockchain['transactions'][address]
            return f"Transaction history for {address}: {', '.join(history)}"
        else:
            return f"No transaction history found for {address}."

# Example usage
if __name__ == "__main__":
    mosaic_llm = MosaicLLM()
    
    # Simulate user interaction
    print(mosaic_llm.process_command("send 0.5 SOL to ExampleAddress2"))
    print(mosaic_llm.process_command("query balance of ExampleAddress1"))
    print(mosaic_llm.process_command("get transaction history for ExampleAddress1"))
    print(mosaic_llm.process_command("send 2 SOL to ExampleAddress3"))  # This should fail due to insufficient balance
    print(mosaic_llm.process_command("query balance of ExampleAddress3"))  # This should show no balance
