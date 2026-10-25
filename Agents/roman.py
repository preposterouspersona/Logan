""" Roman - Data Collection Agent 
    Roman secures the data related to a particular stock.
    It involves market data, company info, financial metrics.
    Handles weekend/holiday news periods automatically.
"""

from typing import Dict, Any, List, Optional
from ..workflows.state import AgentState
from ..tools.yfinance import get_market_data, get_company_info
