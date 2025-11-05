import uuid
import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph.types import Command

# core.pyからエージェントをインポート
from x_agent_core import agent

def init_session_state():
    """セッション状態を初期化する"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'waiting_for_approval' not in st.session_state:
        st.session_state.waiting_for_approval = False
    if 'final_result' not in st.session_state:
        st.session_state.final_result = None
    if 'thread_id' not in st.session_state:
        st.session_state.thread_id = None

def reset_session():
    """セッション状態をリセットする"""
    st.session_state.messages = []
    st.session_state.waiting_for_approval = False
    st.session_state.fina_result = None
    st.session_state.thread_id = None

# セッション状態の初期化
init_session_state()
