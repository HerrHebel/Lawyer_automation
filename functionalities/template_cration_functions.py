from functionalities.authority_data_search import get_authority_address
from functionalities.CRM_scraping_scripts import crm_client_data_scrape
from functionalities.docx_functionalities import save_doc, save_envelope



def wniosek_o_przyznanie_świadczenia():
    list_of_context = []
    add_another_client = True
    while add_another_client:
        # Context inputs:
        client_gen_input = input("Enter client first letter of client's name and their surname in genitive:\n")
        client_dat_input = input("Enter client's full name and surname in dative:\n")
        client_relation_input = input("Enter client's relation to the disabled:\n")
        dis_cert_input = input("Does the disabled have a PZON disability certificate?:\n")
        disabled_name_input = input("Enter name and surname of the disabled:\n")
        pzon_city_input = input("Enter PZON/MZON/WZON location:\n")

        if dis_cert_input == "y":
            dis_cert_input = True

        motion_context = {
            "client_gen": client_gen_input,
            "client_dat": client_dat_input,
            "client_relation": client_relation_input,
            "dis_cert": dis_cert_input,
            "disabled_name": disabled_name_input,
            "pzon_city": pzon_city_input,
        }


        list_of_context.append(motion_context)

        print("Client data added successfully!")

        continue_input = input("Do you want to add another client? y or n:\n")
        if continue_input == "y":
            continue
        else:
            add_another_client = False

    for record in list_of_context:
        save_doc(template_path="docs/templates/wniosek_o_uzasadnienie.docx", context=record,
                 document_name="wniosek o uzasadnienie", saving_dir="docs/saved_files/wnioski o uzasadnienie/")
        save_envelope(context=record, addressee="WSA", operation_number=list_of_context.index(record) + 1,
                      saving_dir="docs/saved_files/envelopes/")