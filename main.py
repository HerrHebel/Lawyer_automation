from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QLineEdit, QFormLayout, QComboBox, QProgressBar
from functionalities.CRM_scraping_scripts import crm_client_data_scrape
from functionalities.authority_data_search import get_authority_address, wsa_list, sko_list
from functionalities.docx_functionalities import save_doc, save_envelope
import sys


class Uzasadnienie(QWidget):
    def __init__(self):
        super().__init__()
        self.uzas_context = {}
        self.list_of_context = []
        self.setWindowTitle("Wniosek o uzasadnienie wyroku")

        # Form setup
        self.crm_case_number_label = QLabel("CRM case number: ")
        self.crm_case_number_input = QLineEdit()

        self.wsa_name_label = QLabel("WSA name: ")
        self.wsa_name_input = QComboBox()
        self.wsa_name_input.insertItems(0, wsa_list)

        self.sko_name_label = QLabel("SKO name: ")
        self.sko_name_input = QComboBox()
        self.sko_name_input.insertItems(0, sko_list[self.wsa_name_input.currentText()])
        self.wsa_name_input.currentIndexChanged.connect(self.update_sko_list)

        self.wsa_case_number_label = QLabel("WSA case number: ")
        self.wsa_case_number_input = QLineEdit()

        self.wsa_ruling_date_label = QLabel("Ruling date: ")
        self.wsa_ruling_date_input = QLineEdit()

        # Cases provided
        self.cases_provided_label = QLabel()

        # Button setup
        confirm_button = QPushButton("Add case to the list")
        confirm_button.clicked.connect(self.save_inputs)
        confirm_button.clicked.connect(lambda: get_authority_address(search_type="sko", context=self.uzas_context))
        confirm_button.clicked.connect(lambda: get_authority_address(search_type="wsa", context=self.uzas_context))
        confirm_button.clicked.connect(self.add_case)

        action_button = QPushButton("Generate docs")
        action_button.clicked.connect(self.execute)

        # Progress bar
        self.prog_bar = QProgressBar()

        self.prog_bar.setRange(0, 10)

        # Layout setup
        input_layout = QFormLayout()

        input_layout.addRow(self.crm_case_number_label, self.crm_case_number_input)
        input_layout.addRow(self.wsa_name_label, self.wsa_name_input)
        input_layout.addRow(self.sko_name_label, self.sko_name_input)
        input_layout.addRow(self.wsa_case_number_label, self.wsa_case_number_input)
        input_layout.addRow(self.wsa_ruling_date_label, self.wsa_ruling_date_input)
        input_layout.addRow(self.cases_provided_label)
        input_layout.addRow(confirm_button)
        input_layout.addRow(action_button)
        input_layout.addRow(self.prog_bar)

        self.setLayout(input_layout)

    def update_sko_list(self):
        self.sko_name_input.clear()
        self.sko_name_input.insertItems(0, sko_list[self.wsa_name_input.currentText()])

    def add_case(self):
        print(self.uzas_context)
        self.list_of_context.append(self.uzas_context)
        self.crm_case_number_input.clear()
        self.wsa_case_number_input.clear()
        self.wsa_ruling_date_input.clear()
        self.uzas_context = {}
        self.cases_provided_label.setText(f"Cases provided: {len(self.list_of_context)}")
        print("Item added")

    def save_inputs(self):
        self.uzas_context["crm_case_number"] = self.crm_case_number_input.text()
        self.uzas_context["wsa_name"] = self.wsa_name_input.currentText()
        self.uzas_context["sko_name"] = self.sko_name_input.currentText()
        self.uzas_context["case_number"] = self.wsa_case_number_input.text()
        self.uzas_context["ruling_date"] = self.wsa_ruling_date_input.text()
        print(self.uzas_context)

    def execute(self):
        progress = 0
        crm_client_data_scrape(self.list_of_context)
        for record in self.list_of_context:
            save_doc(template_path="docs/templates/wniosek_o_uzasadnienie.docx", context=record,
                     document_name="wniosek o uzasadnienie", saving_dir="docs/saved_files/wnioski o uzasadnienie/")
            save_envelope(context=record, addressee="WSA", operation_number=self.list_of_context.index(record) + 1,
                          saving_dir="docs/saved_files/envelopes/")
            progress += 1
            # self.prog_bar.setValue(progress)
        print(self.list_of_context)
        self.list_of_context = []


app = QApplication(sys.argv)
window = Uzasadnienie()
window.show()

app.exec()
