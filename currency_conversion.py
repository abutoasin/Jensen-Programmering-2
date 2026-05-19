import requests

class ConversionRate:
    API_URL = "https://api.exchangerate.host/convert"

    @staticmethod
    def get_rate(from_currency, to_currency="SEK"):
        try:
            params = {"from": from_currency, "to": to_currency}
            response = requests.get(ConversionRate.API_URL, params=params)
            data = response.json()
            return data["info"]["rate"]
        
        except Exception as e:
            print(f"Rate error: {e}")
            return None
