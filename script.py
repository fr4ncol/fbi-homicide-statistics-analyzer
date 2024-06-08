import csv

state_mapping = {
    "50": "AK-Alaska",
    "01": "AL-Alabama",
    "03": "AR-Arkansas",
    "54": "AS-American Samoa",
    "02": "AZ-Arizona",
    "04": "CA-California",
    "05": "CO-Colorado",
    "06": "CT-Connecticut",
    "52": "CZ-Canal Zone",
    "08": "DC-District of Columbia",
    "07": "DE-Delaware",
    "09": "FL-Florida",
    "10": "GA-Georgia",
    "55": "GH-Guam",
    "51": "HI-Hawaii",
    "14": "IA-Iowa",
    "11": "ID-Idaho",
    "12": "IL-Illinois",
    "13": "IN-Indiana",
    "15": "KS-Kansas",
    "16": "KY-Kentucky",
    "17": "LA-Louisiana",
    "20": "MA-Massachusetts",
    "19": "MD-Maryland",
    "18": "ME-Maine",
    "21": "MI-Michigan",
    "22": "MN-Minnesota",
    "24": "MO-Missouri",
    "23": "MS-Mississippi",
    "25": "MT-Montana",
    "26": "NB-Nebraska",
    "32": "NC-North Carolina",
    "33": "ND-North Dakota",
    "28": "NH-New Hampshire",
    "29": "NJ-New Jersey",
    "30": "NM-New Mexico",
    "27": "NV-Nevada",
    "31": "NY-New York",
    "34": "OH-Ohio",
    "35": "OK-Oklahoma",
    "36": "OR-Oregon",
    "37": "PA-Pennsylvania",
    "53": "PR-Puerto Rico",
    "38": "RI-Rhode Island",
    "39": "SC-South Carolina",
    "40": "SD-South Dakota",
    "41": "IN-Tennessee",
    "42": "TX-Texas",
    "43": "UT-Utah",
    "62": "VI-Virgin Islands",
    "45": "VA-Virginia",
    "44": "VT-Vermont",
    "46": "WA-Washington",
    "48": "WI-Wisconsin",
    "47": "WV-West Virginia",
    "49": "WY-Wyoming"
}

fields = [
    ("numer_stanu", 2, 3),
    ("kod_agencji", 4, 10),
    ("typ_miejsca_zbrodni", 11, 11),
    ("podkategoria_miejsca_zbrodni", 12, 12),
    ("rok", 14, 15),
    ("populacja", 16, 24),
    ("kod_hrabstwa", 25, 27),
    ("numer_msa", 28, 30),
    ("identyfikacja_msa", 31, 31),
    ("nazwa_agencji", 32, 55),
    ("nazwa_stanu", 56, 61),
    ("miesiac_przestepstwa", 62, 63),
    ("ostatni_update", 64, 69),
    ("typ_zabojstwa", 71, 71),
    ("numer_zdarzenia", 72, 74),
    ("sytuacja", 75, 75),
    ("wiek_ofiary", 76, 77),
    ("plec_ofiary", 78, 78),
    ("rasa_ofiary", 79, 79),
    ("pochodzenie_etniczne_ofiary", 80, 80),
    ("wiek_sprawcy", 81, 82),
    ("plec_sprawcy", 83, 83),
    ("rasa_sprawcy", 84, 84),
    ("pochodzenie_etniczne_sprawcy", 85, 85),
    ("uzyta_bron", 86, 87),
    ("relacja_ofiary_wzledem_sprawcy", 88, 89),
    ("okolicznosc", 90, 91),
    ("podokolicznosc", 92, 92),
    ("ilosc_ofiar", 93, 95),
    ("ilosc_sprawcow", 96, 98),
    ("opis_ofiar_innych_niz_pierwsza", 99, 148),
    ("opis_sprawcow_innych_niz_pierwszy", 149, 268)
]

# Function to parse each line based on the defined positions
def parse_line(line):
    data = {}
    for field, start, end in fields:
        data[field] = line[start-1:end].strip()
    return data

# Read the input file, parse the data, and write to a CSV file
input_filename = '2022_SHR_NATIONAL_MASTER_FILE.txt'
output_filename = 'output_data.csv'

with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=[field[0] for field in fields])
    writer.writeheader()

    for line in infile:
        parsed_data = parse_line(line)
        writer.writerow(parsed_data)

print(f"Data has been successfully written to {output_filename}")