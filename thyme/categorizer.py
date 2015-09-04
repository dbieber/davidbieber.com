import re

HOUSING = 'housing'
TRANSPORTATION = 'transportation'
ENTERTAINMENT = 'entertainment'
FOOD = 'food'
TECHNOLOGY = 'technology'
HYGEINE = 'hygeine'
CLOTHING = 'clothing'
GIFTS = 'gifts'
MEDICAL = 'medical'
TAXES = 'taxes'
HOTELS = 'hotel'
DONATIONS = 'donation'
EDUCATION = 'education'
INCOME = 'income'

BILLS = 'bills'
FURNITURE = 'furniture'
DECORATIONS = 'decoration'

GAMES = 'games'
SPORTS = 'sports'
BOOKS = 'books'
MOVIES = 'movies'
THEATER = 'theater'

subcategories = {
    HOUSING: [
        FURNITURE,
        BILLS,
        DECORATIONS,
    ],
    ENTERTAINMENT: [
        GAMES,
        SPORTS,
        BOOKS,
        MOVIES,
        THEATER,
    ],
}
exclusion_words = {
    FOOD: [
        'subway swipe',
    ],
    HOTELS: [
        ['uber'],
    ],
}
indicator_words = {
    HOUSING: [
        'moving',
        'for keys',
        'relocation',
        ['holding fee', 'harvest'],
        ['lease', 'americana'],
        'application fee',
    ],
    BILLS: [
        'rent',
        ['harvest', 'electric'],
        ['harvest', 'utils'],
        ['bills', 'harvest'],
        ['internet', 'harvest'],
        'state farm',
        'renters insurance',
    ],
    FURNITURE: [
        'signature hardware',
        'bar stools',
        'bed bath and beyond',
        'home depot',
        'ikea everything',
        'ikea bed',
        'command hooks',
        'oak table',
        'mattress',
    ],
    DECORATIONS: [
        'klein bottle',
    ],
    TRANSPORTATION: [
        'vta',
        'uber',
        'caltrain',
        'ca license',
        'flight',
        'bike',
        'bus',
        'lyft',
        'bart',
        'metrocard',
        ['metro', 'card'],
        ['albany', 'to', 'new york'],
        'taxi',
        'njtransit',
        'nj transit',
        'for gas',  # double check this
        'flights',
        'trailways',
        'megabus',
        ['tickets', 'princeton'],
        ['ride', 'airport'],
        'muni',
        'metro',
        'toll to',
        'Subway swipe',
        'lirr',
        'clipper',
        'train',
        'cab',
        'penn station',
        'ticket to',
        'tickets to',
        'break pads',
    ],
    ENTERTAINMENT: [
        ['escape', 'room'],
        'escape games',
        'tango',
        'ski trip',
        'skiing',
        'ski ticket',
        'concert',
        'reunions',
        'one republic',
        'party',
        ['locked', 'room'],
        'museum',
    ],
    GAMES: [
        'letterpress',
        'game for ios',
    ],
    SPORTS: [
        'skating',
        'tennis',
        'golf',
        'gym',
        'squash',
        'soccer',
        'sports',
    ],
    BOOKS: [
        'big fish',
        'book', # but not book of mormon
        'books',
        'hyperion',
    ],
    MOVIES: [
        'whiplash',
        'kingsman',
        'movie ticket',
        'movie',
        'cinemark',
        'big hero 6',
    ],
    THEATER: [
        'pippin',
        'if then',
        'wicked ticket',
        'wicked tickets',
        'book of mormon',
        'sweeney todd',
        'triangle show',
        'broadway show',
        ['tickets', 'broadway'],
        'fantastiks',
        'fantasticks',
        'a little night music',
        'grand duke',
    ],
    FOOD: [
        'ingredients',
        'ice cream',
        'plutos',
        'crepevine',
        'subway',  # this is a tricky one
        'bread',
        'in n out',
        'peanut butter',
        'nob hill',
        'oreos',
        'falafel',
        'benedictions',
        'dinner',
        'chicken',
        'pasta',
        "s'mores",
        'sandwich',
        'strawberries',
        'tea',
        'sushi',
        'pizza',
        'safeway',
        'the counter',
        'groceries',
        'food',
        'pho',
        "zaneer's",
        'panera',
        'salad',
        'salmon',
        'ground beef',
        'olympus',
        'chipotle',
        'smart and final',
        'bamboo garden',
        'sliders',
        'slider',
        'brgr',
        'banh mi',
        'turkey',
        'waffles',
        'tiger noodle',
        'chinese',
        'hoagie haven',
        'fruit',
        'nectarines',
        'chic fil a',
        'blt',
        "Arby's",
        'popeyes',
        'darbar',
        'first wok',
        'burrito',
        'donut',
        'byrek',
        'biscuit',
        'juice',
        'sauce',
        'cream cream',
        'creme',
        'burger',
        'tangerines',
        'slices',
        'pot belly',
        'lunch',
        'vending machine',
        'tacos',
        'thai',
        'challah',
        'pancakes',
        'bacon',
        'cookie',
        'brisket',
        'wendys',
        'bagel',
        'milk',
        'deli',
        'chips',
        'french fries',
        'despana',
        'shrimp',
        'starbucks',
        'fries',
        'pita',
        'breakfast',
        'meatball',
        'pancake',
        'plum',
        'plums',
        'peach',
        'boka',
        'pinche',
        'duck at uva',
        'hill country',
        'nectarine',
        'shackburger',
        'doritos',
        'macaron',
        'lucky',
        'diner',
        'foods',
        'homegrown',
        'dumplings',
        'chocolate',
        'vino',
        'tic tok',
        'eggs',
        'seasoning',
        'toast',
        'sunny bowl',
        'guacamole',
        'twizzlers',
        'flatbread',
        'sub',
        'veggies',
        '99 ranch',
        'seoul garden',
        'baklava',
        'tomatoes',
        'latkes',
        '5 guys',
        'quiznos',
        'lays',
        'gelato',
        'bushido',
        'carabas',
        'coffee',
        'cake',
        'tortilla',
        'beef',
        'lamb',
        ['splitting', 'bill'],
        ['splitting', 'check'],
    ],
    TECHNOLOGY: [
        'aws',
        'ec2',
        'google services',
        'clock kit',
        'servos',
        'photoresistors',
        'electronics',
        'banggood',
        'domain name',
        'dx',
        'h bridge',
        'power strip',
        'teach everyone',
        'embedded systems',
    ],
    HYGEINE: [
        'laundry',
        'hair cut',
        'haircut',
        'soap',
        'detergent',
        'face wash',
        'toilet paper',
        'toothbrush',
        'deodorant',
        'clippers',
        'paper towel',
    ],
    CLOTHING: [
        'shirt',
        'jeans',
        'target top',
        'tshirt',
        'shorts',
        'uniqlo',
        'socks',
    ],
    GIFTS: [
        'gift',
        'gifts',
        ['for', 'house warming'],
        ['chocolate', 'tissues'],
        ['chocolate', 'for'],
        'laminate for',
        'markers for',
        ['for', 'birthday'],
        'card with cars',
        'east of eden',
        'wrapping',
        "surely you're joking mr feynman",
        'book for mom',
        'thank yous',
        'found',
    ],
    MEDICAL: [
        'steroid cream',
        'dermatologist',
        'fluocinonide',
        'HSA',
        'eye doctor',
        'claritin',
    ],
    TAXES: [
        'tax refund',
    ],
    HOTELS: [
        'holiday inn',
        'yotel',
        'hotel',
    ],
    DONATIONS: [
        'donation',
    ],
    EDUCATION: [
        'gre',
    ],
    INCOME: [
        'payroll',
        'paycheck',
        'interest',
        ['google', 'reimbursement'],
        ['charter', 'refund'],
    ],
}

regex = {}

def matches(word, description):
    if word not in regex:
        regex[word] = re.compile('\\b{}\\b'.format(word.lower()))
    return regex[word].search(description)

def get_categories(description):
    description = description.lower()
    my_categories = set()
    not_my_categories = set()
    for category, words_list in indicator_words.items():
        if '(not {})'.format(category) in description:
            not_my_categories.add(category)
        if '({})'.format(category) in description:
            my_categories.add(category)

        for words in words_list:
            if type(words) is str:
                words = [words]

            if all(matches(word, description) for word in words):
                my_categories.add(category)

    for category, words_list in exclusion_words.items():
        for words in words_list:
            if type(words) is str:
                words = [words]

            if all(matches(word, description) for word in words):
                not_my_categories.add(category)

    for category, subcategories_list in subcategories.items():
        for subcategory in subcategories_list:
            if subcategory in my_categories:
                my_categories.add(category)

    return my_categories - not_my_categories

def main():

    descriptions = [
        ('tickets for skiing for me and alex', [ENTERTAINMENT]),
        ('gourmet 360 burrito at Las Vegas airport', [FOOD]),
        ('uber sjc to apartment', [TRANSPORTATION]),
        ('payroll', [INCOME]),
        ('toll to boreal (5, 2 back)', [TRANSPORTATION]),
        ('in n out and gas money for Andrew for Tahoe', [FOOD]),
        ('groceries', [FOOD]),
        ('from alex for ski ticket', [ENTERTAINMENT]),
        ('toothbrush at Safeway and groceries', [FOOD, HYGEINE]),
        ('amazon for the month', [TECHNOLOGY]),
        ('skating and rental', [ENTERTAINMENT, SPORTS]),
        ('(account value)', []),
        ('movie ticket', [MOVIES, ENTERTAINMENT]),
        ('crepevine', [FOOD]),
        ('haircut', [HYGEINE]),
        ('bread', [FOOD]),
        ('benedictions to Erica', [FOOD]),
        ('subway (shows as 6.57 on statement)', [FOOD]),
        ('ice cream', [FOOD]),
        ('towel, detergent, hangers', [HYGEINE]),
        ('Caltrain SF to MTV', [TRANSPORTATION]),
        ('to Yolanda for Korean dinner at totoro', [FOOD]),
        ('times arrow book on iPhone', [BOOKS, ENTERTAINMENT]),
        ('book of mormon (not book)', [THEATER, ENTERTAINMENT]),
    ]

    for description, expected_categories in descriptions:
        my_categories = get_categories(description)
        print("    ('{description}', [{categories}]),".format(
            description=description,
            categories=', '.join(category.upper() for category in my_categories),
        ))

        if expected_categories is not None:
            assert set(expected_categories) == set(my_categories), '{} != {}'.format(expected_categories, my_categories)

if __name__ == '__main__':
    main()
