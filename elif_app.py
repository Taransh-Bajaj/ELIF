import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# 1. Setup
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="ELIF Simplifier", page_icon="👶")

# 2. Styling the UI
st.title("👶 ELIF: The Simplifier")
st.markdown("### Paste a huge paragraph. Get the simple truth.")

# 3. Input Section
huge_para = st.text_area("Paste your big text here...", height=300, placeholder="Example: Quantum entanglement is a physical phenomenon that occurs when a group of particles...")

# 4. The Logic
if st.button("Simplify Now! ✨"):
    if huge_para:
        with st.spinner("Breaking down big words..."):
            try:
                # This prompt forces the AI to stick to your exact rules
                prompt = (
                    "You are an expert at explaining complex things to a 5-year-old. "
                    "Read the following text and provide:\n"
                    "1. Exactly 5 bullet points of the most important facts in very simple language.\n"
                    "2. One simple analogy that anyone can understand.\n"
                    "Do not use big words. Be friendly."
                )

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": prompt},
                        {"role": "user", "content": huge_para}
                    ]
                )

                # 5. Display the Results
                st.markdown("---")
                st.success("### Here is what it means:")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please paste some text first!")

# Sidebar instructions
st.sidebar.markdown("""
**How to use:**
1. Copy a hard paragraph from a textbook or news.
2. Paste it in the box.
3. Hit the button.
""")