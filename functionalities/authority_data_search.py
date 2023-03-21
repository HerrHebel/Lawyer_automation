import json


def get_authority_address(search_type, context):
    """
    The function finds address data of appropriate WSA.
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
        body_name_correct = False
        while not body_name_correct:
            try:
                body_name = context[f"{body_type}_name"]
                context[f"{body_type}_dat"] = f"{wsa_address_json[body_name]['Dative']}"
                context[f"{body_type}_street_name_number"] = f"{wsa_address_json[body_name]['Street']} " \
                                                    f"{wsa_address_json[body_name]['Building_number']}"
                context[f"{body_type}_zip_city"] = f"{wsa_address_json[body_name]['Zip_code']} " \
                                                   f"{wsa_address_json[body_name]['City']}"
                body_name_correct = True
            except KeyError:
                corrected_body_name = input(f"{body_type.upper()} in {body_name} "
                                            f"not found. Please enter correct WSA location.\n")
                context[f"{body_type}_name"] = corrected_body_name
    return context
