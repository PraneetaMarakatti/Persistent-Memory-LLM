import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="AI Memory Assistant",
    layout="wide"
)

st.title("🧠 AI Assistant with Memory")


# -------------------------
# Chat History
# -------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# show old messages

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])



# -------------------------
# User Input
# -------------------------

user_input = st.chat_input("Ask something or tell me something...")


if user_input:

    # show user message

    st.chat_message("user").write(user_input)

    st.session_state.messages.append(

        {"role":"user","content":user_input}
    )



    # -------------------------
    # Store memory
    # -------------------------

    try:

        requests.post(

            f"{API_URL}/memories",

            json={"text":user_input}

        )

    except Exception as e:

        st.error("Memory store failed")


    # -------------------------
    # Ask AI
    # -------------------------

    try:

        response = requests.get(

            f"{API_URL}/memories/search",

            params={"q":user_input}

        )

        data = response.json()

        answer = data["answer"]


    except Exception as e:

        answer = "Backend not reachable."


    # show AI response

    with st.chat_message("assistant"):

        st.write(answer)


    st.session_state.messages.append(

        {"role":"assistant","content":answer}
    )



# -------------------------
# Sidebar Memories
# -------------------------

st.sidebar.header("Stored Memories")


if st.sidebar.button("Refresh"):

    pass


try:

    memories = requests.get(

        f"{API_URL}/memories"

    ).json()


    for mem in memories:

        col1,col2 = st.sidebar.columns([3,1])

        col1.write(mem["memory"])

        if col2.button(

            "❌",

            key=mem["id"]

        ):

            requests.delete(

                f"{API_URL}/memories/{mem['id']}"

            )

            st.rerun()


except:

    st.sidebar.write("Backend offline")
