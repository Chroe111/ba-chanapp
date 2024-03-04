import streamlit as st
import json
import random
import urllib

with open('word_data.json', mode='r') as f:
    word_json = json.load(f)

noun_list = word_json['名詞']
verb_list = word_json['動詞']
adj_list = word_json['形容詞']

tips = ''

st.title('エセおばあちゃんの知恵袋')
st.write('エセおばあちゃんがエセ雑学を披露してくれます。')
st.write('たまに文法がおかしいですが、おばあちゃんなので許してあげてください。')
st.write('↓ボタンを押して生成')

if st.button('教えて、おばあちゃん！'):
    tips = f'{random.choice(noun_list)}を{random.choice(verb_list)}と{random.choice(adj_list)}んじゃよ'
    with st.chat_message('おばあちゃん', avatar='👵'):
        st.write(tips)
    url = 'https://ba-chanapp.streamlit.app/'
    text = tips + f'\n\n#エセおばあちゃんの知恵袋\n{url}'
    st.link_button('ツイート', f'https://twitter.com/intent/tweet?text={urllib.parse.quote(text)}')
else:
    with st.chat_message('おばあちゃん', avatar='👵'):
        st.write('わしはなんでも知ってるぞい')