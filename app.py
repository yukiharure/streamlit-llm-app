from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI    
from langchain.prompts import (
    ChatPromptTemplate,           
    SystemMessagePromptTemplate,  
    HumanMessagePromptTemplate,   
)

st.title("専門家LLM_Webアプリ")
st.write("##### 専門家①: 栄養士")
st.write("栄養学に基づくアドバイスを得ることができます。")
st.write("##### 専門家②: フィットネストレーナー")
st.write("トレーニング理論に基づくアドバイスを得ることができます。")
st.write("##### 専門家③: 医師")
st.write("医学に基づくアドバイスを得ることができます。")

selected_item = st.radio(
    "質問したい専門家を選んでください",
    ["栄養士", "フィットネストレーナー", "医師"]
)
st.divider()

# ユーザーの質問入力を先に取得
input_message = st.text_input(label="相談内容を入力してください。")

system_template = "あなたは、{genre}に詳しいAIです。質問に対して回答してください。"
human_template = "{question}"

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template),
])

if selected_item == "栄養士":
    messages = prompt.format_prompt(genre="栄養学", question=input_message).to_messages()
elif selected_item == "フィットネストレーナー":
    messages = prompt.format_prompt(genre="トレーニング理論", question=input_message).to_messages()
elif selected_item == "医師":
    messages = prompt.format_prompt(genre="医学", question=input_message).to_messages()

if st.button("実行"):
    if not input_message:
        st.warning("相談内容を入力してください。")
    else:
        with st.spinner("回答を取得中..."):
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            result = llm(messages)
        st.write(result.content)
