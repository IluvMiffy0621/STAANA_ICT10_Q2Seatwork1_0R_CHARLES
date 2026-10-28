"""ICT Club candidate verification system (ICT 10 Seatwork #1)."""

from pyscript import document, when

# List of club members (stored in Title Case so lookups match cleaned input)
CLUB_MEMBERS = [
    "Carlo Villanueva",
    "Denise Bautista",
    "Rafael Aquino",
    "Katrina Navarro",
    "Gabriel Ramos",
    "Isabel Castillo",
    "Nathan Flores",
    "Chloe Domingo",
]


def get_inputs():
    """Read the first and last name typed by the user."""
    # Value of the First Name field
    first_name = document.querySelector("#first-name").value
    # Value of the Last Name field
    last_name = document.querySelector("#last-name").value
    return first_name, last_name


def build_full_name(first_name, last_name):
    """Combine both names into one cleaned, Title Case full name."""
    # Join the names, then collapse extra spaces and fix capitalization
    full_name = " ".join(f"{first_name} {last_name}".split()).title()
    return full_name


def check_membership(full_name):
    """Return True if the full name is in the club members list."""
    # The "in" operator already gives True or False, so no if-statement needed
    is_member = full_name in CLUB_MEMBERS
    return is_member


def get_message(full_name, is_member):
    """Pick the right message using the True/False result as a dictionary key."""
    # Each possible result maps to its message
    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list.",
    }
    return messages[is_member]


def display_result(message):
    """Show the message in the result area."""
    # The result area element on the page
    result_area = document.querySelector("#result")
    result_area.innerText = message


@when("click", "#check-button")
def handle_click(event):
    """Respond to the button click: get input, check the list, show result."""
    first_name, last_name = get_inputs()
    full_name = build_full_name(first_name, last_name)
    is_member = check_membership(full_name)
    message = get_message(full_name, is_member)
    display_result(message)
