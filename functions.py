import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import json

is_number_valid = None
is_possible_number = None
number_type = None
isp = None

class Phone:
    phonenumber = None
    country_code = None
    area_code = None
    line_number = None

    def __init__(self):
        pass

    def set_phone_number(self, phone_number):
        self.phonenumber = phone_number

        return self.phonenumber

    def set_country_code(self, country):
        country_codes = {
            'Afghanistan': +93, 'Albania': +355, 'Algeria': +213, 'Andorra': +376, 'Angola': +244,
            'Argentina': +54, 'Armenia': +374, 'Australia': +61, 'Austria': +43, 'Azerbaijan': +994,
            'Bahrain': +973, 'Bangladesh': +880, 'Belarus': +375, 'Belgium': +32, 'Belize': +501,
            'Benin': +229, 'Bhutan': +975, 'Bolivia': +591, 'Bosnia and Herzegovina': +387, 'Botswana': +267,
            'Brazil': +55, 'Brunei': +673, 'Bulgaria': +359, 'Burkina Faso': +226, 'Burundi': +257,
            'Cambodia': +855, 'Cameroon': +237, 'Canada': +1, 'Central African Republic': +236, 'Chad': +235,
            'Chile': +56, 'China': +86, 'Colombia': +57, 'Comoros': +269, 'Congo': +242,
            'Costa Rica': +506, 'Croatia': +385, 'Cuba': +53, 'Cyprus': +357, 'Czech Republic': +420,
            'Denmark': +45, 'Djibouti': +253, 'Dominican Republic': +1, 'Ecuador': +593, 'Egypt': +20,
            'El Salvador': +503, 'Equatorial Guinea': +240, 'Eritrea': +291, 'Estonia': +372, 'Ethiopia': +251,
            'Fiji': +679, 'Finland': +358, 'France': +33, 'Gabon': +241, 'Gambia': +220,
            'Georgia': +995, 'Germany': +49, 'Ghana': +233, 'Greece': +30, 'Grenada': +1,
            'Guatemala': +502, 'Guinea': +224, 'Guinea-Bissau': +245, 'Guyana': +592, 'Haiti': +509,
            'Honduras': +504, 'Hungary': +36, 'Iceland': +354, 'India': +91, 'Indonesia': +62,
            'Iran': +98, 'Iraq': +964, 'Ireland': +353, 'Israel': +972, 'Italy': +39,
            'Jamaica': +1, 'Japan': +81, 'Jordan': +962, 'Kazakhstan': +7, 'Kenya': +254,
            'Kuwait': +965, 'Kyrgyzstan': +996, 'Laos': +856, 'Latvia': +371, 'Lebanon': +961,
            'Lesotho': +266, 'Liberia': +231, 'Libya': +218, 'Liechtenstein': +423, 'Lithuania': +370,
            'Luxembourg': +352, 'Madagascar': +261, 'Malawi': +265, 'Malaysia': +60, 'Maldives': +960,
            'Mali': +223, 'Malta': +356, 'Mauritania': +222, 'Mauritius': +230, 'Mexico': +52,
            'Moldova': +373, 'Monaco': +377, 'Mongolia': +976, 'Montenegro': +382, 'Morocco': +212,
            'Mozambique': +258, 'Myanmar': +95, 'Namibia': +264, 'Nepal': +977, 'Netherlands': +31,
            'New Zealand': +64, 'Nicaragua': +505, 'Niger': +227, 'Nigeria': +234, 'North Korea': +850,
            'North Macedonia': +389, 'Norway': +47, 'Oman': +968, 'Pakistan': +92, 'Panama': +507,
            'Papua New Guinea': +675, 'Paraguay': +595, 'Peru': +51, 'Philippines': +63, 'Poland': +48,
            'Portugal': +351, 'Qatar': +974, 'Romania': +40, 'Russia': +7, 'Rwanda': +250,
            'Saudi Arabia': +966, 'Senegal': +221, 'Serbia': +381, 'Sierra Leone': +232, 'Singapore': +65,
            'Slovakia': +421, 'Slovenia': +386, 'Somalia': +252, 'South Africa': +27, 'South Korea': +82,
            'South Sudan': +211, 'Spain': +34, 'Sri Lanka': +94, 'Sudan': +249, 'Sweden': +46,
            'Switzerland': +41, 'Syria': +963, 'Taiwan': +886, 'Tajikistan': +992, 'Tanzania': +255,
            'Thailand': +66, 'Togo': +228, 'Trinidad and Tobago': +1, 'Tunisia': +216, 'Turkey': +90,
            'Turkmenistan': +993, 'Uganda': +256, 'Ukraine': +380, 'United Arab Emirates': +971,
            'United Kingdom': +44, 'United States': +1, 'Uruguay': +598, 'Uzbekistan': +998,
            'Vatican City': +39, 'Venezuela': +58, 'Vietnam': +84, 'Yemen': +967, 'Zambia': +260,
            'Zimbabwe': +263
        }
        country_shortcodes = {
            'AF': +93, 'AL': +355, 'DZ': +213, 'AD': +376, 'AO': +244,
            'AR': +54, 'AM': +374, 'AU': +61, 'AT': +43, 'AZ': +994,
            'BH': +973, 'BD': +880, 'BY': +375, 'BE': +32, 'BZ': +501,
            'BJ': +229, 'BT': +975, 'BO': +591, 'BA': +387, 'BW': +267,
            'BR': +55, 'BN': +673, 'BG': +359, 'BF': +226, 'BI': +257,
            'KH': +855, 'CM': +237, 'CA': +1, 'CF': +236, 'TD': +235,
            'CL': +56, 'CN': +86, 'CO': +57, 'KM': +269, 'CG': +242,
            'CR': +506, 'HR': +385, 'CU': +53, 'CY': +357, 'CZ': +420,
            'DK': +45, 'DJ': +253, 'DO': +1, 'EC': +593, 'EG': +20,
            'SV': +503, 'GQ': +240, 'ER': +291, 'EE': +372, 'ET': +251,
            'FJ': +679, 'FI': +358, 'FR': +33, 'GA': +241, 'GM': +220,
            'GE': +995, 'DE': +49, 'GH': +233, 'GR': +30, 'GD': +1,
            'GT': +502, 'GN': +224, 'GW': +245, 'GY': +592, 'HT': +509,
            'HN': +504, 'HU': +36, 'IS': +354, 'IN': +91, 'ID': +62,
            'IR': +98, 'IQ': +964, 'IE': +353, 'IL': +972, 'IT': +39,
            'JM': +1, 'JP': +81, 'JO': +962, 'KZ': +7, 'KE': +254,
            'KW': +965, 'KG': +996, 'LA': +856, 'LV': +371, 'LB': +961,
            'LS': +266, 'LR': +231, 'LY': +218, 'LI': +423, 'LT': +370,
            'LU': +352, 'MG': +261, 'MW': +265, 'MY': +60, 'MV': +960,
            'ML': +223, 'MT': +356, 'MR': +222, 'MU': +230, 'MX': +52,
            'MD': +373, 'MC': +377, 'MN': +976, 'ME': +382, 'MA': +212,
            'MZ': +258, 'MM': +95, 'NA': +264, 'NP': +977, 'NL': +31,
            'NZ': +64, 'NI': +505, 'NE': +227, 'NG': +234, 'KP': +850,
            'MK': +389, 'NO': +47, 'OM': +968, 'PK': +92, 'PA': +507,
            'PG': +675, 'PY': +595, 'PE': +51, 'PH': +63, 'PL': +48,
            'PT': +351, 'QA': +974, 'RO': +40, 'RU': +7, 'RW': +250,
            'SA': +966, 'SN': +221, 'RS': +381, 'SL': +232, 'SG': +65,
            'SK': +421, 'SI': +386, 'SO': +252, 'ZA': +27, 'KR': +82,
            'SS': +211, 'ES': +34, 'LK': +94, 'SD': +249, 'SE': +46,
            'CH': +41, 'SY': +963, 'TW': +886, 'TJ': +992, 'TZ': +255,
            'TH': +66, 'TG': +228, 'TT': +1, 'TN': +216, 'TR': +90,
            'TM': +993, 'UG': +256, 'UA': +380, 'AE': +971,
            'GB': +44, 'US': +1, 'UY': +598, 'UZ': +998,
            'VA': +39, 'VE': +58, 'VN': +84, 'YE': +967, 'ZM': +260,
            'ZW': +263
        }
        self.country_code = country_codes.get(country) or country_shortcodes.get(country)

        return self.country_code
    

def get_phone_info(phonenumber, country_code):
    response = phonenumbers.parse(f'+{country_code}{phonenumber}', None)
    is_number_valid = phonenumbers.is_valid_number(response)
    is_possible_number = phonenumbers.is_possible_number(response)
    number_type = phonenumbers.number_type(response)
    isp = carrier.name_for_number(response, "en")
    if isp == "":
        isp = "Bilinmiyor"
    match is_possible_number:
        case True:
            is_possible_number = "Mümkün"
        case False:
            is_possible_number = "Mümkün Değil"
    match is_number_valid:
        case True:
            is_number_valid = "Geçerli"
        case False:
            is_number_valid = "Geçersiz"
    match number_type:
        case phonenumbers.PhoneNumberType.FIXED_LINE:
            number_type = "Sabit Hat"
        case phonenumbers.PhoneNumberType.MOBILE:
            number_type = "Mobil Hat"
        case phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
            number_type = "Sabit Hat veya Mobil Hat"
        case phonenumbers.PhoneNumberType.TOLL_FREE:
            number_type = "Ücretsiz Hat"
        case phonenumbers.PhoneNumberType.PREMIUM_RATE:
            number_type = "Premium Hat"
        case phonenumbers.PhoneNumberType.SHARED_COST:
            number_type = "Paylaşımlı Hat"
        case phonenumbers.PhoneNumberType.VOIP:
            number_type = "VoIP"
        case phonenumbers.PhoneNumberType.PERSONAL_NUMBER:
            number_type = "Kişisel Hat"
        case phonenumbers.PhoneNumberType.PAGER:
            number_type = "Pager"
        case phonenumbers.PhoneNumberType.UAN:
            number_type = "UAN"
        case phonenumbers.PhoneNumberType.UNKNOWN:
            number_type = "Bilinmeyen"
    return is_number_valid, is_possible_number, number_type,isp


def dummy_get_phone_info(phonenumber):
    try:
        response = phonenumbers.parse(f'+{phonenumber}', None)
        is_number_valid = phonenumbers.is_valid_number(response)
        if is_number_valid == False:
            is_possible_number = phonenumbers.is_possible_number(response)
            match is_possible_number:
                case True:
                    is_possible_number = "Mümkün"
                case False:
                    is_possible_number = "Mümkün Değil"
            return {
                "message": "Böyle Bir Numara Bulunmuyor",
                "Böyle Bir Numara Olması Mümkün mü?": is_possible_number
            }
        else:
            number_type = phonenumbers.number_type(response)
            match number_type:
                case phonenumbers.PhoneNumberType.FIXED_LINE:
                    number_type = "Sabit Hat"
                case phonenumbers.PhoneNumberType.MOBILE:
                    number_type = "Mobil Hat"
                case phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
                    number_type = "Sabit Hat veya Mobil Hat"
                case phonenumbers.PhoneNumberType.TOLL_FREE:
                    number_type = "Ücretsiz Hat"
                case phonenumbers.PhoneNumberType.PREMIUM_RATE:
                    number_type = "Premium Hat"
                case phonenumbers.PhoneNumberType.SHARED_COST:
                    number_type = "Paylaşımlı Hat"
                case phonenumbers.PhoneNumberType.VOIP:
                    number_type = "VoIP"
                case phonenumbers.PhoneNumberType.PERSONAL_NUMBER:
                    number_type = "Kişisel Hat"
                case phonenumbers.PhoneNumberType.PAGER:
                    number_type = "Pager"
                case phonenumbers.PhoneNumberType.UAN:
                    number_type = "UAN"
                case phonenumbers.PhoneNumberType.UNKNOWN:
                    number_type = "Bilinmeyen"
            isp = carrier.name_for_number(response, "tr")
            match is_number_valid:
                case True:
                    is_number_valid = "Geçerli"
                case False:
                    is_number_valid = "Geçersiz"
            return {
                "message": "Başarılı!",
                "Bu Numara Geçerli mi?": is_number_valid,
                "Telefon Numarası": phonenumber,
                "Numara Türü": number_type,
                "ISP": isp
            }
    except phonenumbers.phonenumberutil.NumberParseException:
        return {
            "message": "Geçersiz Numara"
        }
