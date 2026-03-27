import json
import os

target = r'c:\Projetos\ZHC\App\strains.js'

DATABASE_FULL = {
  "24k gold": {
    "name": "24k Gold",
    "type": "indica",
    "lineage": "Kosher x Tangie",
    "terpenes": "Limoneno"
  },
  "acapulco gold": {
    "name": "Acapulco Gold",
    "type": "sativa",
    "lineage": "Mexico",
    "terpenes": "Mirceno"
  },
  "acdc": {
    "name": "ACDC",
    "type": "hybrid",
    "lineage": "Cannatonic",
    "terpenes": "Mirceno"
  },
  "afghan kush": {
    "name": "Afghan Kush",
    "type": "indica",
    "lineage": "Hindu Kush",
    "terpenes": "Mirceno"
  },
  "agent orange": {
    "name": "Agent Orange",
    "type": "hybrid",
    "lineage": "Orange x Diesel",
    "terpenes": "Limoneno"
  },
  "ak-47": {
    "name": "AK-47",
    "type": "sativa-dominant",
    "lineage": "Landrace Mix",
    "terpenes": "Mirceno"
  },
  "alien og": {
    "name": "Alien OG",
    "type": "indica",
    "lineage": "Tahoe x Alien",
    "terpenes": "Limoneno"
  },
  "alaskan thunder fuck": {
    "name": "ATF",
    "type": "sativa",
    "lineage": "North American",
    "terpenes": "Mirceno"
  },
  "amnesia haze": {
    "name": "Amnesia Haze",
    "type": "sativa",
    "lineage": "Thai x Afghan",
    "terpenes": "Mirceno"
  },
  "animal cookies": {
    "name": "Animal Cookies",
    "type": "indica",
    "lineage": "GSC x Fire OG",
    "terpenes": "Cariofileno"
  },
  "apple fritter": {
    "name": "Apple Fritter",
    "type": "hybrid",
    "lineage": "Sour Apple x Cookies",
    "terpenes": "Cariofileno"
  },
  "atomic nl": {
    "name": "Atomic NL",
    "type": "indica",
    "lineage": "NL Selection",
    "terpenes": "Mirceno"
  },
  "banana kush": {
    "name": "Banana Kush",
    "type": "indica",
    "lineage": "Ghost OG",
    "terpenes": "Limoneno"
  },
  "berry white": {
    "name": "Berry White",
    "type": "indica",
    "lineage": "Blueberry x Widow",
    "terpenes": "Mirceno"
  },
  "big bud": {
    "name": "Big Bud",
    "type": "indica",
    "lineage": "Afghan x Skunk",
    "terpenes": "Mirceno"
  },
  "biscotti": {
    "name": "Biscotti",
    "type": "indica",
    "lineage": "Gelato x OG",
    "terpenes": "Cariofileno"
  },
  "black domina": {
    "name": "Black Domina",
    "type": "indica",
    "lineage": "Indica Mix",
    "terpenes": "Mirceno"
  },
  "blackberry kush": {
    "name": "Blackberry Kush",
    "type": "indica",
    "lineage": "Blackberry x Afghan",
    "terpenes": "Mirceno"
  },
  "blue cheese": {
    "name": "Blue Cheese",
    "type": "indica",
    "lineage": "Blueberry x Cheese",
    "terpenes": "Cariofileno"
  },
  "blue dream": {
    "name": "Blue Dream",
    "type": "sativa",
    "lineage": "Blueberry x Haze",
    "terpenes": "Mirceno"
  },
  "blueberry": {
    "name": "Blueberry",
    "type": "indica",
    "lineage": "Thai x Afghan",
    "terpenes": "Mirceno"
  },
  "bruce banner": {
    "name": "Bruce Banner",
    "type": "sativa",
    "lineage": "OG x Diesel",
    "terpenes": "Limoneno"
  },
  "bubba kush": {
    "name": "Bubba Kush",
    "type": "indica",
    "lineage": "OG x NL",
    "terpenes": "Cariofileno"
  },
  "bubble gum": {
    "name": "Bubble Gum",
    "type": "hybrid",
    "lineage": "Unknown",
    "terpenes": "Mirceno"
  },
  "candy kush": {
    "name": "Candy Kush",
    "type": "hybrid",
    "lineage": "BD x OG",
    "terpenes": "Limoneno"
  },
  "cannatonic": {
    "name": "Cannatonic",
    "type": "hybrid",
    "lineage": "MK Ultra x G13",
    "terpenes": "Mirceno"
  },
  "casey jones": {
    "name": "Casey Jones",
    "type": "sativa",
    "lineage": "Oriental x Diesel",
    "terpenes": "Mirceno"
  },
  "cat piss": {
    "name": "Cat Piss",
    "type": "sativa",
    "lineage": "SSH Pheno",
    "terpenes": "Pineno"
  },
  "charlotte's web": {
    "name": "Charlotte's Web",
    "type": "indica",
    "lineage": "Medicinal Hemp",
    "terpenes": "Mirceno"
  },
  "cheese": {
    "name": "Cheese",
    "type": "hybrid",
    "lineage": "Skunk #1 Pheno",
    "terpenes": "Cariofileno"
  },
  "chemdawg": {
    "name": "Chemdawg",
    "type": "hybrid",
    "lineage": "Thai x Nepalese",
    "terpenes": "Cariofileno"
  },
  "cherry bomb": {
    "name": "Cherry Bomb",
    "type": "hybrid",
    "lineage": "Big Bud x Cherry",
    "terpenes": "Mirceno"
  },
  "cherry pie": {
    "name": "Cherry Pie",
    "type": "indica",
    "lineage": "GDP x Durban",
    "terpenes": "Mirceno"
  },
  "chocolope": {
    "name": "Chocolope",
    "type": "sativa",
    "lineage": "Chocolate x Cannalope",
    "terpenes": "Mirceno"
  },
  "chronic": {
    "name": "Chronic",
    "type": "hybrid",
    "lineage": "NL x Skunk x AK",
    "terpenes": "Mirceno"
  },
  "cinderella 99": {
    "name": "Cinderella 99",
    "type": "sativa",
    "lineage": "Princess x Jack",
    "terpenes": "Terpinoleno"
  },
  "clementine": {
    "name": "Clementine",
    "type": "sativa",
    "lineage": "Tangie x Lemon Skunk",
    "terpenes": "Limoneno"
  },
  "colombian gold": {
    "name": "Colombian Gold",
    "type": "sativa",
    "lineage": "Santa Marta Landrace",
    "terpenes": "Mirceno"
  },
  "cookies and cream": {
    "name": "Cookies and Cream",
    "type": "hybrid",
    "lineage": "Starfighter x GSC",
    "terpenes": "Cariofileno"
  },
  "cream caramel": {
    "name": "Cream Caramel",
    "type": "indica",
    "lineage": "3-way mix",
    "terpenes": "Mirceno"
  },
  "critical kush": {
    "name": "Critical Kush",
    "type": "indica",
    "lineage": "Critical x OG",
    "terpenes": "Mirceno"
  },
  "critical mass": {
    "name": "Critical Mass",
    "type": "indica",
    "lineage": "Afghani x Skunk",
    "terpenes": "Mirceno"
  },
  "death star": {
    "name": "Death Star",
    "type": "indica",
    "lineage": "Sensi Star x Sour D",
    "terpenes": "Mirceno"
  },
  "diamond og": {
    "name": "Diamond OG",
    "type": "indica",
    "lineage": "OG Kush Hybrid",
    "terpenes": "Limoneno"
  },
  "diesel": {
    "name": "Original Diesel",
    "type": "hybrid",
    "lineage": "Chemdawg x NL",
    "terpenes": "Cariofileno"
  },
  "do-si-dos": {
    "name": "Do-Si-Dos",
    "type": "indica",
    "lineage": "GSC x Face Off",
    "terpenes": "Limoneno"
  },
  "durban poison": {
    "name": "Durban Poison",
    "type": "sativa",
    "lineage": "South African Landrace",
    "terpenes": "Terpinoleno"
  },
  "early skunk": {
    "name": "Early Skunk",
    "type": "hybrid",
    "lineage": "Skunk x Pearl",
    "terpenes": "Mirceno"
  },
  "el patron": {
    "name": "El Patron",
    "type": "hybrid",
    "lineage": "AMG x Shiva",
    "terpenes": "Limoneno"
  },
  "euphoria": {
    "name": "Euphoria",
    "type": "hybrid",
    "lineage": "Medic x Shark",
    "terpenes": "Mirceno"
  },
  "fat banana": {
    "name": "Fat Banana",
    "type": "indica",
    "lineage": "Banana OG x OG",
    "terpenes": "Limoneno"
  },
  "fire og": {
    "name": "Fire OG",
    "type": "indica",
    "lineage": "OG x SFV OG",
    "terpenes": "Mirceno"
  },
  "forbidden fruit": {
    "name": "Forbidden Fruit",
    "type": "indica",
    "lineage": "GDP x Tangie",
    "terpenes": "Mirceno"
  },
  "fruit spirit": {
    "name": "Fruit Spirit",
    "type": "indica",
    "lineage": "Blueberry x Widow",
    "terpenes": "Limoneno"
  },
  "g13": {
    "name": "G13",
    "type": "indica",
    "lineage": "Gov Seed",
    "terpenes": "Mirceno"
  },
  "garlic cookies": {
    "name": "GMO Cookies",
    "type": "indica",
    "lineage": "GSC x Chem",
    "terpenes": "Cariofileno"
  },
  "gelato": {
    "name": "Gelato #33",
    "type": "hybrid",
    "lineage": "Sunset x Thin Mint",
    "terpenes": "Cariofileno"
  },
  "ghost train haze": {
    "name": "Ghost Train Haze",
    "type": "sativa",
    "lineage": "Ghost OG x Neville",
    "terpenes": "Terpinoleno"
  },
  "girl scout cookies": {
    "name": "Girl Scout Cookies (GSC)",
    "type": "indica",
    "lineage": "OG x Durban",
    "terpenes": "Cariofileno"
  },
  "godfather og": {
    "name": "Godfather OG",
    "type": "indica",
    "lineage": "Triple OG x Cherry",
    "terpenes": "Mirceno"
  },
  "golden goat": {
    "name": "Golden Goat",
    "type": "sativa",
    "lineage": "Hawaiian x Romulan",
    "terpenes": "Terpinoleno"
  },
  "gorilla glue": {
    "name": "Gorilla Glue #4 (GG4)",
    "type": "hybrid",
    "lineage": "Mix Sour P.",
    "terpenes": "Cariofileno"
  },
  "granddaddy purple": {
    "name": "Granddaddy Purple (GDP)",
    "type": "indica",
    "lineage": "Purps x Big Bud",
    "terpenes": "Mirceno"
  },
  "grape ape": {
    "name": "Grape Ape",
    "type": "indica",
    "lineage": "Mendo Purps x Afghani",
    "terpenes": "Mirceno"
  },
  "green crack": {
    "name": "Green Crack",
    "type": "sativa",
    "lineage": "Skunk x Afghani",
    "terpenes": "Mirceno"
  },
  "harlequin": {
    "name": "Harlequin",
    "type": "sativa",
    "lineage": "Landrace Mix",
    "terpenes": "Mirceno"
  },
  "headbanger": {
    "name": "Headbanger",
    "type": "sativa",
    "lineage": "Sour D x Kush",
    "terpenes": "Limoneno"
  },
  "hindu kush": {
    "name": "Hindu Kush",
    "type": "indica",
    "lineage": "Afghan Landrace",
    "terpenes": "Mirceno"
  },
  "holy grail kush": {
    "name": "Holy Grail Kush",
    "type": "hybrid",
    "lineage": "Kosher x OG 18",
    "terpenes": "Mirceno"
  },
  "ice": {
    "name": "ICE",
    "type": "hybrid",
    "lineage": "NL x Skunk x Afghan",
    "terpenes": "Mirceno"
  },
  "ice cream cake": {
    "name": "Ice Cream Cake",
    "type": "indica",
    "lineage": "Wedding x Gelato",
    "terpenes": "Limoneno"
  },
  "jack herer": {
    "name": "Jack Herer",
    "type": "sativa",
    "lineage": "Haze x Mix",
    "terpenes": "Terpinoleno"
  },
  "kali mist": {
    "name": "Kali Mist",
    "type": "sativa",
    "lineage": "Unknown Haze",
    "terpenes": "Mirceno"
  },
  "king louie xiii": {
    "name": "King Louie XIII",
    "type": "indica",
    "lineage": "OG x Confid.",
    "terpenes": "Mirceno"
  },
  "kosher kush": {
    "name": "Kosher Kush",
    "type": "indica",
    "lineage": "Indica Kush",
    "terpenes": "Mirceno"
  },
  "kush mints": {
    "name": "Kush Mints",
    "type": "hybrid",
    "lineage": "Animal x Bubba",
    "terpenes": "Limoneno"
  },
  "la confidential": {
    "name": "LA Confidential",
    "type": "indica",
    "lineage": "Afghan x Cali Indica",
    "terpenes": "Mirceno"
  },
  "lavender": {
    "name": "Lavender",
    "type": "indica",
    "lineage": "Skunk x Mix",
    "terpenes": "Linalol"
  },
  "lemon haze": {
    "name": "Lemon Haze",
    "type": "sativa",
    "lineage": "Skunk x Haze",
    "terpenes": "Limoneno"
  },
  "lsd": {
    "name": "LSD",
    "type": "indica",
    "lineage": "Skunk x Mazar",
    "terpenes": "Mirceno"
  },
  "manga rosa": {
    "name": "Manga Rosa",
    "type": "sativa",
    "lineage": "Brazilian Landrace",
    "terpenes": "Terpinoleno"
  },
  "master kush": {
    "name": "Master Kush",
    "type": "indica",
    "lineage": "Hindu x Skunk",
    "terpenes": "Mirceno"
  },
  "mazar": {
    "name": "Mazar",
    "type": "indica",
    "lineage": "Afghan x Skunk",
    "terpenes": "Mirceno"
  },
  "mimosa": {
    "name": "Mimosa",
    "type": "sativa",
    "lineage": "Clementine x Punch",
    "terpenes": "Limoneno"
  },
  "northern lights": {
    "name": "Northern Lights",
    "type": "indica",
    "lineage": "Afghan x Thai",
    "terpenes": "Mirceno"
  },
  "og kush": {
    "name": "OG Kush",
    "type": "hybrid",
    "lineage": "Chem x Hindu Kush",
    "terpenes": "Mirceno"
  },
  "panama red": {
    "name": "Panama Red",
    "type": "sativa",
    "lineage": "Central American",
    "terpenes": "Mirceno"
  },
  "pineapple express": {
    "name": "Pineapple Express",
    "type": "hybrid",
    "lineage": "Trainwreck x Hawaiian",
    "terpenes": "Mirceno"
  },
  "purple haze": {
    "name": "Purple Haze",
    "type": "sativa",
    "lineage": "Purple Thai x Haze",
    "terpenes": "Mirceno"
  },
  "purple punch": {
    "name": "Purple Punch",
    "type": "indica",
    "lineage": "GDP x Larry OG",
    "terpenes": "Cariofileno"
  },
  "quantum kush": {
    "name": "Quantum Kush",
    "type": "sativa",
    "lineage": "Irish x Wreck",
    "terpenes": "Terpinoleno"
  },
  "runtz": {
    "name": "Runtz",
    "type": "hybrid",
    "lineage": "Zkittlez x Gelato",
    "terpenes": "Cariofileno"
  },
  "santa maria": {
    "name": "Santa Maria",
    "type": "sativa",
    "lineage": "Brazil",
    "terpenes": "Limoneno"
  },
  "shiva skunk": {
    "name": "Shiva Skunk",
    "type": "indica",
    "lineage": "Skunk 1 x NL 5",
    "terpenes": "Mirceno"
  },
  "sour diesel": {
    "name": "Sour Diesel",
    "type": "sativa",
    "lineage": "Chem x Skunk",
    "terpenes": "Cariofileno"
  },
  "strawberry cough": {
    "name": "Strawberry Cough",
    "type": "sativa",
    "lineage": "Strawberry Fields x Haze",
    "terpenes": "Mirceno"
  },
  "super lemon haze": {
    "name": "Super Lemon Haze",
    "type": "sativa",
    "lineage": "Lemon Skunk x SSH",
    "terpenes": "Limoneno"
  },
  "tangerine dream": {
    "name": "Tangerine Dream",
    "type": "sativa",
    "lineage": "G13 x Haze",
    "terpenes": "Limoneno"
  },
  "wedding cake": {
    "name": "Wedding Cake",
    "type": "indica",
    "lineage": "TK x Mints",
    "terpenes": "Cariofileno"
  },
  "white widow": {
    "name": "White Widow",
    "type": "hybrid",
    "lineage": "Brazilian x Indian",
    "terpenes": "Mirceno"
  },
  "zkittlez": {
    "name": "Zkittlez",
    "type": "indica",
    "lineage": "Grape Ape x Grapefruit",
    "terpenes": "Cariofileno"
  },
  "amnesia gold": {
    "name": "Amnesia Gold",
    "type": "sativa",
    "lineage": "Amnesia x Lennon"
  },
  "ayahuasca purple": {
    "name": "Ayahuasca Purple",
    "type": "indica",
    "lineage": "Red River x Master Kush"
  },
  "bcn critical xxl": {
    "name": "BCN Critical XXL",
    "type": "indica",
    "lineage": "Kritikal x Afghan"
  },
  "beaver cookies": {
    "name": "Beaver Cookies",
    "type": "hybrid",
    "lineage": "GSC x GMO"
  },
  "blue magoo": {
    "name": "Blue Magoo",
    "type": "indica",
    "lineage": "Blueberry x Major Pink"
  },
  "bubble kush": {
    "name": "Bubble Kush",
    "type": "indica",
    "lineage": "Bubble Gum x OG Kush"
  },
  "candy kush auto": {
    "name": "Candy Kush Auto",
    "type": "hybrid",
    "lineage": "Candy x Ruderalis"
  },
  "cbd kush": {
    "name": "CBD Kush",
    "type": "hybrid",
    "lineage": "Kanchi x Quaze"
  },
  "dark phoenix": {
    "name": "Dark Phoenix",
    "type": "sativa",
    "lineage": "Trainwreck x Jack Herer"
  },
  "fat banana auto": {
    "name": "Fat Banana Auto",
    "type": "indica",
    "lineage": "FB x Ruderalis"
  },
  "fast eddy": {
    "name": "Fast Eddy",
    "type": "hybrid",
    "lineage": "Cheese x Juanita"
  },
  "green gelato": {
    "name": "Green Gelato",
    "type": "hybrid",
    "lineage": "Sunset x Thin Mint"
  },
  "hulkberry": {
    "name": "HulkBerry",
    "type": "sativa",
    "lineage": "OG Kush x Strawberry Diesel"
  },
  "quick one": {
    "name": "Quick One",
    "type": "indica",
    "lineage": "Lowryder x NL"
  },
  "royal gorilla": {
    "name": "Royal Gorilla",
    "type": "hybrid",
    "lineage": "Sour Dubb x Chem Sister"
  },
  "royal medic": {
    "name": "Royal Medic",
    "type": "sativa",
    "lineage": "Juanita x Critical"
  },
  "royal runtz": {
    "name": "Royal Runtz",
    "type": "hybrid",
    "lineage": "Zkittlez x Gelato"
  },
  "sour diesel auto": {
    "name": "Sour Diesel Auto",
    "type": "sativa",
    "lineage": "SD x Ruderalis"
  },
  "sweet zz": {
    "name": "Sweet ZZ",
    "type": "indica",
    "lineage": "Grape Ape x Grapefruit"
  },
  "triple g": {
    "name": "Triple G",
    "type": "indica",
    "lineage": "Gorilla x Gelato"
  },
  "watermelon": {
    "name": "Watermelon",
    "type": "indica",
    "lineage": "Unknown"
  },
  "white widow auto": {
    "name": "White Widow Auto",
    "type": "hybrid",
    "lineage": "WW x Ruderalis"
  },
  "707 headband": {
    "name": "707 Headband",
    "type": "hybrid",
    "lineage": "Sour D x OG"
  },
  "afghan pearl": {
    "name": "Afghan Pearl",
    "type": "indica",
    "lineage": "Afghan x Pearl"
  },
  "alien dawg": {
    "name": "Alien Dawg",
    "type": "indica",
    "lineage": "Alien x Chem"
  },
  "amnesia auto": {
    "name": "Amnesia Auto",
    "type": "sativa",
    "lineage": "Amnesia x Ruder."
  },
  "animal mints": {
    "name": "Animal Mints",
    "type": "hybrid",
    "lineage": "Animal x GSC"
  },
  "aurora borealis": {
    "name": "Aurora Borealis",
    "type": "indica",
    "lineage": "NL x Skunk"
  },
  "bc big bud": {
    "name": "BC Big Bud",
    "type": "indica",
    "lineage": "Big Bud x Sativa"
  },
  "blue magoo auto": {
    "name": "Blue Magoo Auto",
    "type": "indica",
    "lineage": "Blueberry x Major"
  },
  "bubba kush auto": {
    "name": "Bubba Kush Auto",
    "type": "indica",
    "lineage": "Bubba x Ruder."
  },
  "california orange": {
    "name": "Cali Orange",
    "type": "hybrid",
    "lineage": "Cali Landrace"
  },
  "chocolate haze": {
    "name": "Chocolate Haze",
    "type": "sativa",
    "lineage": "Thai x Cannalope"
  },
  "cookies gelato": {
    "name": "Cookies Gelato",
    "type": "hybrid",
    "lineage": "GSC x Gelato"
  },
  "critical auto": {
    "name": "Critical Auto",
    "type": "indica",
    "lineage": "Critical x Ruder."
  },
  "dinamex": {
    "name": "Dinamex",
    "type": "hybrid",
    "lineage": "Cali x Mexico"
  },
  "glueberry og": {
    "name": "Glueberry OG",
    "type": "hybrid",
    "lineage": "GG x Berry"
  },
  "green gelat auto": {
    "name": "Green Gelato Auto",
    "type": "hybrid",
    "lineage": "Gelato x Ruder."
  },
  "kali dog": {
    "name": "Kali Dog",
    "type": "hybrid",
    "lineage": "Chemdawg x Sour D"
  },
  "medical mass": {
    "name": "Medical Mass",
    "type": "hybrid",
    "lineage": "Critical x Medic"
  },
  "mother's helper": {
    "name": "Mother's Helper",
    "type": "hybrid",
    "lineage": "Chocolope x NL"
  },
  "northern light auto": {
    "name": "NL Auto",
    "type": "indica",
    "lineage": "NL x Ruder."
  },
  "og kush auto": {
    "name": "OG Kush Auto",
    "type": "hybrid",
    "lineage": "OG x Ruder."
  },
  "painkiller xl": {
    "name": "Painkiller XL",
    "type": "sativa",
    "lineage": "Respect x Juanita"
  },
  "purple queen auto": {
    "name": "Purple Queen Auto",
    "type": "indica",
    "lineage": "Queen x Ruder."
  },
  "royal ak": {
    "name": "Royal AK",
    "type": "sativa",
    "lineage": "AK-47 x Mix"
  },
  "royal bluematic": {
    "name": "Royal Bluematic",
    "type": "indica",
    "lineage": "Blueberry x Ruder."
  },
  "royal cheese": {
    "name": "Royal Cheese",
    "type": "hybrid",
    "lineage": "Cheese x Mix"
  },
  "royal cookies": {
    "name": "Royal Cookies",
    "type": "indica",
    "lineage": "Cookies Mix"
  },
  "royal critical": {
    "name": "Royal Critical",
    "type": "indica",
    "lineage": "Critical Mix"
  },
  "royal dwarf": {
    "name": "Royal Dwarf",
    "type": "indica",
    "lineage": "Skunk x Ruder."
  },
  "royal gorila auto": {
    "name": "Royal Gorilla Auto",
    "type": "hybrid",
    "lineage": "Gorilla x Ruder."
  },
  "royal haze auto": {
    "name": "Royal Haze Auto",
    "type": "sativa",
    "lineage": "Haze x Ruder."
  },
  "royal jack auto": {
    "name": "Royal Jack Auto",
    "type": "sativa",
    "lineage": "Jack Herer x Ruder."
  },
  "shining silver haze": {
    "name": "Shining Silver Haze",
    "type": "sativa",
    "lineage": "Haze x Skunk"
  },
  "solomatic cbd": {
    "name": "Solomatic CBD",
    "type": "hybrid",
    "lineage": "Asia CBD Mix"
  },
  "special kush auto": {
    "name": "Special Kush Auto",
    "type": "indica",
    "lineage": "Kush x Ruder."
  },
  "speedy chile": {
    "name": "Speedy Chile",
    "type": "indica",
    "lineage": "Early Skunk x Chile"
  },
  "stress killer auto": {
    "name": "Stress Killer Auto",
    "type": "sativa",
    "lineage": "Lemon x Ruder."
  },
  "sweet zz auto": {
    "name": "Sweet ZZ Auto",
    "type": "indica",
    "lineage": "Sweet ZZ x Ruder."
  },
  "watermelon auto": {
    "name": "Watermelon Auto",
    "type": "indica",
    "lineage": "Watermelon x Ruder."
  },
  "wedding gelato": {
    "name": "Wedding Gelato",
    "type": "hybrid",
    "lineage": "Wedding x Gelato"
  }
}

js_content = 'const STRAIN_DB = ' + json.dumps(DATABASE_FULL) + ';'
with open(target, 'w', encoding='utf-8') as f:
    f.write('const STRAIN_DB = ' + json.dumps(DATABASE_FULL) + ';')
print('SUCESSO: Banco de dados regenerado!')
