import json

wsa_list = ["Białystok", "Bydgoszcz", "Gdańsk", "Gliwice", "Gorzów Wielkopolski", "Kielce", "Kraków", "Lublin", "Łódź",
            "Olsztyn", "Opole", "Poznań", "Rzeszów", "Szczecin", "Warszawa", "Wrocław", "NSA"]
sko_list = {
    "Białystok": ["Białystok", "Łomża", "Suwałki"],
    "Bydgoszcz": ["Bydgoszcz", "Toruń", "Włocławek"],
    "Gdańsk": ["Gdańsk", "Słupsk"],
    "Gliwice": ["Bielsko Biała", "Częstochowa", "Katowice"],
    "Gorzów Wielkopolski": ["Gorzów Wielkopolski", "Zielona Góra"],
    "Kielce": ["Kielce"],
    "Kraków": ["Nowy Sącz", "Kraków", "Tarnów"],
    "Lublin": ["Biała Podlaska", "Chełm", "Lublin", "Zamość"],
    "Łódź": ["Łódź", "Piotrków Trybunalski", "Sieradz", "Skierniewice"],
    "Olsztyn": ["Elbląg", "Olsztyn"],
    "Opole": ["Opole"],
    "Poznań": ["Kalisz", "Konin", "Leszno", "Piła", "Poznań"],
    "Rzeszów": ["Krosno", "Przemyśl", "Rzeszów", "Tarnobrzeg"],
    "Szczecin": ["Koszalin", "Szczecin"],
    "Warszawa": ["Ciechanów", "Ostrołęka", "Płock", "Radom", "Siedlce", "Warszawa"],
    "Wrocław": ["Jelenia Góra", "Legnica", "Wałbrzych", "Wrocław"],
    "NSA": []
}


def get_authority_address(search_type, context):
    """
    The function finds address data of appropriate authority.
    :param context: dict, Set of data to be used in docx document creation the function is going to write the output to.
    :return: dict, input dict with WSA address data saved into it
    """
    if search_type == "wsa":
        json_address_file_path = "authority_data/wsa_addresses.json"
        body_type = "wsa"
    elif search_type == "sko":
        json_address_file_path = "authority_data/sko_addresses.json"
        body_type = "sko"
    with open(json_address_file_path) as wsa_address_data:
        wsa_address_json = json.load(wsa_address_data)
        body_name = context[f"{body_type}_name"]
        context[f"{body_type}_dat"] = f"{wsa_address_json[body_name]['Dative']}"
        context[f"{body_type}_street_name_number"] = f"{wsa_address_json[body_name]['Street']} " \
                                            f"{wsa_address_json[body_name]['Building_number']}"
        context[f"{body_type}_zip_city"] = f"{wsa_address_json[body_name]['Zip_code']} " \
                                           f"{wsa_address_json[body_name]['City']}"
    return context
