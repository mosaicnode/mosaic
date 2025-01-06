from typing import Dict, List
from datetime import datetime

class UserBehaviorInsights:
    def __init__(self):
        """
        Initialize the UserBehaviorInsights with a simulated database to store user interactions.
        """
        self.user_data = {}  # Dictionary to store user interaction data

    def record_interaction(self, user_id: str, interaction_type: str, details: Dict):
        """
        Records a user's interaction with the blockchain.

        :param user_id: Unique identifier for the user
        :param interaction_type: Type of interaction (e.g., 'transaction', 'query', 'staking')
        :param details: Dictionary containing details of the interaction
        """
        if user_id not in self.user_data:
            self.user_data[user_id] = []
        
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'type': interaction_type,
            'details': details
        }
        self.user_data[user_id].append(interaction)

    def analyze_user_behavior(self, user_id: str) -> Dict:
        """
        Analyzes the behavior of a specific user based on recorded interactions.

        :param user_id: Unique identifier for the user to analyze
        :return: Dictionary with insights on user behavior
        """
        if user_id not in self.user_data:
            return {"error": "User not found or no interaction data available."}
        
        interactions = self.user_data[user_id]
        insights = {
            'total_interactions': len(interactions),
            'interaction_types': {},
            'frequency': {},
            'engagement_level': 'Low',  # Default, will be updated based on analysis
            'recommendations': []
        }
        
        # Count interaction types
        for interaction in interactions:
            interaction_type = interaction['type']
            if interaction_type not in insights['interaction_types']:
                insights['interaction_types'][interaction_type] = 0
            insights['interaction_types'][interaction_type] += 1
            
            # Calculate interaction frequency per day
            date = interaction['timestamp'].split('T')[0]
            if date not in insights['frequency']:
                insights['frequency'][date] = 0
            insights['frequency'][date] += 1
        
        # Determine engagement level
        if insights['total_interactions'] > 10:
            insights['engagement_level'] = 'High'
        elif insights['total_interactions'] > 5:
            insights['engagement_level'] = 'Medium'
        
        # Tailor recommendations based on insights
        self._generate_recommendations(insights, interactions)
        
        return insights

    def _generate_recommendations(self, insights: Dict, interactions: List):
        """
        Generates personalized recommendations based on user behavior analysis.

        :param insights: Dictionary containing user behavior insights
        :param interactions: List of user interactions
        """
        if 'transaction' in insights['interaction_types'] and insights['interaction_types']['transaction'] > 5:
            insights['recommendations'].append("Consider using our transaction optimization tool for better efficiency.")
        
        if 'query' in insights['interaction_types'] and insights['interaction_types']['query'] > 3:
            insights['recommendations'].append("You might benefit from our advanced analytics for deeper market insights.")
        
        if 'staking' in insights['interaction_types']:
            insights['recommendations'].append("Explore our staking automation features to manage your stakes more effectively.")
        
        # Example of more personalized recommendation based on frequency
        if len(insights['frequency']) > 7:  # If interaction over more than a week
            insights['recommendations'].append("Given your consistent interaction, you're eligible for our loyalty program.")
        
        # Example of recommendation based on engagement level
        if insights['engagement_level'] == 'Low':
            insights['recommendations'].append("Increase your engagement with our platform by trying out different features.")
        elif insights['engagement_level'] == 'High':
            insights['recommendations'].append("Thank you for your high engagement! Consider becoming a community contributor.")

# Example usage
if __name__ == "__main__":
    insights_tool = UserBehaviorInsights()
    
    # Simulate user interactions
    insights_tool.record_interaction('user1', 'transaction', {'
