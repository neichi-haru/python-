import cv2

a_1 = cv2.VideoCapture('/Users/neichiharu/Desktop/Y2meta.app-1分で自己紹介-(1080p).mp4')
print(type(a_1))

print(a_1.isOpened())

from langchain_community.document_loaders import YoutubeLoader


YOUTUBE_URL = "https://www.youtube.com/watch?v=B7Ok1fDawfQ"

# youtube-transcript-apiで文字起こし ====================================
loader = YoutubeLoader.from_youtube_url(
    YOUTUBE_URL ,          # 取得したいYouTube URL
    add_video_info=False, # 動画情報を取得する場合はTrue
    language=["ja"],      # 取得する字幕の言語指定(複数指定は取得の優先順位づけ)
    translation="ja",     # 字幕を自動翻訳したい場合の言語指定
)
documents = loader.load()
content = documents[0].page_content # 文字起こし出力
print(content)
