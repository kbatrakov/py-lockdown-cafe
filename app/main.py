from __future__ import annotations
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    masks_to_buy = sum(not friend["wearing_a_mask"] for friend in friends)

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            return f"Friends should buy {masks_to_buy} masks"

        else:
            return f"Friends can go to {cafe.name}"
