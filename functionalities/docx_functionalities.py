from docxtpl import DocxTemplate


def save_envelope(context, addressee, operation_number, saving_dir):
    """
    The function saves envelope with proper addressee data.
    :param context: dict, Set of data to be used in docx document creation the function is going get appropriate data from.
    :param addressee: str, Authority to which the letter is to be sent.
    :param operation_number: int, item's list number for saving multiple envelopes addressed to the same body.
    :param saving_dir: str, path to the folder file is to be saved to.
    :return: .docx file, saved envelope
    """
    addressee_city = context["wsa_name"]
    envelope = DocxTemplate("docs/templates/Koperta_C5.docx")
    envelope.render(context)
    envelope_file_name = f"Koperta {addressee} {addressee_city} - {operation_number}.docx"
    envelope.save(saving_dir + envelope_file_name)


def save_doc(template_path, context, document_name, saving_dir):
    """
    The function saves the new document from docx template.
    :param template_path: str, path to template from which new document shall be created
    :param context: dict, Set of data to be used in docx document creation.
    :param document_name: str, the name the new file should be saved as.
    :param saving_dir: str, path to the folder file is to be saved to.
    :return: .docx file, saved document
    """
    document = DocxTemplate(f"{template_path}")
    document.render(context)
    document_file_name = f"{context['client_surname_name'].upper()} - {document_name}.docx"
    document.save(saving_dir + document_file_name)