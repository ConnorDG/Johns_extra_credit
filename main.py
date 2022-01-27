from selenium import webdriver
import time

animal_ary = ["Aardvark",
              "Albatross",
              "Alligator",
              "Alpaca",
              "Anole",
              "Ant",
              "Anteater",
              "Antelope",
              "Ape",
              "Armadillo",
              "Ass",
              "Baboon",
              "Badger",
              "Barracuda",
              "Bat",
              "Bear",
              "Beaver",
              "Bee",
              "Binturong",
              "Bird",
              "Bison",
              "Bluebird",
              "Boar",
              "Bobcat",
              "Budgerigar",
              "Buffalo",
              "Butterfly",
              "Camel",
              "Capybara",
              "Caracal",
              "Caribou",
              "Cassowary",
              "Cat",
              "Caterpillar",
              "Cattle",
              "Chamois",
              "Cheetah",
              "Chicken",
              "Chimpanzee",
              "Chinchilla",
              "Chough",
              "Coati",
              "Cobra",
              "Cockroach",
              "Cod",
              "Cormorant",
              "Cougar",
              "Coyote",
              "Crab",
              "Crane",
              "Cricket",
              "Crocodile",
              "Crow",
              "Cuckoo",
              "Curlew",
              "Deer",
              "Dhole",
              "Dingo",
              "Dinosaur",
              "Dog",
              "Dogfish",
              "Dolphin",
              "Donkey",
              "Dove",
              "Dragonfly",
              "Duck",
              "Dugong",
              "Dunlin",
              "Eagle",
              "Echidna",
              "Eel",
              "Eland",
              "Elephant",
              "Elephantseal",
              "Elk",
              "Emu",
              "Falcon",
              "Ferret",
              "Finch",
              "Fish",
              "Fisher",
              "Flamingo",
              "Fly",
              "Flycatcher",
              "Fox",
              "Frog",
              "Gaur",
              "Gazelle",
              "Gecko",
              "Genet",
              "Gerbil",
              "Giantpanda",
              "Giraffe",
              "Gnat",
              "Gnu",
              "Goat",
              "Goldfinch",
              "Goosander",
              "Goose",
              "Gorilla",
              "Goshawk",
              "Grasshopper",
              "Grouse",
              "Guanaco",
              "Guineafowl",
              "Guineapig",
              "Gull",
              "Hamster",
              "Hare",
              "Hawk",
              "Hedgehog",
              "Hermitcrab",
              "Heron",
              "Herring",
              "Hippopotamus",
              "Hoatzin",
              "Hoopoe",
              "Hornet",
              "Horse",
              "Human",
              "Hummingbird",
              "Hyena",
              "Ibex",
              "Ibis",
              "Iguana",
              "Impala",
              "Jackal",
              "Jaguar",
              "Jay",
              "Jellyfish",
              "Jerboa",
              "Kangaroo",
              "Kingbird",
              "Kingfisher",
              "Kinkajou",
              "Kite",
              "Koala",
              "Kodkod",
              "Komododragon",
              "Kookaburra",
              "Kouprey",
              "Kudu",
              "Langur",
              "Lapwing",
              "Lark",
              "Lechwe",
              "Lemur",
              "Leopard",
              "Lion",
              "Lizard",
              "Llama",
              "Lobster",
              "Locust",
              "Loris",
              "Louse",
              "Lynx",
              "Lyrebird",
              "Macaque",
              "Macaw",
              "Magpie",
              "Mallard",
              "Mammoth",
              "Manatee",
              "Mandrill",
              "Margay",
              "Marmoset",
              "Marmot",
              "Meerkat",
              "Mink",
              "Mole",
              "Mongoose",
              "Monkey",
              "Moose",
              "Mosquito",
              "Mouse",
              "Myna",
              "Narwhal",
              "Newt",
              "Nightingale",
              "Nilgai",
              "Ocelot",
              "Octopus",
              "Okapi",
              "Oncilla",
              "Opossum",
              "Orangutan",
              "Oryx",
              "Ostrich",
              "Otter",
              "Ox",
              "Owl",
              "Oyster",
              "Panther",
              "Parrot",
              "Panda",
              "Partridge",
              "Peafowl",
              "Penguin",
              "Pheasant",
              "Pig",
              "Pigeon",
              "Pika",
              "Polarbear",
              "Pony",
              "Porcupine",
              "Porpoise",
              "Prairiedog",
              "Pug",
              "Quail",
              "Quelea",
              "Quetzal",
              "Rabbit",
              "Raccoon",
              "Ram",
              "Rat",
              "Raven",
              "Reddeer",
              "Redpanda",
              "Reindeer",
              "Rhea",
              "Rhinoceros",
              "Rook",
              "Saki",
              "Salamander",
              "Salmon",
              "Sanddollar",
              "Sandpiper",
              "Sardine",
              "Sassaby",
              "Sealion",
              "Seahorse",
              "Seal",
              "Serval",
              "Shark",
              "Sheep",
              "Shrew",
              "Shrike",
              "Siamang",
              "Skink",
              "Skipper",
              "Skunk",
              "Sloth",
              "Snail",
              "Snake",
              "Spider",
              "Spoonbill",
              "Squid",
              "Squirrel",
              "Starling",
              "Stilt",
              "Swan",
              "Tamarin",
              "Tapir",
              "Tarsier",
              "Termite",
              "Thrush",
              "Tiger",
              "Toad",
              "Topi",
              "Toucan",
              "Turaco",
              "Turkey",
              "Turtle",
              "Vicuña",
              "Vinegaroon",
              "Viper",
              "Vulture",
              "Wallaby",
              "Walrus",
              "Wasp",
              "Waterbuffalo",
              "Waxwing",
              "Weasel",
              "Whale",
              "Wobbegong",
              "Wolf",
              "Wolverine",
              "Wombat",
              "Woodpecker",
              "Worm",
              "Wren",
              "Yak",
              "Zebra"]
animal = animal_ary[0]
number = 100000000
passwrd = animal + number
n = 0
website = input("ULR: ")
web = webdriver.Chrome()
web.get(website)
text_box = input("textbox: ")
submit_box = input("submit: ")
time.sleep(1)
success = False
while not success:
    box = web.find(text_box)
    box.send_keys(passwrd)
    submit = web.find(submit_box)
    number += 1
    success = web.find()
    if number == 10000000000:
        number = 1000000000
        n += 1
        animal = animal_ary[n]

    passwrd = animal + number
