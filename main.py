from pyscript import display, document 

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "F": ("Fluorine", 9, 18.998),
    "Cl": ("Chlorine", 17, 35.45),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.90)
}


def search_element(e):
    document.getElementById('result').innerHTML = ""

    element1 = document.getElementById('element').value.strip().title()

    # Using .get() - no if statement
    element, atomic_number, atomic_mass = non_metals.get(
        element1,
        ("Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {element1}<br>
    <b>Element:</b> {element}<br>
    <b>Atomic Number:</b> {atomic_number}<br>
    <b>Atomic Mass:</b> {atomic_mass}
    """
