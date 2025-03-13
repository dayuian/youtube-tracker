# youtube_api.py
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_channel_id_by_handle(api_key: str, handle_or_name: str):
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        res = youtube.search().list(
            part="snippet",
            q=handle_or_name,
            type="channel",
            maxResults=1
        ).execute()

        if 'items' not in res or not res['items']:
            return None

        return res['items'][0]['snippet']['channelId']
    except Exception:
        return None


def get_channel_info(api_key: str, channel_id: str):
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        res = youtube.channels().list(
            part='snippet,statistics,brandingSettings',
            id=channel_id
        ).execute()

        if 'items' not in res or len(res['items']) == 0:
            return {"error": "找不到頻道資訊，請確認 ID 是否正確。"}, None

        item = res['items'][0]
        snippet = item['snippet']
        stats = item['statistics']
        branding = item.get('brandingSettings', {})

        return {
            "title": snippet.get('title'),
            "desc": snippet.get('description', ''),
            "thumbnail": snippet['thumbnails']['high']['url'],
            "view_count": int(stats['viewCount']),
            "video_count": int(stats['videoCount']),
            "country": snippet.get('country', '未知'),
            "published_at": snippet.get('publishedAt', ''),
            "custom_url": snippet.get('customUrl', ''),
            "banner_url": branding.get("image", {}).get("bannerExternalUrl", None)
        }, int(stats['subscriberCount'])

    except HttpError as e:
        err_content = e.content.decode()
        if "quotaExceeded" in err_content:
            return {"error": "API 配額已用盡，請明天再試或更換金鑰"}, None
        elif "keyInvalid" in err_content:
            return {"error": "無效的 API 金鑰或未啟用 YouTube API"}, None
        else:
            return {"error": f"API 錯誤：{e}"}, None
    except Exception as e:
        return {"error": f"未知錯誤：{e}"}, None
