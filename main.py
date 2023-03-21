from functionalities.template_cration_functions import wniosek_o_uzasadnienie


operation_type = input("Welcome to Layer automator. Please choose operation type:\n 1. Wniosek o uzasadnienie "
                       "wyroku\n 2. Wnioski o przyznanie świadczenia pielęgnacyjnego\n")

# Wniosek o uzasadnienie
if operation_type == "1":
    wniosek_o_uzasadnienie()
