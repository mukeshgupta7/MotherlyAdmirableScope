class MonitoringAgent:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def check_performance(self, campaign_metrics):
        suggestions = {}
        if campaign_metrics['CTR'] < self.thresholds['CTR']:
            suggestions['content'] = 'Update content to be more engaging.'
        if campaign_metrics['conversion_rate'] < self.thresholds['conversion_rate']:
            suggestions['call_to_action'] = 'Adjust the call-to-action.'
        return suggestions
