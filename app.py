import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

st.set_page_config(
    page_title="専門家 AI アシスタント",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 専門家 AI アシスタント")
st.markdown("""
### 📖 アプリの概要
このアプリは、選択した分野の専門家として AI が質問に回答します。

### 🎯 使い方
1. **専門家を選択**: ラジオボタンで相談したい分野の専門家を選んでください
2. **質問を入力**: テキストボックスに質問や相談内容を入力してください
3. **回答を取得**: 「回答を取得」ボタンをクリックすると、AI 専門家が回答します

---
""")


def get_llm_response(user_input: str, expert_type: str) -> str:
    """
    LLM からの回答を取得する関数
    
    Args:
        user_input (str): ユーザーからの入力テキスト
        expert_type (str): 専門家の種類（"健康の専門家" または "資産運用の専門家"）
    
    Returns:
        str: LLM からの回答テキスト
    """
    system_messages = {
        "健康の専門家": """あなたは健康とウェルネスの専門家です。
栄養、運動、メンタルヘルス、病気の予防などについて、科学的根拠に基づいた
アドバイスを提供してください。ただし、具体的な診断や治療については
必ず医療機関の受診を勧めてください。""",
        
        "資産運用の専門家": """あなたは資産運用とファイナンシャルプランニングの専門家です。
投資戦略、資産配分、リスク管理、税金対策などについて、実用的で
バランスの取れたアドバイスを提供してください。ただし、具体的な
金融商品の推奨は控え、一般的な原則を説明してください。"""
    }
    
    system_message = system_messages.get(expert_type, "あなたは親切なアシスタントです。")
    
    try:
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.5,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=user_input)
        ]
        
        response = llm.invoke(messages)
        return response.content
    
    except Exception as e:
        return f"エラーが発生しました: {str(e)}\n\n環境変数 OPENAI_API_KEY が正しく設定されているか確認してください。"


st.subheader("👨‍⚕️ 専門家を選択")
expert_type = st.radio(
    "相談したい分野を選んでください:",
    ["健康の専門家", "資産運用の専門家"],
    index=0,
    horizontal=True
)

if expert_type == "健康の専門家":
    st.info("🏥 健康の専門家: 栄養、運動、メンタルヘルスなどについてアドバイスします")
else:
    st.info("💰 資産運用の専門家: 投資戦略、資産配分、リスク管理などについてアドバイスします")

st.subheader("✍️ 質問を入力")
user_input = st.text_area(
    "質問や相談内容を入力してください:",
    height=150,
    placeholder="例: 健康的な食生活を送るためのポイントを教えてください"
)

if st.button("🚀 回答を取得", type="primary", use_container_width=True):
    if user_input.strip():
        with st.spinner("AI が回答を生成中..."):
            response = get_llm_response(user_input, expert_type)
            
            st.subheader("💬 AI 専門家からの回答")
            st.markdown(f"**選択された専門家**: {expert_type}")
            st.divider()
            st.markdown(response)
            
            st.success("✅ 回答が生成されました！")
    else:
        st.warning("⚠️ 質問を入力してください。")

st.divider()
st.caption("💡 注意: AI の回答は参考情報です。重要な決定をする際は専門家に相談してください。")
