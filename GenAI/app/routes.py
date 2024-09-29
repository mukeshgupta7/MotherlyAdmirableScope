from flask import Blueprint, request, jsonify
from app.agents.segmentation_agent import SegmentationAgent
from app.agents.content_agent import ContentAgent
from app.agents.optimization_agent import OptimizationAgent
from app.agents.monitoring_agent import MonitoringAgent
import pandas as pd
import numpy as np
import json

main = Blueprint('main', __name__)

# Load and preprocess real-life marketing data
campaign_data = pd.read_csv('data/marketing_campaign.csv').to_dict(orient='records')
thresholds = {'CTR': 0.03, 'conversion_rate': 0.02, 'engagement_rate': 0.6}

# Initialize agents
segmentation_agent = SegmentationAgent(campaign_data)
content_agent = ContentAgent()
optimization_agent = OptimizationAgent(campaign_data)
monitoring_agent = MonitoringAgent(thresholds)

@main.route('/')
def index():
    return 'Hello'

@main.route('/process_campaign', methods=['POST'])
def process_campaign():
    data = request.json
    customer_data = data.get('customer_data', {})
    prompt = data.get('prompt', '')
    real_time_metrics = data.get('metrics', {})

    # Step 1: Audience Segmentation
    segment = segmentation_agent.segment(customer_data)
    print("##segmentation_agent.")

    # Step 2: Content Generation
    generated_content = content_agent.generate_content(prompt, segment)
    print("##content_agent.")
    
    # Step 3: Campaign Optimization
    optimization = optimization_agent.get_optimization_suggestions(segment)
    print("##optimization_agent.")
    
    # Step 4: Monitor real-time performance and adjust
    performance_suggestions = monitoring_agent.check_performance(real_time_metrics)
    print("##monitoring_agent.")

    segment = int(segment) if isinstance(segment, (np.int32, np.int64)) else segment
    optimization = int(optimization) if isinstance(optimization, (np.int32, np.int64)) else optimization
    performance_suggestions = int(performance_suggestions) if isinstance(performance_suggestions, (np.int32, np.int64)) else performance_suggestions
    
    # return jsonify({
    #     "segment": segment,
    #     "generated_content": generated_content,
    #     "optimization": optimization,
    #     "performance_suggestions": performance_suggestions
    # }, ensure_ascii=False)

# ...

    return json.dumps({"segment": segment, "generated_content": generated_content, "optimization": optimization, "performance_suggestions": performance_suggestions}), 200, {"Content-Type": "application/json"}
