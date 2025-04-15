import datetime
from app.errors import (NotWearingMaskError, NotVaccinatedError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict[str | str, int]) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        today = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < today:
            raise OutdatedVaccineError

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
