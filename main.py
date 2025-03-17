import telebot
from telebot import types
import requests
bot = telebot.TeleBot('6585659246:AAEMJTeganyeOYR7jP8pJwpOuGu7MPxQSFI')

start_txt = "Привет, я бот-путеводитель по интересным местам Тюмени! \n\nHi, I'm a travel bot for interesting places in Tyumen!"

user_lang = {}
user_data = {}
categories = {
    "ru": ["🎒 Школьник", "🎓 Студент", "🌍 Иностранный студент", "👨‍👩‍👧‍👦 Семья"],
    "en": ["🎒 School student", "🎓 University student", "🌍 International student", "👨‍👩‍👧‍👦 Family"]
}

sight = {
    "ru": ["🌉❤ Мост влюблённых", "🐱🪴 Сквер сибирских кошек", "🌳 Сквер Дзержинского", "🛣️ Цветной бульвар", "🏞️🚶‍♂ Набережная реки Туры",
           "⛪ Знаменский собор", "🏛️ Тюменский драматический театр", "🏛️🛢️ Музей Геологии, нефти и газа", "📜🌳 Исторический парк 'Россия – моя история'",
           "🌲🏞️ Гилевская роща" ],
    "en": ["🌉❤ Lovers' Bridge", "🐱🪴 Siberian Cats Square", "🌳 Dzerzhinsky Square", "🛣️ Tsvetnoy Boulevard", "🏞️🚶‍♂ Tura River Embankment",
            "⛪ Znamensky Cathedral", "🏛️ Tyumen Drama Theater", "🏛️🛢️ Museum of Geology, Oil, and Gas", "📜🌳 Historical Park 'Russia – My History'",
            "🌲🏞️ Gilevskaya Grove"]
        }
questions = {
    "ru": {
        "🎒 Школьник": {
            "🌉❤ Мост влюблённых": {
                "question": "Почему этот мост называют Мостом Влюбленных?",
                "answer": (
                    "Он стал символом любви из-за традиции вешать замки, а также является излюбленным местом для свиданий.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/bridges/28125)"
                )
            },
            "🐱🪴 Сквер сибирских кошек": {
                "question": "Почему в сквере столько кошек?",
                "answer": (
                    "Памятники посвящены сибирским кошкам, которых отправили в Санкт-Петербург спасать Эрмитаж от крыс.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39599)"
                )
            },
            "🌳 Сквер Дзержинского": {
                "question": "Кто такой Дзержинский?",
                "answer": (
                    "Это историческая личность, сыгравшая важную роль в начале XX века.\n\n"
                    "Подробнее можно узнать по [ссылке](https://ru.wikipedia.org/wiki/Дзержинский,_Феликс_Эдмундович)"
                )
            },
            "🛣️ Цветной бульвар": {
                "question": "Почему бульвар называется Цветным?",
                "answer": (
                    "Из-за ярких фонтанов, уличных артистов и множества развлечений.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39600)"
                )
            },
            "🏞️🚶‍♂ Набережная реки Туры": {
                "question": "Какая река здесь протекает?",
                "answer": (
                    "Это река Тура, главная водная артерия Тюмени.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39601)"
                )
            },
            "⛪ Знаменский собор": {
                "question": "Почему этот собор так важен?",
                "answer": (
                    "Он один из старейших храмов города и памятник архитектуры XVIII века.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/temples/28126)"
                )
            },
            "🏛️ Тюменский драматический театр": {
                "question": "Какие спектакли здесь ставят?",
                "answer": (
                    "В театре можно увидеть классические постановки и современные пьесы.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/theaters/28127)"
                )
            },
            "🏛️🛢️ Музей Геологии, нефти и газа": {
                "question": "Почему нефть важна для Тюмени?",
                "answer": (
                    "Тюменская область – один из крупнейших нефтедобывающих регионов России.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/28128)"
                )
            },
            "📜🌳 Исторический парк 'Россия – моя история'": {
                "question": "Можно ли здесь узнать что-то интересное о прошлом России?",
                "answer": (
                    "Да, музей наполнен интерактивными экспонатами, которые помогут лучше понять историю страны.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/39602)"
                )
            },
            "🌲🏞️ Гилевская роща": {
                "question": "Какие животные здесь водятся?",
                "answer": (
                    "В роще можно встретить белок, зайцев и множество птиц.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/parks/39603)"
                )
            }
        },
        "🎓 Студент": {
            "🌉❤ Мост влюблённых": {
                "question": "Есть ли в Тюмени популярные места для романтических встреч?",
                "answer": (
                    "Да, помимо Моста Влюбленных, такими местами считаются Цветной бульвар и набережная Туры.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/bridges/28125)"
                )
            },
            "🐱🪴 Сквер сибирских кошек": {
                "question": "Какую роль играли кошки в истории России?",
                "answer": (
                    "Они спасли произведения искусства в Эрмитаже, а также считаются символами уюта и удачи.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39599)"
                )
            },
            "🌳 Сквер Дзержинского": {
                "question": "Какие еще значимые фигуры связаны с Тюменью?",
                "answer": (
                    "С городом связаны Григорий Распутин, Дмитрий Менделеев и многие другие.\n\n"
                    "Подробнее можно узнать по [ссылке](https://ru.wikipedia.org/wiki/Дзержинский,_Феликс_Эдмундович)"
                )
            },
            "🛣️ Цветной бульвар": {
                "question": "Есть ли тут интересные культурные события?",
                "answer": (
                    "Да, здесь проходят фестивали, концерты и выступления уличных артистов.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39600)"
                )
            },
            "🏞️🚶‍♂ Набережная реки Туры": {
                "question": "Можно ли здесь заниматься спортом?",
                "answer": (
                    "Да, есть велосипедные дорожки, тренажеры и зоны для пробежек.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39601)"
                )
            },
            "⛪ Знаменский собор": {
                "question": "Какие архитектурные стили здесь использованы?",
                "answer": (
                    "Барокко с элементами классики, что делает его уникальным для Сибири.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/temples/28126)"
                )
            },
            "🏛️ Тюменский драматический театр": {
                "question": "Какие известные актеры выступали на этой сцене?",
                "answer": (
                    "Здесь выступали многие российские актеры, включая народных артистов.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/theaters/28127)"
                )
            },
            "🏛️🛢️ Музей Геологии, нефти и газа": {
                "question": "Какие технологии используют в добыче нефти?",
                "answer": (
                    "Современные методы включают горизонтальное бурение и гидроразрыв пласта.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/28128)"
                )
            },
            "📜🌳 Исторический парк 'Россия – моя история'": {
                "question": "Какие исторические периоды здесь освещены?",
                "answer": (
                    "Музей охватывает все периоды, начиная с Древней Руси и заканчивая современностью.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/39602)"
                )
            },
            "🌲🏞️ Гилевская роща": {
                "question": "Можно ли здесь заниматься активным отдыхом?",
                "answer": (
                    "Да, в парке есть велодорожки и зоны для пикников.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/parks/39603)"
                )
            }
        },
        "🌍 Иностранный студент": {
            "🌉❤ Мост влюблённых": {
                "question": "Почему люди вешают замки на этом мосту?",
                "answer": (
                    "Это традиция, символизирующая вечную любовь, вдохновленная подобными обычаями в Европе.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/bridges/28125)"
                )
            },
            "🐱🪴 Сквер сибирских кошек": {
                "question": "Почему здесь установлен памятник кошкам?",
                "answer": (
                    "Сибирские кошки были отправлены в Эрмитаж для защиты его от грызунов и стали героями истории.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39599)"
                )
            },
            "🌳 Сквер Дзержинского": {
                "question": "Кем был Дзержинский и почему этот парк назван в его честь?",
                "answer": (
                    "Феликс Дзержинский был советским политическим деятелем, и этот парк был назван в его честь в советское время.\n\n"
                    "Подробнее можно узнать по [ссылке](https://ru.wikipedia.org/wiki/Дзержинский,_Феликс_Эдмундович)"
                )
            },
            "🛣️ Цветной бульвар": {
                "question": "Что является главной достопримечательностью Цветного бульвара?",
                "answer": (
                    "Это оживленное место с фонтанами, цирком и уличными представлениями.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39600)"
                )
            },
            "🏞️🚶‍♂ Набережная реки Туры": {
                "question": "Что могут делать посетители на набережной Туры?",
                "answer": (
                    "Они могут наслаждаться прогулками, кататься на лодках или посещать местные кафе.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39601)"
                )
            },
            "⛪ Знаменский собор": {
                "question": "Чем примечателен этот собор?",
                "answer": (
                    "Это архитектурный памятник XVIII века и важный религиозный объект.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/temples/28126)"
                )
            },
            "🏛️ Тюменский драматический театр": {
                "question": "Можно ли посмотреть спектакль на другом языке?",
                "answer": (
                    "Некоторые постановки сопровождаются субтитрами или адаптированы для иностранных гостей.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/theaters/28127)"
                )
            },
            "🏛️🛢️ Музей Геологии, нефти и газа": {
                "question": "Есть ли интерактивные экспонаты?",
                "answer": (
                    "Да, в музее есть макеты, симуляторы и интерактивные панели.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/28128)"
                )
            },
            "📜🌳 Исторический парк 'Россия – моя история'": {
                "question": "Есть ли экскурсии на английском языке?",
                "answer": (
                    "Да, музей предлагает экскурсии на нескольких языках, включая английский.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/39602)"
                )
            },
            "🌲🏞️ Гилевская роща": {
                "question": "Чем Гилевская роща примечательна?",
                "answer": (
                    "Это уникальная природная зона внутри города, где можно насладиться тишиной и свежим воздухом.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/parks/39603)"
                )
            }
        },
        "👨‍👩‍👧‍👦 Семья": {
            "🌉❤ Мост влюблённых": {
                "question": "Что означает традиция вешать замки?",
                "answer": (
                    "Она символизирует прочные отношения и семейное счастье.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/bridges/28125)"
                )
            },
            "🐱🪴 Сквер сибирских кошек": {
                "question": "Почему именно сибирские кошки?",
                "answer": (
                    "Они славятся своей выносливостью и густой шерстью, идеально подходящей для холодного климата.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39599)"
                )
            },
            "🌳 Сквер Дзержинского": {
                "question": "Почему этот сквер популярен среди горожан?",
                "answer": (
                    "Этот сквер интересен своей историей, архитектурой и памятником Дзержинскому.\n\n"
                    "Подробнее можно узнать по [ссылке](https://ru.wikipedia.org/wiki/Дзержинский,_Феликс_Эдмундович)"
                )
            },
            "🛣️ Цветной бульвар": {
                "question": "Какие развлечения здесь есть для детей?",
                "answer": (
                    "Есть карусели, игровые зоны и выступления цирковых артистов.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39600)"
                )
            },
            "🏞️🚶‍♂ Набережная реки Туры": {
                "question": "Можно ли здесь устроить пикник?",
                "answer": (
                    "Да, вдоль набережной есть удобные зоны для отдыха и пикников.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39601)"
                )
            },
            "⛪ Знаменский собор": {
                "question": "Можно ли зайти внутрь собора?",
                "answer": (
                    "Да, он открыт для посетителей, внутри можно увидеть старинные иконы.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/temples/28126)"
                )
            },
            "🏛️ Тюменский драматический театр": {
                "question": "Есть ли детские спектакли?",
                "answer": (
                    "Да, театр регулярно ставит детские представления и сказки.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/theaters/28127)"
                )
            },
            "🏛️🛢️ Музей Геологии, нефти и газа": {
                "question": "Будет ли детям интересно в этом музее?",
                "answer": (
                    "Да, здесь много познавательных экспонатов, которые можно потрогать.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/28128)"
                )
            },
            "📜🌳 Исторический парк 'Россия – моя история'": {
                "question": "Будет ли детям интересно?",
                "answer": (
                    "Да, здесь есть интерактивные экраны и увлекательные видеопрезентации.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/39602)"
                )
            },
            "🌲🏞️ Гилевская роща": {
                "question": "Есть ли здесь детские площадки?",
                "answer": (
                    "Да, в парке оборудованы игровые зоны для детей.\n\n"
                    "Подробнее можно узнать по [ссылке](https://www.tourister.ru/world/europe/russia/city/tyumen/parks/39603)"
                )
            }
        }
    },
    "en": {
    "🎒 School student": {
        "🌉❤ Lovers' Bridge": {
            "question": "Why is this bridge called Lovers' Bridge?",
            "answer": (
                "It has become a symbol of love due to the tradition of hanging locks and is a favorite spot for dates.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/bridges/28125)"
            )
        },
        "🐱🪴 Siberian Cats Square": {
            "question": "Why are there so many cats in this square?",
            "answer": (
                "The monuments are dedicated to Siberian cats that were sent to St. Petersburg to save the Hermitage from rats.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39599)"
            )
        },
        "🌳 Dzerzhinsky Square": {
            "question": "Who was Dzerzhinsky?",
            "answer": (
                "He was a historical figure who played an important role in the early 20th century.\n\n"
                "More information can be found at [link](https://en.wikipedia.org/wiki/Felix_Dzerzhinsky)"
            )
        },
        "🛣️ Tsvetnoy Boulevard": {
            "question": "Why is this boulevard called Tsvetnoy?",
            "answer": (
                "Because of its bright fountains, street performers, and numerous attractions.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39600)"
            )
        },
        "🏞️🚶‍♂ Tura River Embankment": {
            "question": "Which river flows here?",
            "answer": (
                "This is the Tura River, the main waterway of Tyumen.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39601)"
            )
        },
        "⛪ Znamensky Cathedral": {
            "question": "Why is this cathedral so important?",
            "answer": (
                "It is one of the oldest churches in the city and an architectural monument from the 18th century.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/temples/28126)"
            )
        },
        "🏛️ Tyumen Drama Theater": {
            "question": "What kind of performances are staged here?",
            "answer": (
                "The theater features classical plays and modern dramas.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/theaters/28127)"
            )
        },
        "🏛️🛢️ Museum of Geology, Oil, and Gas": {
            "question": "Why is oil important for Tyumen?",
            "answer": (
                "The Tyumen region is one of the largest oil-producing regions in Russia.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/28128)"
            )
        },
        "📜🌳 Historical Park 'Russia – My History'": {
            "question": "Can you learn something interesting about Russia's past here?",
            "answer": (
                "Yes, the museum is filled with interactive exhibits that help you better understand the country's history.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/39602)"
            )
        },
        "🌲🏞️ Gilevskaya Grove": {
            "question": "What animals can be found here?",
            "answer": (
                "In the grove, you can find squirrels, hares, and many birds.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/parks/39603)"
            )
        }
    },
    "🎓 University student": {
        "🌉❤ Lovers' Bridge": {
            "question": "Are there other popular romantic spots in Tyumen?",
            "answer": (
                "Yes, besides Lovers' Bridge, Tsvetnoy Boulevard and the Tura River Embankment are also popular.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/bridges/28125)"
            )
        },
        "🐱🪴 Siberian Cats Square": {
            "question": "What role did cats play in Russian history?",
            "answer": (
                "They saved artworks in the Hermitage and are considered symbols of comfort and good luck.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39599)"
            )
        },
        "🌳 Dzerzhinsky Square": {
            "question": "What other significant figures are associated with Tyumen?",
            "answer": (
                "Grigory Rasputin, Dmitry Mendeleev, and many others are connected to the city.\n\n"
                "More information can be found at [link](https://en.wikipedia.org/wiki/Felix_Dzerzhinsky)"
            )
        },
        "🛣️ Tsvetnoy Boulevard": {
            "question": "Are there any interesting cultural events here?",
            "answer": (
                "Yes, festivals, concerts, and street performances are held here.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39600)"
            )
        },
        "🏞️🚶‍♂ Tura River Embankment": {
            "question": "Can you do sports here?",
            "answer": (
                "Yes, there are bicycle paths, exercise equipment, and jogging zones.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39601)"
            )
        },
        "⛪ Znamensky Cathedral": {
            "question": "What architectural styles are used here?",
            "answer": (
                "Baroque with elements of classicism, making it unique for Siberia.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/temples/28126)"
            )
        },
        "🏛️ Tyumen Drama Theater": {
            "question": "Which famous actors have performed on this stage?",
            "answer": (
                "Many Russian actors, including People's Artists, have performed here.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/theaters/28127)"
            )
        },
        "🏛️🛢️ Museum of Geology, Oil, and Gas": {
            "question": "What technologies are used in oil extraction?",
            "answer": (
                "Modern methods include horizontal drilling and hydraulic fracturing.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/28128)"
            )
        },
        "📜🌳 Historical Park 'Russia – My History'": {
            "question": "Which historical periods are covered here?",
            "answer": (
                "The museum covers all periods, from Ancient Rus' to modern times.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/39602)"
            )
        },
        "🌲🏞️ Gilevskaya Grove": {
            "question": "Can you engage in active recreation here?",
            "answer": (
                "Yes, the park has bike paths and picnic areas.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/parks/39603)"
            )
        }
    },
    "🌍 International student": {
        "🌉❤ Lovers' Bridge": {
            "question": "Why do people hang locks on this bridge?",
            "answer": (
                "It's a tradition symbolizing eternal love, inspired by similar customs in Europe.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/bridges/28125)"
            )
        },
        "🐱🪴 Siberian Cats Square": {
            "question": "Why is there a monument to cats here?",
            "answer": (
                "Siberian cats were sent to the Hermitage to protect it from rodents and became heroes of history.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39599)"
            )
        },
        "🌳 Dzerzhinsky Square": {
            "question": "Who was Dzerzhinsky and why is this park named after him?",
            "answer": (
                "Felix Dzerzhinsky was a Soviet political figure, and this park was named after him during Soviet times.\n\n"
                "More information can be found at [link](https://en.wikipedia.org/wiki/Felix_Dzerzhinsky)"
            )
        },
        "🛣️ Tsvetnoy Boulevard": {
            "question": "What is the main attraction of Tsvetnoy Boulevard?",
            "answer": (
                "It's a lively place with fountains, a circus, and street performances.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39600)"
            )
        },
        "🏞️🚶‍♂ Tura River Embankment": {
            "question": "What can visitors do on the Tura River Embankment?",
            "answer": (
                "They can enjoy walks, boat rides, or visit local cafes.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39601)"
            )
        },
        "⛪ Znamensky Cathedral": {
            "question": "What is notable about this cathedral?",
            "answer": (
                "It's an 18th-century architectural monument and an important religious site.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/temples/28126)"
            )
        },
        "🏛️ Tyumen Drama Theater": {
            "question": "Can you watch a performance in another language?",
            "answer": (
                "Some performances are accompanied by subtitles or adapted for foreign guests.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/theaters/28127)"
            )
        },
        "🏛️🛢️ Museum of Geology, Oil, and Gas": {
            "question": "Are there interactive exhibits?",
            "answer": (
                "Yes, the museum has models, simulators, and interactive panels.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/28128)"
            )
        },
        "📜🌳 Historical Park 'Russia – My History'": {
            "question": "Are there tours in English?",
            "answer": (
                "Yes, the museum offers tours in several languages, including English.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/39602)"
            )
        },
        "🌲🏞️ Gilevskaya Grove": {
            "question": "What is notable about Gilevskaya Grove?",
            "answer": (
                "It's a unique natural area within the city where you can enjoy silence and fresh air.\n\n"
                "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/parks/39603)"
            )
        },
    # "👨‍👩‍👧‍👦 Family": {
    #     "🌉❤ Lovers' Bridge": {
    #         "question": "What does the tradition of hanging locks mean?",
    #         "answer": (
    #             "It symbolizes strong relationships and family happiness.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/bridges/28125)"
    #         )
    #     },
    #     "🐱🪴 Siberian Cats Square": {
    #         "question": "Why specifically Siberian cats?",
    #         "answer": (
    #             "They are known for their endurance and thick fur, ideal for cold climates.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39599)"
    #         )
    #     },
    #     "🌳 Dzerzhinsky Square": {
    #         "question": "Why is this square popular among locals?",
    #         "answer": (
    #             "This square is interesting for its history, architecture, and the monument to Dzerzhinsky.\n\n"
    #             "More information can be found at [link](https://en.wikipedia.org/wiki/Felix_Dzerzhinsky)"
    #         )
    #     },
    #     "🛣️ Tsvetnoy Boulevard": {
    #         "question": "What entertainment is available for children here?",
    #         "answer": (
    #             "There are carousels, play areas, and circus performances.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39600)"
    #         )
    #     },
    #     "🏞️🚶‍♂ Tura River Embankment": {
    #         "question": "Can you have a picnic here?",
    #         "answer": (
    #             "Yes, there are convenient picnic areas along the embankment.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/placeofinterest/39601)"
    #         )
    #     },
    #     "⛪ Znamensky Cathedral": {
    #         "question": "Can you go inside the cathedral?",
    #         "answer": (
    #             "Yes, it's open to visitors, and you can see ancient icons inside.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/temples/28126)"
    #         )
    #     },
    #     "🏛️ Tyumen Drama Theater": {
    #         "question": "Are there children's performances?",
    #         "answer": (
    #             "Yes, the theater regularly stages children's plays and fairy tales.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/theaters/28127)"
    #         )
    #     },
    #     "🏛️🛢️ Museum of Geology, Oil, and Gas": {
    #         "question": "Will children find this museum interesting?",
    #         "answer": (
    #             "Yes, there are many educational exhibits that children can touch.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/28128)"
    #         )
    #     },
    #     "📜🌳 Historical Park 'Russia – My History'": {
    #         "question": "Will children find it interesting?",
    #         "answer": (
    #             "Yes, there are interactive screens and engaging video presentations.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/museum/39602)"
    #         )
    #     },
    #     "🌲🏞️ Gilevskaya Grove": {
    #         "question": "Are there playgrounds here?",
    #         "answer": (
    #             "Yes, the park has play areas for children.\n\n"
    #             "More information can be found at [link](https://www.tourister.ru/world/europe/russia/city/tyumen/parks/39603)"
    #         )
    #     }
    # }
    }
    }
}

@bot.message_handler(commands=['start'])
def start(message):
    # выводим приветственное сообщение
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ["🇷🇺 Русский", "🇬🇧 English"])
def set_lang(message):
    user_id = message.from_user.id
    remove_markup = types.ReplyKeyboardRemove()

    if message.text == "🇷🇺 Русский":
        user_lang[user_id] = "ru"
        user_data[user_id] = {}
        bot.send_message(user_id, "Вы выбрали русский язык. Идём дальше!", reply_markup=remove_markup)

    elif message.text == "🇬🇧 English":
        user_lang[user_id] = "en"
        user_data[user_id] = {}
        bot.send_message(user_id, "You have chosen English. Let's move on!", reply_markup=remove_markup)

    choose_listener(message)

def choose_listener(message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "ru")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories[lang]:
        markup.add(types.KeyboardButton(category))

    btn_back = types.KeyboardButton("⬅️ Назад" if lang == "ru" else "⬅️ Back")
    markup.add(btn_back)

    if lang == "ru":
        bot.send_message(user_id, "Выберите, кто вы:", reply_markup=markup)
    else:
        bot.send_message(user_id, "Choose your category:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in sum(categories.values(), []))
def set_listener_type(message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "ru")
    remove_markup = types.ReplyKeyboardRemove()

    user_data[user_id]["category"] = message.text

    if lang == "ru":
        bot.send_message(user_id, f"Вы выбрали: {message.text}. Давайте начнем!", reply_markup=remove_markup)
    else:
        bot.send_message(user_id, f"You chose: {message.text}. Let's get started!", reply_markup=remove_markup)

    choose_sight(message)

def choose_sight(message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "ru")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for place in sight[lang]:
        markup.add(types.KeyboardButton(place))

    btn_back = types.KeyboardButton("⬅️ Назад" if lang == "ru" else "⬅️ Back")
    markup.add(btn_back)

    if lang == "ru":
        bot.send_message(user_id, "Выберите место, которое хотите посетить", reply_markup=markup)
    else:
        bot.send_message(user_id, "Choose a place you want to visit", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in sum(sight.values(), []))
def show_sight_info(message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "ru")
    remove_markup  = types.ReplyKeyboardRemove()

    user_data[user_id]["sight"] = message.text
    if lang == "ru":
        bot.send_message(user_id, f"Итак, {message.text}. Сейчас всё узнаем!", reply_markup=remove_markup)
    else:
        bot.send_message(user_id, f"So, {message.text}. We'll find out now!", reply_markup=remove_markup)
    show_sight_details(message)


@bot.message_handler(func=lambda message: message.text in [q["question"] for q_list in questions["ru"].values()
for q in q_list.values()] + [q["question"] for q_list in questions["en"].values() for q in q_list.values()])
def handle_question(message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "ru")
    category = user_data[user_id]["category"]
    sight_name = user_data[user_id]["sight"]
    question_data = questions[lang][category][sight_name]
    answer = question_data["answer"]
    bot.send_message(user_id, answer, parse_mode="Markdown")

def show_sight_details(message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "ru")
    sight_name = user_data[user_id]["sight"]
    category = user_data[user_id]["category"]
    sight_images = {
        "ru": {
            "🌉❤ Мост влюблённых": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_65b4c85ecf428b0280462fe8_65b52918f5952b407f9ffc07/scale_1200",
            "🐱🪴 Сквер сибирских кошек": "https://avatars.mds.yandex.net/i?id=a0a58a1d89681d891d8dbe90a06d1c4e_l-10705627-images-thumbs&n=13",
            "🌳 Сквер Дзержинского": "https://static.tildacdn.info/tild6630-6330-4562-a664-633130643564/170d27adc182c8a8c3a9.jpg",
            "🛣️ Цветной бульвар": "http://rasfokus.ru/images/photos/medium/f82f25451097df495bdb172e0a07f4a2.jpg",
            "🏞️🚶‍♂ Набережная реки Туры": "https://frog72.com/upload/iblock/2b7/2b7ecd7b0b2eac65449101a6065ec421.jpg",
            "⛪ Знаменский собор": "https://avatars.mds.yandex.net/i?id=728bae0e64f8744de9f77271eb28f286_l-8206800-images-thumbs&n=13",
            "🏛️ Тюменский драматический театр": "https://img1.advisor.travel/1314x680px-Tyumenskiy_dramaticheskiy_teatr_15.jpg",
            "🏛️🛢️ Музей Геологии, нефти и газа": "https://tourism86.ucoz.net/_nw/17/57434507.jpg",
            "📜🌳 Исторический парк 'Россия – моя история'": "https://cdn.culture.ru/images/4616c291-f323-5584-9e48-93c3340ff9d9",
            "🌲🏞️ Гилевская роща": "https://baldezh.top/uploads/posts/2022-09/1662085937_2-funart-pro-p-park-gilevskaya-roshcha-pinterest-2.jpg"
        },
        "en":
            {
                "🌉❤ Lovers' Bridge": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_65b4c85ecf428b0280462fe8_65b52918f5952b407f9ffc07/scale_1200",
                "🐱🪴 Siberian Cats Square": "https://avatars.mds.yandex.net/i?id=a0a58a1d89681d891d8dbe90a06d1c4e_l-10705627-images-thumbs&n=13",
                "🌳 Dzerzhinsky Square": "https://static.tildacdn.info/tild6630-6330-4562-a664-633130643564/170d27adc182c8a8c3a9.jpg",
                "🛣️ Tsvetnoy Boulevard": "http://rasfokus.ru/images/photos/medium/f82f25451097df495bdb172e0a07f4a2.jpg",
                "🏞️🚶‍♂ Tura River Embankment": "https://frog72.com/upload/iblock/2b7/2b7ecd7b0b2eac65449101a6065ec421.jpg",
                "⛪ Znamensky Cathedral": "https://avatars.mds.yandex.net/i?id=728bae0e64f8744de9f77271eb28f286_l-8206800-images-thumbs&n=13",
                "🏛️ Tyumen Drama Theater": "https://img1.advisor.travel/1314x680px-Tyumenskiy_dramaticheskiy_teatr_15.jpg",
                "🏛️🛢️ Museum of Geology, Oil, and Gas": "https://tourism86.ucoz.net/_nw/17/57434507.jpg",
                "📜🌳 Historical Park 'Russia – My History'": "https://cdn.culture.ru/images/4616c291-f323-5584-9e48-93c3340ff9d9",
                "🌲🏞️ Gilevskaya Grove": "https://baldezh.top/uploads/posts/2022-09/1662085937_2-funart-pro-p-park-gilevskaya-roshcha-pinterest-2.jpg"
            }
                }
    sight_info = {
        "ru": {
            "🌉❤ Мост влюблённых": "Соединяет берега Туры, стал символом любви благодаря традиции вешать замки.",
            "🐱🪴 Сквер сибирских кошек": "В память о кошках, спасших Эрмитаж от нашествия грызунов.",
            "🌳 Сквер Дзержинского": "Исторический сквер, названный в честь Феликса Дзержинского.",
            "🛣️ Цветной бульвар": "Центральная прогулочная зона Тюмени с фонтанами, аттракционами и цирком.",
            "🏞️🚶‍♂ Набережная реки Туры": "Современная набережная с красивыми видами и местами для отдыха.",
            "⛪ Знаменский собор": "Один из старейших храмов Тюмени, построенный в XVIII веке.",
            "🏛️ Тюменский драматический театр": "Один из крупнейших театров Сибири, открытый в 1858 году.",
            "🏛️🛢️ Музей Геологии, нефти и газа": "Экспозиция, посвященная истории нефтяной промышленности региона.",
            "📜🌳 Исторический парк 'Россия – моя история'": "Интерактивный музейный комплекс о российской истории.",
            "🌲🏞️ Гилевская роща": "Природный парк с экологическими тропами и зонами отдыха."
             }  ,
        "en":
            {
                "🌉❤ Lovers' Bridge": "Connects the banks of the Tura River and has become a symbol of love due to the tradition of hanging locks.",
                "🐱🪴 Siberian Cats Square": "Dedicated to the cats that saved the Hermitage from a rodent invasion.",
                "🌳 Dzerzhinsky Square": "A historic square named after Felix Dzerzhinsky.",
                "🛣️ Tsvetnoy Boulevard": "The central promenade of Tyumen with fountains, attractions, and a circus.",
                "🏞️🚶‍♂ Tura River Embankment": "A modern embankment with beautiful views and places for relaxation.",
                "⛪ Znamensky Cathedral": "One of the oldest churches in Tyumen, built in the 18th century.",
                "🏛️ Tyumen Drama Theater": "One of the largest theaters in Siberia, opened in 1858.",
                "🏛️🛢️ Museum of Geology, Oil, and Gas": "An exhibition dedicated to the history of the region’s oil industry.",
                "📜🌳 Historical Park 'Russia – My History'": "An interactive museum complex about Russian history.",
                "🌲🏞️ Gilevskaya Grove": "A natural park with ecological trails and recreation areas."
            }
                }
    sight_stickers = {
        "ru": {
            "🌉❤ Мост влюблённых": "CAACAgIAAxkBAAEOGi1n2E5aIc-ZA5XaAAEEfT4pR94mOQwAAktWAAIqb6lKUpKxwEdTjQM2BA",
            "🐱🪴 Сквер сибирских кошек": "CAACAgIAAxkBAAEOGjdn2E6bIAXI71MhEf33MfgZt0lP1gACUFAAAmfQsEoh9QMPjorD2zYE",
            "🌳 Сквер Дзержинского": "CAACAgIAAxkBAAEOGj9n2E7DcYSEuThDKqNCpP3y4GNH2wACxFAAAia9sUpG23IgeHHJKTYE",
            "🛣️ Цветной бульвар": "CAACAgIAAxkBAAEOGj1n2E7B_yMg4-Jap9YU0P9ebGhQigACO1YAAkMwsEqcirX8p8GvjTYE",
            "🏞️🚶‍♂ Набережная реки Туры": "CAACAgIAAxkBAAEOGjFn2E6ElZlo1XbHPG5g0ycrU4oi_wACZFQAAo8wsUoNOVYYLEl7CzYE",
            "⛪ Знаменский собор": "CAACAgIAAxkBAAEOGjNn2E6HWRR5Tjn8OREu7Yht9TtSXwAC4FMAAuu5qEr25dxE8hyRAjYE",
            "🏛️ Тюменский драматический театр": "CAACAgIAAxkBAAEOGjln2E6e-O3I2qWYkKp1SCEbjC74aAACF1IAAvmaqUqvRnKD3jKD5DYE",
            "🏛️🛢️ Музей Геологии, нефти и газа": "CAACAgIAAxkBAAEOGkFn2E9sMXzP-eZmWwr9KbiWZuwHuwAC71cAAvnGqEqPuZBK7wEfGDYE",
            "📜🌳 Исторический парк 'Россия – моя история'": "CAACAgIAAxkBAAEOGkdn2E-qVYcBm8rvOQ3gwdKEtX6RswACKFQAAn_EqErr2g0_nEbcyjYE",
            "🌲🏞️ Гилевская роща": "CAACAgIAAxkBAAEOGkVn2E-aGJPpX4BLi2k4AAFohCVK-8AAArxQAAI6BrFKYDbnExHafV82BA"
        },
        "en": {
            "🌉❤ Lovers' Bridge": "CAACAgIAAxkBAAEOGi1n2E5aIc-ZA5XaAAEEfT4pR94mOQwAAktWAAIqb6lKUpKxwEdTjQM2BA",
            "🐱🪴 Siberian Cats Square": "CAACAgIAAxkBAAEOGjdn2E6bIAXI71MhEf33MfgZt0lP1gACUFAAAmfQsEoh9QMPjorD2zYE",
            "🌳 Dzerzhinsky Square": "CAACAgIAAxkBAAEOGj9n2E7DcYSEuThDKqNCpP3y4GNH2wACxFAAAia9sUpG23IgeHHJKTYE",
            "🛣️ Tsvetnoy Boulevard": "CAACAgIAAxkBAAEOGj1n2E7B_yMg4-Jap9YU0P9ebGhQigACO1YAAkMwsEqcirX8p8GvjTYE",
            "🏞️🚶‍♂ Tura River Embankment": "CAACAgIAAxkBAAEOGjFn2E6ElZlo1XbHPG5g0ycrU4oi_wACZFQAAo8wsUoNOVYYLEl7CzYE",
            "⛪ Znamensky Cathedral": "CAACAgIAAxkBAAEOGjNn2E6HWRR5Tjn8OREu7Yht9TtSXwAC4FMAAuu5qEr25dxE8hyRAjYE",
            "🏛️ Tyumen Drama Theater": "CAACAgIAAxkBAAEOGjln2E6e-O3I2qWYkKp1SCEbjC74aAACF1IAAvmaqUqvRnKD3jKD5DYE",
            "🏛️🛢️ Museum of Geology, Oil, and Gas": "CAACAgIAAxkBAAEOGkFn2E9sMXzP-eZmWwr9KbiWZuwHuwAC71cAAvnGqEqPuZBK7wEfGDYE",
            "📜🌳 Historical Park 'Russia – My History'": "CAACAgIAAxkBAAEOGkdn2E-qVYcBm8rvOQ3gwdKEtX6RswACKFQAAn_EqErr2g0_nEbcyjYE",
            "🌲🏞️ Gilevskaya Grove": "CAACAgIAAxkBAAEOGkVn2E-aGJPpX4BLi2k4AAFohCVK-8AAArxQAAI6BrFKYDbnExHafV82BA"
        }
                }
    bot.send_message(user_id, sight_info[lang].get(sight_name, "Информации пока нет."))
    bot.send_photo(user_id, sight_images[lang].get(sight_name, "https://example.com/default.jpg"))
    bot.send_sticker(user_id, sight_stickers[lang].get(sight_name,"CAACAgIAAxkBAAIBYWWP8UeLw3q3sQkWbZ0ZKUP1tGqOAAIFAAPANk8T1hJGQCoxf_E0BA"))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    question_data = questions[lang][category][sight_name]
    if question_data:
        markup.add(types.KeyboardButton(question_data["question"]))


    btn1 = types.KeyboardButton("➡ Далее" if lang == "ru" else "➡ Forward")
    btn_back = types.KeyboardButton("⬅️ Назад" if lang == "ru" else "⬅️ Back")
    markup.add(btn_back, btn1)
    bot.send_message(user_id, "Что вас интересует?" if lang == "ru" else "What are you interested in?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["➡ Далее", "➡ Forward"])
def handle_next(message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "ru")
    choose_sight(message)

@bot.message_handler(func=lambda message: message.text in ["⬅️ Назад", "⬅️ Back"])
def handle_back(message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "ru")

    # Определяем текущее состояние пользователя
    if "sight" in user_data[user_id]:
        # Если пользователь находится на этапе выбора достопримечательности, возвращаем его к выбору категории
        del user_data[user_id]["sight"]  # Удаляем выбранную достопримечательность
        choose_listener(message)
    elif "category" in user_data[user_id]:
        # Если пользователь находится на этапе выбора категории, возвращаем его к выбору языка
        del user_data[user_id]["category"]  # Удаляем выбранную категорию
        start(message)  # Возвращаем к выбору языка
    else:
        # Если пользователь находится на этапе выбора языка, ничего не делаем
        pass





if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print('❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌')








