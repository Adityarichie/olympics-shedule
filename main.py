from flask import Flask, render_template, request

app = Flask(__name__)

names = ["Rishit", "Avani", "Shrishti", "Akshaat", "Izan", "Sohan", "Soham", "Nupur", "Pranshu", "Joel", "Gagan", "Amogh", "Vriddhi", "Zara", "Siri", "Vilekhya", 
            'Panshul', 'Shivani', 'Sujith', 'Krishna', 'Aashritha', 'Abhya', 'Navaankur', 'Fassil', 'Garv', 'Sayuj', 'Saqib', 'Sanu', 'Amani', 'Zahra', 'Shlok', "Shasvin", "Jia", 'Apoorva'
            'Rishika']

Rishit = """My mannn Top G, homie - You are wayy better than anyone bro
           We met in euroo..What we were like 2nd grade or something, we were like the coolest backbenchers bro 😂\n
           we used bully so many kids hahahahha it was fun, we did bunk classes, play fb like gods and yeah ofc we were the strongest in the whole grade hehehe like 
           we literally beat anyone in arm wrestling bro like litrally anyone sheesh, and those days were fun when we used talk back to teachers in a logical way and they would get pissed hahahah
           we were literally not scared of anyoneeee, too gud bro\n
           I rate you like 9999999999 out of 10 bro, Euro was fun all because of you, you always had my back - love you bro, its like i've known you forever bro
           we did soo many stuff broo, i can keep writing forevr no jokes and yes ofc we'l contniue to grind
           and become millionaires - its gonna be so funnn yeeeeeee \n 
           See you at the Top Bro!"""

Avani = """
    Ayyy, my first crushhh - best frnd, my therapist 😂💀\n
    We too met in euro huh, end of 5th grade. We were in the same club i forgot the name but yeah \n
    that was the first time i saw u and then in those snack/lunch breaks ofc 😂and then the magnetic train thingy if u remember 
    and those trips damn, it was so fun back then all with shrishti also 😂😂, but ofc it got messed up in the end of 6th grade 
    all covid n shit, but yeah we again started talking in 8th huhh, so many pranks huh, stuff got so intense and funny hahaha, all
    on discord damnn, ngl all the days i talked to you, it was worth it - they were pretyy gud \n
    You are like 10/10 yo

    """


Shrishti = """
    Wasup yo - you are like a good friend who anyone would wanna have
    we never really got along properly 😂, but yeah we talked so muchhh in these past years 
    but yeah the best memories were in 6thh, times were so gud, but hahah even after that 
    like 2 years back or a year idk, but yeah it was fun, all the long convo we had late night till 4am
     bout meeting n all, bout euro, you sending all voice msggg heheh and yeah we had so many fights, pranks on DC
    we made so many gprs, i would simply leave n again join, random drama we used to have bro 
    i rate you like 8/10, cause i never really got along with u hehe

    """


Akshat = """
    AHHAHAHAHAHA - BITCH, suck grass ah - u r gay frnd, we in same apt huh
    its funny how we have gone so far away places that too cycling hahahha
    ik ur gay n all but im not ok - because of u only so much last day last im telling 
    and that last day is never there - last day ill eat junk n it keeps exteneding wow 
    we would have cycled easily like 500km till now in these past years, like 100 times going 
    to phoenix, forum, lakefront, city and random places 
    we spent also so much for no reason - easy aournd 60-70k, ULTIMATE BUCKET 🤣, sting, sippie, red bull
    wow too gud, but we got screwed also like that, very gud 
    come today last day 😂 - "" MOMO time wow hahahaha ", its very hard da, getting rich🤣
    """


Izan = """
    Wasup bro, so much we talked huh bout business, self improvement n all 
    all those terrace talks, writing down time table, parkour n all, planning bout future
    writing all business ideas, grinding n all, gymming also so much n all - damnn we leveled up
    so much looking at our past, reading all the psychology hahah too gud bro 
    it might not look that gud rn but looking at our past we have like 1000 x growth easily 
    ik we both will become super rich soon ofc 
    till then, we'l grinddd, it will be hard 😂 but thats gud  
    """


Sohan = """
    way too gud u r bro, so much playing of fb, CLASH ROYALE 😂, it was fun bro
    even all those nights were we were talking bout me, all the advice - too gud bro 🤣 and ofc even the gym bro
    so much me, u, sanjay & navaankur used to grind all that 5am gymm ahhhhh too guddddd
    all tho we known each other for like wat 1-2 year, the bond is too gud bro, ur like my elder brother only
    soo gud how we ordered whey, earphones, this that to your house n go to your to house to use it cause uk my parents 😂
    its so gud that u shifted to endeavour bro - 

    """


Soham = """
    wasup skinny bitchhhhh, we met like a year back huhhh 
    so much talking, gym o my gawd in a year only we did so much 
    idk how u got so big triceps n all - all genetics bro 😂, we talked so much 
    bout how we r gonna improve, how will get rich, psychology and what not 
    even doing push ups pr, handstand - damn, we r always learning 1 thing or the other from 
    each other, and also you've helped so much in the gym correct my form this that 
    its a gud thing that u shifted here, ik ur not here anymore but wat u r like 5 mins away 
    so come off when ever ur free - we'l learn planche n alll 
    grinddd off till then huhhhh
    """


Nupur = """
    Wasuppp skinny ladie, soo much gym n all u told u'll do starting this year, what happened huh
    uk wen u think bout it u r like a mutual frnd, u never came down just because u were dating 😏
    now u will be, wat u guys r always talking thats why, - no - we used to play also ok, so eat grass thas it
    heheh all the morning tennis were pretty fun, uk cause i always bear u heheh, im too gud ik
    i still owe u a shawarma uk - but since u forgot it,, ill eat it myself - ik u wont remember why i owe u so i dont owe u 
    thas it 😂, ik ur gay n all, secret's safe wit me heheheh
    come off to endeavour to PLAY sometimes ok - 
    """


Praanshu = """
    Ay yo - ive known you since i was born huh 😂, since i was like 2-3 years old 
    back in regency n stuff, so much football, this that we used to play back then 
    all with garv, sanjay, even snakes bro 😂, like uk uk when it was raining and a snake 
    fell on ur head and u just took n threw it huh 💀, then yeah we shifted to endeavour 
    we used to play so much clash royale i remember, u r the one who told me this game in the " private van " hahahah
    bro that guy gunnie, madan or someshit hahahah wow they were so gay, but yeah later i beat u haha in clash royale 
    and then u stoped coming down only - but now its peacee cause u r there to play virus or someshit when ur free
    and bro ur guitar skilla >>>>> way too gud, like damn - randomly u can play way too hard stuff so easily like how 
    and yes ur teaching me, ill get to ur level someday somedayyy
    comeee down more tho for playing somethingg - 
    """


Joel = """
    My man, my best frnd no jokes, my bad bro 
    i recorded u by "MISTAKE" doing the snake dance 😂
    u unlike the others, u r always there in the night, like anywhere in the dark ur there
    but cheating bro, we could never reallt catch u while we were playing hide n seek cause it used to be 
    dark and u  could easily camoflage like cheating bro 
    u shifted huh 
    damn nice nice 
    ok 
     """


Gagan = """
    wasup bro Gym bro 
    always flexing with ur strength huhhhhh
    i mean yeah ofc ur pretty strong only, stronger than all of us n shit
    u r like the anime dictionary like, i like it how u used to explain these 
    diff types of animes, for like 30, 45 mins - all baki n all i still remember 
    come to endeavour bro for gym n alll
    and give treat again 😂 that was fun fs heheheheh 
    u used to like literally carry me like i was nothing - like damn 
    nice broo, get more stonger become larry wheels hehehe-
    """


Amogh = """
    wasupppp brooo, you r my good frnd bro, we met in euro huh
    i used to tell u all the rumours n all remember 
    in those private van times, damn hahahahha it used to be fun 
    but the best part used to be when we used to play fb against other classes bro 
    like our combo we used to easily beat anyone, damn gud bro - 
    we had so much back then bro, we'l meet someday again, so fun stuff
    atbb with ur studies bro, ik VERY EASY for u - smartass but yeaa - u r like 10/10 bro
    """


Vriddhi = """
    Ayyy yo, shortie 😂, its funny how we met each other and how it all started
    all that prank, and then ended up in me again getting back to u and to starting it all over huh
    we met irl wen we played badminton huh, i beat u hehehehhehe, im taller and older than u remember hehe
    from there we started talking more, i gave u a nickname remember - im so gud hehe, ngl all those times 
    When i came over to your house and chilled it was pretty fun, how we pulled diff types of pranks from my acc 💀the good thing is ur chill, cool which is gud 
    the best thing is u did not see my galary 💀, i mean u did but not totally huh, u were like thisss close but ofc 
    im fast uk, im too gud 😂, i beat u in valo also rememberr hehehehehheehe
    okay so anyways, atb with ur sports yooo, we'l meet again somedayyyy till then 
    byeeeeeeee
    """


Zara = """
    ay yo, we met online huh because siri huh, we started talking so much online 
    damn ngl it was fun, even those fights between u and siri because of me wow 
    u r a gud frnd i agree, we talked so much on dc, bout this that, how we aint ever giving up n shit huh
    and bout we r gonna level up n meet the tates n stuff huh
    but wrong situation and wrong timing ruined stuff  

    """


Siri = """
    its funny how it all started yo, insta - and then u coming over to my apt n all damn 
    we did not talk much ye, mostly insta and once irl i remember 
    ik things never really settled between us but yeah me thinking of it now 
    its all peacee
    """


Vilekhya = """
    ay yo, i got to know u because of ur bro ofc, and ur frnds lol 
    we dont talk much ye, cause we dont have any interesting mutual ground n stuff 
    and yeee i did make the mango dish u told me to, remember, i forgot to tell u but yea
    i did make it, it was pretty gud but later that day i had something to do or something ig so i forgot bout it
    thas why i didn't tell u, bout how it turned out n shit but yes, im looking forward to getting to u know u better ✌️
    """


Panshul = """
    we were in the same school huh, and we in the same apt, we dont talk much these days 
    but yeah ur a peaceful guy 
    we'l catch up someday -
    """


Shivani = """
    you are not really my frnd ok - but yea, we live in the same apt 
    asdfghjkl; -
    """

Navaankur = """

"""

Sujith = """
    Wasup my boy
    """


Sanu = """
    Wat is up bro 
    """


Jia = """
    Ay yoo
    """


Shlok = """
        Wasup boss
    """


Apoorva = """
        Remember me huh
    """


Shasvin = """
        wasup man 
    """


Zahra = """
        WOW
    """


Krishna = """
        HALO
    """


Saqib = """
        Ay yo wasup bro 
    """


Sayuj = """
        Ayyyy yoooo 
    """


Aashritha = """
        Ayy hi
    """


Garv = """
        Wasup monster back guy 
    """


Fassil = """
        You are white
    """


Abhya = """
        Heyy
    """

Amani = """
        Hiii
    """

    
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def login():
    data = str(request.form["name"])
    if data.capitalize() not in names:
        return render_template("error.html")
    elif data.capitalize() == "Rishit":
        return render_template("friends.html", friend=Rishit, name="Rishit")
    elif data.capitalize() == "Avani":
        return render_template("friends.html", friend=Avani, name="Avani")
    elif data.capitalize() == "Amogh":
        return render_template("friends.html", friend=Amogh, name="Amogh")
    elif data.capitalize() == "Shrishti":
        return render_template("friends.html", friend=Shrishti, name="Shrishti")
    elif data.capitalize() == "Akshat":
        return render_template("friends.html", friend=Akshat, name="Akshat")
    elif data.capitalize() == "Sohan":
        return render_template("friends.html", friend=Sohan, name="Sohan")
    elif data.capitalize() == "Sanu":
        return render_template("friends.html", friend=Sanu, name="Sanu")
    elif data.capitalize() == "Izan":
        return render_template("friends.html", friend=Izan, name="Izan")
    elif data.capitalize() == "Soham":
        return render_template("friends.html", friend=Soham, name="Soham")
    elif data.capitalize() == "Navaankur":
        return render_template("friends.html", friend=Navaankur, name="Navaankur")
    elif data.capitalize() == "Nupur":
        return render_template("friends.html", friend=Nupur, name="Nupur")
    elif data.capitalize() == "Pranshu":
        return render_template("friends.html", friend=Praanshu, name="Praanshu")
    elif data.capitalize() == "Joel":
        return render_template("friends.html", friend=Joel, name="Joel")
    elif data.capitalize() == "Gagan":
        return render_template("friends.html", friend=Gagan, name="Gagan")
    elif data.capitalize() == "Vriddhi":
        return render_template("friends.html", friend=Vriddhi, name="Vriddhi")
    elif data.capitalize() == "Zara":
        return render_template("friends.html", friend=Zara, name="Zara")
    elif data.capitalize() == "Siri":
        return render_template("friends.html", friend=Siri, name="Siri")
    elif data.capitalize() == "Vilekhya":
        return render_template("friends.html", friend=Vilekhya, name="Vilekhya")
    elif data.capitalize() == "Panshul":
        return render_template("friends.html", friend=Panshul, name="Panshul")
    elif data.capitalize() == "Vilekhya":
        return render_template("friends.html", friend=Vilekhya, name="Vilekhya")
    elif data.capitalize() == "Shivani":
        return render_template("friends.html", friend=Shivani, name="Shivani")
    elif data.capitalize() == "Sujith":
        return render_template("friends.html", friend=Sujith, name="Sujith")
    elif data.capitalize() == "Krishna":
        return render_template("friends.html", friend=Krishna, name="Krishna")
    elif data.capitalize() == "Aashritha":
        return render_template("friends.html", friend=Aashritha, name="Aashritha")
    elif data.capitalize() == "Abhya":
        return render_template("friends.html", friend=Abhya, name="Abhya")
    elif data.capitalize() == "Fassil":
        return render_template("friends.html", friend=Fassil, name="Fassil")
    elif data.capitalize() == "Garv":
        return render_template("friends.html", friend=Garv, name="Garv")
    elif data.capitalize() == "Sayuj":
        return render_template("friends.html", friend=Sayuj, name="Sayuj")
    elif data.capitalize() == "Saqib":
        return render_template("friends.html", friend=Saqib, name="Saqib")
    elif data.capitalize() == "Amani":
        return render_template("friends.html", friend=Amani, name="Amani")
    elif data.capitalize() == "Zahra":
        return render_template("friends.html", friend=Zahra, name="Zahra")
    elif data.capitalize() == "Shlok":
        return render_template("friends.html", friend=Shlok, name="Shlok")
    elif data.capitalize() == "Shasvin":
        return render_template("friends.html", friend=Shasvin, name="Shasvin")
    elif data.capitalize() == "Jia":
        return render_template("friends.html", friend=Jia, name="Jia")
    elif data.capitalize() == "Apoorva":
        return render_template("friends.html", friend=Apoorva, name="Apoorva")


if __name__ == "__main__":
    app.run(port=1143, debug=True)

