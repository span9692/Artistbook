from app.models import db, Post

def seed_posts():
    post1 = Post(post_content='testing...testing...1 2 3', owner_id=1, profile_id=1)
    post2 = Post(post_content='It\'s up and running!! 😱', owner_id=1, profile_id=1)
    post3 = Post(post_content='Welcome to Soundbook!', owner_id=1, profile_id=1)
    post4 = Post(post_content='What\'s good Soundbook, I\'m Ice Cube and I\'m Straight Outta Compton', owner_id=2, profile_id=2)
    post5 = Post(post_content='Soundbook what\'s good, Dre here', owner_id=3, profile_id=3)
    post6 = Post(post_content='Who\'s the genius behind this site?', owner_id=4, profile_id=4)
    post7 = Post(post_content='Woah this is awesome!', owner_id=6, profile_id=6)
    post8 = Post(post_content='Hi Soundbook! It\'s Lisa from Blackpink! 😄', owner_id=6, profile_id=6)
    post9 = Post(post_content='Yo this site is lit', owner_id=3, profile_id=3)
    post10 = Post(post_content='Hi Mr. Ice Cube!', owner_id=6, profile_id=2)
    post11 = Post(post_content='Hey everyone, Kendrick here', owner_id=17, profile_id=17)
    post12 = Post(post_content='Hi everyone, I\'m Billie Eilish!', owner_id=18, profile_id=18)
    post13 = Post(post_content='You good bro?', owner_id=17, profile_id=4)
    post14 = Post(post_content='Hi everyone!! 😄', owner_id=7, profile_id=7)
    post15 = Post(post_content='This site is crisppp', owner_id=8, profile_id=8)
    post16 = Post(post_content='Wow this site is amazinggg', owner_id=9, profile_id=9)
    post17 = Post(post_content='Wow this site\'s dope', owner_id=17, profile_id=17)
    post18 = Post(post_content='Let\'s collab sometime 😊', owner_id=9, profile_id=5)
    post19 = Post(post_content='Woah there\'s so many cool people on here!', owner_id=10, profile_id=10)
    post20 = Post(post_content='I\'m sorry Taylor ☹️', owner_id=4, profile_id=10)
    post21 = Post(post_content='What\'s good my brotha', owner_id=17, profile_id=8)
    post22 = Post(post_content='got a new album coming soon, can anyone guess the title of the album?', owner_id=8, profile_id=8)
    post23 = Post(post_content='What\'s good, Shady here', owner_id=11, profile_id=11)
    post24 = Post(post_content='Ready to rip the stadium next week?', owner_id=17, profile_id=11)
    post25 = Post(post_content='Hi everyone, I\'m Tiësto', owner_id=12, profile_id=12)
    post26 = Post(post_content='Thanks for the add, I\'m a huge fan', owner_id=9, profile_id=6)
    post27 = Post(post_content='This site is beautiful!!!', owner_id=16, profile_id=16)
    post28 = Post(post_content='Hey everyone, I\'m Chester', owner_id=14, profile_id=14)
    post29 = Post(post_content='Nice meeting you last week!', owner_id=12, profile_id=18)
    post30 = Post(post_content='Hey everyone, I\'m Michael', owner_id=13, profile_id=13)
    post31 = Post(post_content='You gon be at Coachella this year?', owner_id=11, profile_id=12)
    post32 = Post(post_content='Linkin Park 💯', owner_id=16, profile_id=14)
    post33 = Post(post_content='Omfgggg Britneyyyy!', owner_id=7, profile_id=16)
    post34 = Post(post_content='Hi Soundbook! I\'m Mariah Carey', owner_id=15, profile_id=15)
    post35 = Post(post_content='What\'s good Dre?', owner_id=8, profile_id=3)
    post36 = Post(post_content='Hey Kanye 😊', owner_id=15, profile_id=4)
    post37 = Post(post_content='When\'s the new album coming out?', owner_id=14, profile_id=13)
    post38 = Post(post_content='What up King?', owner_id=11, profile_id=13)
    post39 = Post(post_content='I grew up listening to you music', owner_id=18, profile_id=14)
    post40 = Post(post_content='New tour starting next month!', owner_id=5, profile_id=5)
    post41 = Post(post_content='Hey Blinks! Thanks for all the support, we love you guys ❤️', owner_id=6, profile_id=6)
    post42 = Post(post_content='You\'re so sweet!', owner_id=16, profile_id=15)
    post43 = Post(post_content='Love your music Gaga', owner_id=4, profile_id=16)
    post44 = Post(post_content='Your last album was 🔥', owner_id=10, profile_id=17)
    post45 = Post(post_content='Luv your hair', owner_id=5, profile_id=18)
    post46 = Post(post_content='Long as I\'m Shady, he\'s gonna have have to live in my shadow', owner_id=11, profile_id=11)
    post47 = Post(post_content='Unce unce unce', owner_id=12, profile_id=12)
    post48 = Post(post_content='Got a dope track, think you should get on it', owner_id=3, profile_id=2)
    post49 = Post(post_content='Gon be in Vegas next weekend, hmu', owner_id=11, profile_id=3)
    post50 = Post(post_content='Hi Mariah, you\'re super pretty!', owner_id=6, profile_id=15)
    post51 = Post(post_content='You were AMAZING in A Star Is Born', owner_id=7, profile_id=16)
    post52 = Post(post_content='What else is in your DNA?', owner_id=4, profile_id=17)
    post53 = Post(post_content='Omg I can\'t stop listening to your music', owner_id=6, profile_id=18)
    post54 = Post(post_content='Ay what\'s good Kanye?', owner_id=9, profile_id=4)
    post55 = Post(post_content='Let\'s go shopping next week!', owner_id=18, profile_id=5)
    post56 = Post(post_content='I\'m freeeeeeeeee!!!!!!', owner_id=7, profile_id=7)
    post57 = Post(post_content='You\'re so cute!', owner_id=10, profile_id=6)
    post58 = Post(post_content='I\'m so happy for you Britney!', owner_id=5, profile_id=7)
    post59 = Post(post_content='What you working on these days?', owner_id=14, profile_id=9)
    post60 = Post(post_content='Hey Abel, I love your music', owner_id=16, profile_id=8)
    post61 = Post(post_content='Gonna kick it with Luda this week if you wanna come thru', owner_id=11, profile_id=9)
    post62 = Post(post_content='Omg I love your hair!', owner_id=16, profile_id=10)
    post63 = Post(post_content='Yo Em, you heard MGK quit rapping?', owner_id=9, profile_id=11)
    post64 = Post(post_content='You and Ava look amazing in the music vid 😄', owner_id=7, profile_id=12)
    post65 = Post(post_content='You\'re an inspiration', owner_id=16, profile_id=13)
    post66 = Post(post_content='Thanks for the add, always been a fan of your music', owner_id=17, profile_id=14)
    post67 = Post(post_content='Hi Taylor, I\'m a long time fan!', owner_id=18, profile_id=10)
    post68 = Post(post_content='Lovin the new track!', owner_id=18, profile_id=12)
    post69 = Post(post_content='Omfgggggggggg it\'s Chesterrrrrr', owner_id=14, profile_id=5)
    post70 = Post(post_content='Woah KDot!', owner_id=9, profile_id=17)
    post71 = Post(post_content='Heard the news! Let\'s go!!', owner_id=18, profile_id=7)
    post72 = Post(post_content='What you up to nowadays?', owner_id=14, profile_id=8)
    post73 = Post(post_content='I like you\'re new stuff', owner_id=12, profile_id=9)
    post74 = Post(post_content='Sup Cube?', owner_id=17, profile_id=2)
    post75 = Post(post_content='Christmas is over! See you all next year!', owner_id=15, profile_id=15)
    post76 = Post(post_content='Pete ain\'t even funny.', owner_id=4, profile_id=4)
    post77 = Post(post_content='Omg you\'re so pretty!', owner_id=6, profile_id=5)
    post78 = Post(post_content='Yo Em what rhymes with orange', owner_id=3, profile_id=11)
    post79 = Post(post_content='How do you wake up Lady Gaga?', owner_id=18, profile_id=16)
    post80 = Post(post_content='How you walk forward and move backwards at the same time??', owner_id=9, profile_id=13)
    post81 = Post(post_content='What color should I dye my hair next?', owner_id=18, profile_id=18)
    post82 = Post(post_content='Nice meeting you last weekend! Where the rest of the girls at???', owner_id=5, profile_id=6)
    post83 = Post(post_content='Yo Dre', owner_id=2, profile_id=3)


    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.add(post11)
    db.session.add(post12)
    db.session.add(post13)
    db.session.add(post14)
    db.session.add(post15)
    db.session.add(post16)
    db.session.add(post17)
    db.session.add(post18)
    db.session.add(post19)
    db.session.add(post20)
    db.session.add(post21)
    db.session.add(post22)
    db.session.add(post23)
    db.session.add(post24)
    db.session.add(post25)
    db.session.add(post26)
    db.session.add(post27)
    db.session.add(post28)
    db.session.add(post29)
    db.session.add(post30)
    db.session.add(post31)
    db.session.add(post32)
    db.session.add(post33)
    db.session.add(post34)
    db.session.add(post35)
    db.session.add(post36)
    db.session.add(post37)
    db.session.add(post38)
    db.session.add(post39)
    db.session.add(post40)
    db.session.add(post41)
    db.session.add(post42)
    db.session.add(post43)
    db.session.add(post44)
    db.session.add(post45)
    db.session.add(post46)
    db.session.add(post47)
    db.session.add(post48)
    db.session.add(post49)
    db.session.add(post50)
    db.session.add(post51)
    db.session.add(post52)
    db.session.add(post53)
    db.session.add(post54)
    db.session.add(post55)
    db.session.add(post56)
    db.session.add(post57)
    db.session.add(post58)
    db.session.add(post59)
    db.session.add(post60)
    db.session.add(post61)
    db.session.add(post62)
    db.session.add(post63)
    db.session.add(post64)
    db.session.add(post65)
    db.session.add(post66)
    db.session.add(post67)
    db.session.add(post68)
    db.session.add(post69)
    db.session.add(post70)
    db.session.add(post71)
    db.session.add(post72)
    db.session.add(post73)
    db.session.add(post74)
    db.session.add(post75)
    db.session.add(post76)
    db.session.add(post77)
    db.session.add(post78)
    db.session.add(post79)
    db.session.add(post80)
    db.session.add(post81)
    db.session.add(post82)
    db.session.add(post83)

    db.session.commit()


def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()
