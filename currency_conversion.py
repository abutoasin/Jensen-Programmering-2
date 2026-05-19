import requests

class ConversionRate:
    API_URL = "https://api.frankfurter.app/latest"

    @staticmethod
    def get_rate(from_currency, to_currency="SEK"):
        try:
            params = {"from": from_currency, "to": to_currency}
            response = requests.get(ConversionRate.API_URL, params=params)
            data = response.json()
            return data["rates"][to_currency]
        
        except Exception as e:
            print(f"Rate error: {e}")
            return None
