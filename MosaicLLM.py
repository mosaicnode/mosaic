from typing import Dict, List

class MosaicLLM:
    def __init__(self):
        """
        Initialize the MosaicLLM with a simulated knowledge base and user profiles.
        """
        # Simulated knowledge base with different levels of explanation
        self.knowledge_base = {
            'blockchain': {
                'beginner': "A blockchain is like a digital ledger where transactions are recorded in blocks, linked together in a chain.",
                'intermediate': "Blockchain technology is a decentralized database managed by multiple participants, across multiple computers, ensuring that each transaction is validated by consensus.",
                'advanced': "Blockchain operates on principles of distributed ledger technology, cryptographic security, and consensus mechanisms like Proof of Work or Proof of Stake to maintain a tamper-evident record of transactions."
            },
            'smart_contract': {
                'beginner': "A smart contract is like a digital vending machine; it automatically executes actions when certain conditions are met.",
                'intermediate': "Smart contracts are self-executing contracts where the terms of the agreement are directly written into code, deployed on the blockchain, and automatically enforce and execute agreements.",
                'advanced': "Smart contracts utilize blockchain technology to facilitate, verify, or enforce the negotiation or performance of a contract, using cryptographic hash functions for security and immutability."
            },
            # Add more topics here
        }
        
        # User profiles to simulate different knowledge levels
        self.user_profiles = {
            'User1': 'beginner',
            'User2': 'intermediate',
            'User3': 'advanced'
        }

    def generate_content(self, topic: str, user_id: str) -> str:
        """
        Generates educational content based on the topic and the user's knowledge level.

        :param topic: The blockchain topic to explain
        :param user_id: The ID of the user to tailor the explanation for
        :return: A string containing the educational content
        """
        if user_id not in self.user_profiles:
            return "User profile not found. Please register or provide a valid user ID."
        
        user_level = self.user_profiles[user_id]
        if topic not in self.knowledge_base or user_level not in self.knowledge_base[topic]:
            return f"Sorry, we don't have information on {topic} at the {user_level} level."
        
        return self.knowledge_base[topic][user_level]

    def adapt_knowledge_level(self, user_id: str, feedback: str) -> str:
        """
        Adapts the user's knowledge level based on feedback.

        :param user_id: The ID of the user
        :param feedback: Feedback on whether the content was too simple or too complex
        :return: A message confirming the change or current status
        """
        if user_id not in self.user_profiles:
            return "User profile not found. Please register or provide a valid user ID."
        
        current_level = self.user_profiles[user_id]
        levels = ['beginner', 'intermediate', 'advanced']
        
        if feedback.lower() == 'too simple':
            new_level = levels[min(levels.index(current_level) + 1, len(levels) - 1)]
        elif feedback.lower() == 'too complex':
            new_level = levels[max(levels.index(current_level) - 1, 0)]
        else:
            return "Please provide feedback as 'too simple' or 'too complex'."
        
        self.user_profiles[user_id] = new_level
        return f"Knowledge level for {user_id} updated to {new_level}."

# Example usage
if __name__ == "__main__":
    llm = MosaicLLM()
    
    # Educate a beginner user about blockchain
    print(llm.generate_content('blockchain', 'User1'))
    
    # Educate an intermediate user about smart contracts
    print(llm.generate_content('smart_contract', 'User2'))
    
    # Adapting knowledge level based on feedback
    print(llm.adapt_knowledge_level('User1', 'too simple'))
    
    # Now educate the same user after level change
    print(llm.generate_content('blockchain', 'User1'))
