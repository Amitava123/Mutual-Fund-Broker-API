import requests
from app.config.settings import settings

class RapidAPIService:
    @staticmethod
    def get_nav(mf_name: str):
        url = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"
        headers = {
            "x-rapidapi-key": settings.RAPIDAPI_KEY,
            "x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-rapidapi-ua": "RapidAPI-Playground"
        }
        params = {
            "Scheme_Type": "Open"
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            raise ValueError(f"Error fetching data from RapidAPI: {response.status_code}")
        
        schemes = response.json()
        
        # Extract the NAV for each scheme
        result = []
        for scheme in schemes:
            scheme_data = {
                "Scheme_Name": scheme.get("Scheme_Name"),
                "Net_Asset_Value": scheme.get("Net_Asset_Value"),
            }
            result.append(scheme_data)
        
        return result
