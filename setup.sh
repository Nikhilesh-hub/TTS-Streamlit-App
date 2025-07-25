mkdir -p ~/.streamlit/

echo "\
[general]\
" > ~/.streamlit/config.toml

echo "\
[server]\
headless = true\
enableCORS = false\
port = $PORT\
" >> ~/.streamlit/config.toml