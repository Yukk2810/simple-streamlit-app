import openai
import streamlit as st

# この行を追加することでLangCoreでログを残すことができます
openai.api_base = "https://oai.langcore.org/v1"

# Streamlitアプリケーションの外観をカスタマイズします
st.set_page_config(
    page_title="ボトルネック見つけるくん☆彡",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="auto",
)

# 背景色を白に変更
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    st.title("ボトルネック見つけるくん☆彡")
    
    # マテリアルデザインのテキスト入力フィールドを使って、ユーザーに課題を入力させます
    user_input = st.text_input("課題や悩んでいる内容を入力してください: ")
    
    # マテリアルデザインのボタンを使って、ボトルネックを調べるアクションをトリガーします
    if st.button("ボトルネックを調べる"):
        catchphrase = call_chatgpt_api(user_input)
        st.write("考えられるボトルネック: ", catchphrase)
    
    # エラーメッセージのスペースを追加します
    st.text("")

def call_chatgpt_api(input_text):
    try:
        prompt = f"""あなたは経営戦略に秀でた製造エンジニアで、データドリブンの思考を持っています。次の内容からボトルネックを考えてください。
内容: {input_text}
"""
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=100,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"エラー: ボトルネックは分かりませんでした。{str(e)}"

if __name__ == "__main__":
    main()
