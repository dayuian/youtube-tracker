# main.py
import streamlit as st
import time
from datetime import datetime

from youtube_api import get_channel_id_by_handle, get_channel_info
from sidebar import sidebar_inputs
from visual import odometer_component

# 頁面設定
st.set_page_config("YouTube 訂閱追蹤", page_icon="📺", layout="centered")

# 自訂樣式
st.markdown("""
    <style>
    .st-emotion-cache-1kyxreq { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# 取得側欄參數
api_key, channel_input, refresh_interval = sidebar_inputs()

st.title("📈 YouTube 訂閱即時追蹤")

if api_key and channel_input:
    st.info("🔍 嘗試解析頻道資訊中...")
    channel_id = get_channel_id_by_handle(api_key, channel_input)

    if not channel_id:
        st.error("❌ 無法找到該頻道，請確認輸入名稱或 @handle 是否正確。")
    else:
        with st.spinner("📡 正在取得頻道資料..."):
            info, subs = get_channel_info(api_key, channel_id)

        if info and "error" not in info:
            # 橫幅圖
            if info.get("banner_url"):
                st.image(info["banner_url"], use_container_width=True)

            # 頻道資訊
            st.markdown("## 🎬 頻道資訊")
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(info["thumbnail"], width=100)
            with col2:
                st.markdown(f"**名稱：** `{info['title']}`")
                st.markdown(f"📹 **影片數：** `{info['video_count']:,}`　👁️ **觀看數：** `{info['view_count']:,}`")

                if info.get("custom_url"):
                    st.markdown(f"🔗 [youtube.com/{info['custom_url']}](https://www.youtube.com/{info['custom_url']})")

                st.markdown(f"📍 國家：`{info.get('country', '未知')}`")

                if info.get("published_at"):
                    dt = datetime.fromisoformat(info["published_at"].replace("Z", "+00:00"))
                    st.markdown(f"📅 創立時間：`{dt.strftime('%Y-%m-%d')}`")

            if info["desc"]:
                st.markdown(f"📝 `{info['desc'][:120]}...`")

            st.divider()

            # 訂閱區塊
            st.markdown("## 📊 即時訂閱人數")
            sub_placeholder = st.empty()
            prev_subs = subs

            while True:
                info, new_subs = get_channel_info(api_key, channel_id)

                # 錯誤處理：API 爆掉或 quota 滿
                if info and "error" in info:
                    with sub_placeholder.container():
                        st.error(f"❌ 訂閱資料更新失敗：{info['error']}")
                    st.stop()

                if new_subs is not None:
                    with sub_placeholder.container():
                        odometer_component(new_subs)
                        st.caption(f"更新時間：{time.strftime('%H:%M:%S')}")
                    prev_subs = new_subs

                time.sleep(refresh_interval)
        else:
            st.error(f"❌ 無法取得頻道資訊：{info['error']}")
else:
    st.info("請在側欄輸入 API 金鑰與頻道名稱 / @handle 後開始。")
