class BMI:
    def __init__(self, weight, height):
        self.weight = weight  # Berat dalam kilogram
        self.height = height  # Tinggi dalam meter

    def BMI_Value(self):
        """
        Menghitung nilai BMI (Body Mass Index) menggunakan berat dan tinggi.
        Rumus BMI : berat / tinggi^2
        """
        return self.weight / (self.height ** 2)

    def __eq__(self, other):
        """
        Melakukan override terhadap metode equals untuk membandingkan berat dan tinggi dua objek BMI.
        """
        return self.weight == other.weight and self.height == other.height


# Contoh penggunaan:
if __name__ == "__main__":
    person1 = BMI(70, 1.75)  # Berat: 70 kg, Tinggi: 1.75 meter
    person2 = BMI(65, 1.70)  # Berat: 65 kg, Tinggi: 1.70 meter

    print("BMI untuk orang 1:", person1.BMI_Value())
    print("BMI untuk orang 2:", person2.BMI_Value())

    if person1 == person2:
        print("Orang 1 dan Orang 2 memiliki berat dan tinggi yang sama.")
    else:
        print("Orang 1 dan Orang 2 tidak memiliki berat dan tinggi yang sama.")
