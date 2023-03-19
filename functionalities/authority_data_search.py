import json


def get_wsa_address(context):
    """
    The function finds address data of appropriate WSA.
    :param context: dict, Set of data to be used in docx document creation the function is going to write the output to.
    :return: dict, input dict with WSA address data saved into it
    """
    # WSA address search
    with open("authority_data/wsa_addresses.json") as wsa_address_data:
        body_name = context["wsa_name"]
        wsa_address_json = json.load(wsa_address_data)
        context["wsa_dat"] = f"{wsa_address_json[body_name]['Dative']}"
        context[
            "wsa_street_name_number"] = f"{wsa_address_json[body_name]['Street']} {wsa_address_json[body_name]['Building_number']}"
        context["wsa_zip_city"] = f"{wsa_address_json[body_name]['Zip_code']} {wsa_address_json[body_name]['City']}"
    return context


def get_sko_address(context):
    """
    The function finds address data of appropriate SKO.
    :param context: dict, Set of data to be used in docx document creation the function is going to write the output to.
    :return: dict, input dict with WSA address data saved into it
    """
    with open("authority_data/sko_addresses.json") as sko_address_data:
        body_name = context["sko_name"]
        sko_address_json = json.load(sko_address_data)
        context["sko_dat"] = f"{sko_address_json[body_name]['Dative']}"
        context[
            "sko_street_name_number"] = f"{sko_address_json[body_name]['Street']} {sko_address_json[body_name]['Building_number']}"
        context["sko_zip_city"] = f"{sko_address_json[body_name]['Zip_code']} {sko_address_json[body_name]['City']}"
    return context