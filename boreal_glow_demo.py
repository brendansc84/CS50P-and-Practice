# 💖 Survey mark pink — comments should be pink

import math  # keyword/import should be orange

GAS_PRESSURE_PSI = 60          # variable/constant → gas line yellow
waterline_label = "H2O MAIN"   # strings → waterline blue
underground_cable_depth = 0.9  # numbers → lime green
safety_vest_on = True          # keywords (True/False) → orange

def locate_flag(color: str) -> str:  # function name → underground cable red
    """Return a lil' flag for the given utility color."""
    return f"[{color}]"

class BorealSurveyorGlow:
    def __init__(self, crew_size: int):
        self.crew_size = crew_size  # variable/attribute → gas line yellow

    def stake(self, station: float) -> str:
        note = f"Stake at {station:.2f}m — crew: {self.crew_size}"
        return note

# --- Demo logic to show tokens in context ---
def demo():
    # numbers (ints, floats, hex) should glow lime
    hex_sample = 0xFF
    radius = 3.14

    # strings (blue), variables (yellow), functions (red)
    msg = (
        locate_flag("WATER") + " "
        + locate_flag("GAS") + " "
        + locate_flag("POWER")
    )

    # keywords like if/else/for/return/try/except → orange
    if safety_vest_on and GAS_PRESSURE_PSI >= 60:
        surveyor = BorealSurveyorGlow(crew_size=3)
        stations = [10, 12.5, 15.75]
        notes = [surveyor.stake(s) for s in stations]  # list comp uses many tokens
    else:
        notes = ["No work without PPE."]

    try:
        area = math.pi * (radius ** 2)  # ** shows operator/numbers nicely
    except Exception as err:
        area = float("nan")
        notes.append(f"⚠️ Error: {err}")

    # f-strings (blue), variables (yellow), numbers (lime), functions (red)
    print(
        f"{msg}\n"
        f"Waterline: {waterline_label} | Cable depth: {underground_cable_depth}m\n"
        f"Area calc: {area:.3f} | Hex sample: {hex_sample}\n"
        f"Notes:\n- " + "\n- ".join(notes)
    )

if __name__ == "__main__":  # keywords → orange
    demo()                   # function call → red
