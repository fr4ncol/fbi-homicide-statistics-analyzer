import csv

# Function to read mapping files and return a dictionary
def read_mapping_file(filename):
    mapping = {}
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            mapping[row['number']] = row['state']  # For state mapping
    return mapping

def read_location_type_file(filename):
    mapping = {}
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            mapping[row['code']] = row['description']  # For location type mapping
    return mapping

# Read the state and location type mappings
state_mapping = read_mapping_file('mappings\state_mapping.csv')
location_type_mapping = read_location_type_file('mappings\location_type_mapping.csv')

# Define the positions and their respective fields
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
        value = line[start-1:end].strip()
        if field == "numer_stanu":
            value = state_mapping.get(value, value)  # Translate state number to name
        elif field == "typ_miejsca_zbrodni":
            value = location_type_mapping.get(value, value)  # Translate crime location type
        data[field] = value
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
