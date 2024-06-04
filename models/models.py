from pydantic import BaseModel, field_validator, Field
from datetime import datetime
from typing import List


class Persoon(BaseModel):
  gemeente: str = Field(description="De gemeente waar de persoon woont")
  naam: str = Field(description="De naam van de persoon")
  geslacht: bool = Field(description="Het geslacht van de persoon (Mannelijk/Vrouwelijk)")
  verwachte_datum: datetime = Field(description="De verwachte datum in de vorm 'MM/DD/JJJJ'")

class Data(BaseModel):
  personen: List[Persoon] = Field(description="Lijst met personen")

@field_validator('verwachte_datum', mode='before')
def parse_date(cls, value):
    return datetime.strptime(value, '%m-%d-%Y')
    
@field_validator('geslacht', mode='before')
def convert_to_bool(cls, value):
    if value.lower() == "vrouwelijk":
        return True
    return False
    
