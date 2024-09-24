# agents/__init__.py

# This file allows the agents package to be recognized as a module.
# It initializes and manages imports for all the AI agents involved in the system.

from .segmentation_agent import SegmentationAgent
from .content_agent import ContentAgent
from .optimization_agent import OptimizationAgent
from .monitoring_agent import MonitoringAgent

# The agents can be initialized from here if needed, or they can be managed individually in the routes.
