from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="별의 일주운동 시뮬레이터", layout="wide")

st.title("별의 일주운동 시뮬레이터")
st.caption("Three.js 기반 지구 자전·천구 회전·관측자 시점을 체험해 보세요.")

index_path = Path(__file__).parent / "simulator" / "index.html"
html_content = index_path.read_text(encoding="utf-8")

components.html(html_content, height=900, width="100%", scrolling=False)
