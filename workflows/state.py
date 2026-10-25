"""Defines the Agent State schema for LangGraph orchestration."""

from typing import TypedDSict, Optional, Dict, List, Any
from datetime import datetime


class AgentState(TypedDict):
    """
    Common data structre that passes through the orchestration graph.
    """

    session_id: str
    symbols: List[str]
    current_step: str
    analysis_date: str # Date of stock analysis.


    data_collection_results : Optional[Dict[str,Any]]
    technical_analysis_results : Optional[Dict[str,Any]]
    news_intelligence_results : Optional[Dict[str,Any]]
    portfolio_manager_results : Optional[Dict[str,Any]]
    #bull_vs_bear_results: Optional[Dict[str,Any]]
    
    error: Optional[str]



def initialize_state(session_id:str, symbols: List[str] ,analysis_date : Optional[str] = None ) -> AgentState :

    if analysis_date is None:
        analysis_date = datetime.now().strftime("%Y-%m-%d")

    return AgentState(
        session_id=session_id,
        symbols=symbols,
        analysis_date=analysis_date,
        current_step="initialized",
        data_collection_results=None,
        technical_analysis_results=None,
        news_intelligence_results=None,
        portfolio_manager_results=None,
        error=None
    )   

def assign_error(state: AgentState, error_message: str) -> AgentState:
    """assign error in state"""
    state["error"]=error_message
    state["current_step"] ="error"
    return state
 
    