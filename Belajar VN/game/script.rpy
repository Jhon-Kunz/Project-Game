# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Koharu", color="#cf08ee")
default player_name = ""
define j = Character("[player_name]", color="#0842f0")
image splash = "logo.png"

label splashscreen:
    scene black
    with Pause(1)
    
    show splash at truecenter with dissolve
    with Pause(2)
    
    
    hide splash with dissolve
    with Pause(1)

    return 

# Game start 

label start:
    call screen name_input_screen
    if player_name.strip() == "":
        $ player_name = "Jhon-kun"

    play music good_morning fadein 2.0
    scene bedroom day with fade
    "'Terbangun dari tidur...'"

    j "Hoaammmm....."
    j "Jam berapa ini?..."
    "'Mengambil handphone untuk melihat jam'"
    j "Walah..{w=0.5}, udah jam segini aja, aku harus segera bersiap"
    "Aku pun bergegas untuk mandi, mengenakan seragam sekolah dan hanya mengunyah sepotong roti untuk sarapan"

label street:
    scene street day with fade
    j "Semoga saja aku tidak terlambat hari ini.."
    j "Tadi berangkat jam 7:00, gerbang sekolah ditutup jam 07:30...{w=0.5} semoga saja sempat.."
    "Saat aku berjalan, aku mendengar seorang gadis memanggilku..."
    "Suaranya cukup familiar untuk diriku,suaranya merdu dan ceria.."
    "Aku pun menoleh ke belakang...."

    show koharu upset with moveinleft
    k "akhirnya kekejar juga..."
    k "kamu mah ga mau nungguin aku..."
    k "aku samperin ke rumah kamu dan kata ibu kamu, kamu sudah berangkat..."

    "Ternyata gadis itu adalah Koharu.."
    "Dia adalah teman masa kecilku...{w=0.4}, kami menghabiskan waktu bermain bersama dulu..."
    "Sekarang dia satu sekolah denganku"
    "Bisa dibilang....{w=0.7}, dia adalah primadona kelas dan cukup populer di sekolah"
    "Bahkan seluruh laki-laki di sekolah nge-fans banget dengan dia"

    j "Loh?{w=0.5}, aku kira kamu sudah berangkat dari awal"
    j "tumben banget kamu telat seperti ini?"

    show koharu embarassed
    "'Muka memerah...'"
    k "e-eh?!..{w=0.8}e-hmm"
    k "a-aku telat bangun tadi..."
    "Aku sedikit terkejut dan bingung pada saat itu juga...."
    "Biasanya Koharu tidak pernah bangun telat.."
    j "ohh...{w=0.2},begitu ya...."

    show koharu happy
    k "Jhon..."
    j "ya?..."
    k "Mau jalan ke sekolah bareng ga?..."
    j" huhh?..."

    show koharu sad
    k "Kita kan jarang banget jalan bareng kamu tau...."
    k "kamu selalu suka bangun telat..." 
    "Melihat ekspresi Koharu, ada rasa sedikit menyesal didalam diriku karena sering bangun telat"
    "Tentang jalan bersama pun dia benar...{w=0.6}, sudah lama aku tidak jalan ke sekolah bersama dengannya..."
    k "Jadi....{w=0.7}, kamu mau ga?...."

    menu:
        "Jalan bareng...":
            jump jalan_bareng

    label jalan_bareng:
        show koharu happy with dissolve
        k "Serius..!?" 
        k "Kalau gitu,{w=0.5}yuk jalan..."
        j "Eh,i-iya iya..."
        "Setelah itu, kami pun berangkat bersama ke sekolah"

    label sekolah:
        play music school fadein 2.0
        scene school hallway day with fade
        "'Sesampainya di sekolah'"

        show koharu blush with dissolve
        k "Hihi..~"
        j "Kenapa ketawa?"

        show koharu happy
        k "eh!?...{w=0.3}, bukan apa apa kok...." 
        k "kamu...{w=0.5}, kelihatan beda aja, hihi"

        menu(time=10.0, timeout="too_slow"):
            "Perasaan aku sama aja deh":
                jump awkward
            "Oh...":
                jump btw
        
        label awkward:
            show koharu embarassed with dissolve
            k "ehmm, lupakan"
        
        label btw:
            show koharu happy with dissolve
            k "btw, kamu suka olahraga apa sih?"
        
        label too_slow:
            show koharu upset with dissolve
            k "kok diem aja sih"
        
       