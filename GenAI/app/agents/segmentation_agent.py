# from sklearn.cluster import KMeans
# import pandas as pd

# class SegmentationAgent:
#     def __init__(self, campaign_data):
#         self.campaign_data = campaign_data
#         self.X = pd.DataFrame(campaign_data)[['Age', 'Income', 'Engagement_Rate']]
#         self.kmeans = KMeans(n_clusters=3)
#         self.kmeans.fit(self.X)

#     def segment(self, customer_data):
#         customer_features = [customer_data['Age'], customer_data['Income'], customer_data['Engagement_Rate']]
#         return self.kmeans.predict([customer_features])[0]

from sklearn.cluster import KMeans
import pandas as pd

class SegmentationAgent:
    def __init__(self, campaign_data):
        self.campaign_data = campaign_data
        self.X = pd.DataFrame(campaign_data)[['Age', 'Income', 'Engagement_Rate']]
        self.feature_names = self.X.columns.tolist()
        self.X = self.X.values
        self.kmeans = KMeans(n_clusters=3)
        self.kmeans.fit(self.X)

    def segment(self, customer_data):
        customer_features = [customer_data['Age'], customer_data['Income'], customer_data['Engagement_Rate']]
        return self.kmeans.predict([customer_features])[0]
