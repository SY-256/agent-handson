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

def run_agent(input_data):
    """エージェントを実行し、結果を処理する"""
    # AIエージェント呼び出しに使うconfigurationの作成
    config = {"configurable":
              {"thread_id": st.session_state.thread_id}
    }

    # 結果を処理
    with st.spinner("処理中...", show_time=True):
        for chunk in agent.stream(input_data, stream_mode="updates", config=config):
            for task_name, result in chunk.items():
                # interruptの場合
                if task_name == "__interrupt__":
                    st.session_state.tool_info = result[0].value
                    st.session_state.waiting_approval = True
                # 最終回答の場合
                elif task_name == "agent":
                    st.session_state.final_result = result.content
                # LLM推論の場合
                elif task_name == "invoke_llm":
                    if isinstance(chunk["invoke_llm"].content, list):
                        for content in result.content:
                            if content["type"] == "text":
                                st.session_state.messages.append({"role": "assistant", "content": content["text"]})
                # ツール実行の場合
                elif task_name == "use_tool":
                    st.session_state.messages.append({"role": "assistant", "content": "ツール実行"})

        st.rerun()


