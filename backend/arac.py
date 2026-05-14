"""
Arac sinifi.
"""


class Arac:
    """
    Araç paylaşım sistemindeki bir aracı temsil eder.

    Attributes:
        arac_id (int)
        marka (str)
        model (str)
        kilometre (int)
        musait_mi (bool)
        saatlik_ucret (float)
    """

    def __init__(self, arac_id: int, marka: str, model: str,
                 kilometre: int = 0, musait_mi: bool = True,
                 saatlik_ucret: float = 100.0):
        if not marka or not marka.strip():
            raise ValueError("Marka boş olamaz.")
        if not model or not model.strip():
            raise ValueError("Model boş olamaz.")
        if kilometre < 0:
            raise ValueError("Kilometre negatif olamaz.")
        if saatlik_ucret < 0:
            raise ValueError("Saatlik ücret negatif olamaz.")

        self.arac_id = arac_id
        self.marka = marka.strip()
        self.model = model.strip()
        self.kilometre = kilometre
        self.musait_mi = musait_mi
        self.saatlik_ucret = saatlik_ucret

    def arac_durumu_guncelle(self, yeni_durum: bool) -> None:
        self.musait_mi = yeni_durum

    def kilometre_guncelle(self, yeni_km: int) -> None:
        if yeni_km < 0:
            raise ValueError("Kilometre negatif olamaz.")
        self.kilometre = yeni_km

    def to_dict(self) -> dict:
        return {
            "arac_id": self.arac_id,
            "marka": self.marka,
            "model": self.model,
            "kilometre": self.kilometre,
            "musait_mi": self.musait_mi,
            "saatlik_ucret": self.saatlik_ucret,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Arac":
        return cls(
            arac_id=d["arac_id"],
            marka=d["marka"],
            model=d["model"],
            kilometre=d.get("kilometre", 0),
            musait_mi=d.get("musait_mi", True),
            saatlik_ucret=d.get("saatlik_ucret", 100.0),
        )

    def __repr__(self) -> str:
        durum = "müsait" if self.musait_mi else "kirada"
        return f"Arac(id={self.arac_id}, {self.marka} {self.model}, {durum})"
