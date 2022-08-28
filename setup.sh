mkdir -p ~/.streamlit/
echo "[theme]
primaryColor=’#575fe8’
backgroundColor=’#f5f7f3’
secondaryBackgroundColor=’#c9eab8’
font = ‘sans serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
