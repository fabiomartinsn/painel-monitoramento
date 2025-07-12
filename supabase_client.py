import requests

URL = "https://mjkwwobawarucinryfzf.supabase.co/rest/v1/produtividade"

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1qa3d3b2Jhd2FydWNpbnJ5ZnpmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE3NTAxNTAsImV4cCI6MjA2NzMyNjE1MH0.Ji_MI0kdWc0O-KoFGxs3gFGPE2Xo2CSCtkDl9djRGMo"

def obter_eventos_recentes():
    headers = {
        "apikey": API_KEY,
        "Authorization": f"Bearer {API_KEY}"
    }
    params = {
        "select": "*",
        "order": "timestamp.desc",
        "limit": "50"
    }
    response = requests.get(URL, headers=headers, params=params)
    return response.json()