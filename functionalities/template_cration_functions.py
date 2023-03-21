from functionalities.authority_data_search import get_authority_address
from functionalities.CRM_scraping_scripts import crm_client_data_scrape
from functionalities.docx_functionalities import save_doc, save_envelope


def wniosek_o_uzasadnienie():
    list_of_context = []
    add_another_client = True
    while add_another_client:
        # Context inputs:
        crm_case_number_input = input("Enter CRM case number:\n")
        wsa_name_input = input("Enter WSA city:\n")
        sko_name_input = input("Enter SKO city:\n")
        wsa_case_number_input = input("Enter case number:\n")
        ruling_date_input = input("Enter ruling date:\n")

        uzas_context = {
            "crm_case_number": crm_case_number_input,
            "client_surname_name": "",
            "client_street_name_number": "",
            "client_zip_city": "",
            "wsa_name": wsa_name_input,
            "wsa_dat": "",
            "wsa_street_name_number ": "",
            "wsa_zip_city": "",
            "sko_name": sko_name_input,
            "sko_dat": "",
            "sko_street_name_number": "",
            "sko_zip_city": "",
            "case_number": wsa_case_number_input,
            "ruling_date": ruling_date_input,
        }

        get_authority_address(search_type="sko", context=uzas_context)
        get_authority_address(search_type="wsa", context=uzas_context)

        # queue and continue condition evaluation
        print(f"Client input no. {len(list_of_context) + 1}\n"
              f"CRM case number: {crm_case_number_input}\n"
              f"WSA: {uzas_context['wsa_name']}\n"
              f"SKO: {uzas_context['sko_name']}\n"
              f"WSA case number: {wsa_case_number_input}\n"
              f"Ruling date: {ruling_date_input}")

        list_of_context.append(uzas_context)

        print("Client data added successfully!")

        continue_input = input("Do you want to add another client? y or n:\n")
        if continue_input == "y":
            continue
        else:
            add_another_client = False

    for record in list_of_context:
        crm_client_data_scrape(context=record)
        save_doc(template_path="docs/templates/wniosek_o_uzasadnienie.docx", context=record,
                 document_name="wniosek o uzasadnienie", saving_dir="docs/saved_files/wnioski o uzasadnienie/")
        save_envelope(context=record, addressee="WSA", operation_number=list_of_context.index(record) + 1,
                      saving_dir="docs/saved_files/envelopes/")