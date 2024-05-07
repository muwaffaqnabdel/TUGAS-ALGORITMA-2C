def hitung_BMI(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def rekomendasi_BMI(bmi):
    if bmi < 18.5:
        return "Berat badan kurang. Anda disarankan untuk meningkatkan asupan makanan dan berkonsultasi dengan ahli gizi."
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal. Pertahankan pola makan sehat dan rutin berolahraga."
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan. Anda disarankan untuk mengurangi asupan kalori dan meningkatkan aktivitas fisik."
    else:
        return "Obesitas. Segera konsultasikan dengan dokter atau ahli gizi untuk program penurunan berat badan yang sesuai."
berat_badan = float(input("masukkan berat badan (kg): "))
tinggi_badan = float(input("masukkan tinggi badan (cm): "))
def hitung_BMI(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def rekomendasi_BMI(bmi):
    if bmi < 18.5:
        return "Berat badan kurang. Anda disarankan untuk meningkatkan asupan makanan dan berkonsultasi dengan ahli gizi."
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal. Pertahankan pola makan sehat dan rutin berolahraga."
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan. Anda disarankan untuk mengurangi asupan kalori dan meningkatkan aktivitas fisik."
    else:
        return "Obesitas. Segera konsultasikan dengan dokter atau ahli gizi untuk program penurunan berat badan yang sesuai."