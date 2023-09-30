import openai
import streamlit as st

# この行を追加することでLangCoreでログを残すことができます
openai.api_base = "https://oai.langcore.org/v1"

def main():
    st.title("ボトルネック見つけるくん☆彡")
    user_input = st.text_input("課題や悩んでいる内容を入力してください: ")
    if st.button("ボトルネックを調べる"):
        catchphrase = call_chatgpt_api(user_input)
        st.write("考えられるボトルネック: ", catchphrase)


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
