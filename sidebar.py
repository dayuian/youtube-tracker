# sidebar.py
import streamlit as st

def sidebar_inputs():
    with st.sidebar:
        st.header("🔧 設定")
        api_key = st.text_input("🔑 YouTube API 金鑰", type="password")
        channel_input = st.text_input("📺 頻道名稱或 @handle", placeholder="例如：@andy6023 或 Andy 老師")
        refresh_interval = st.slider("⏱️ 更新間隔（秒）", 5, 60, value=10)

        st.markdown("---")
        st.caption("📘 說明：")
        st.markdown("""
        - 到 [Google Cloud Console](https://console.cloud.google.com/) 申請 API 金鑰  
        - 輸入頻道名稱或 `@handle`，系統會自動解析  
        - 訂閱數支援跳動動畫 ✨
        """)
        st.markdown("---")
        st.caption("👨‍💻 開發者：余彦志（大宇/ian） | v1.2")

    return api_key, channel_input, refresh_interval
