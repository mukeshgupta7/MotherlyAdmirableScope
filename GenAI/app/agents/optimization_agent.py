class OptimizationAgent:
    def __init__(self, campaign_data):
        self.campaign_data = campaign_data

    def get_optimization_suggestions(self, customer_segment):
        return {
            "best_time": "2 PM",
            "best_channel": "Email"
        }
