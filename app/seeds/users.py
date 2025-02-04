from app.models import db, User
import datetime


# Adds a demo user, you can add other users here if you want
def seed_users():
    Sean = User(first_name='Sean', last_name='Pan', work='Soundbook', location='Santa Clara, CA', education='University of California, Davis', email='seanhpan@gmail.com', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640671558/sean%20profile/ydp144b-scene_z55mm6.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640671558/sean%20profile/269896008_333738648345712_8581279171827465648_n_kjrjtf.jpg', password='password', birthday=datetime.date(1992, 9, 6), gender='Male')
    demo = User(first_name='O\'Shea', last_name='Jackson Sr.', bio='NWA, from the bottom now we here', work='Interscope Records', location='Compton, CA', education='William Howard High School',  email='ojackson@gmail.com', alias='Ice Cube', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1639647559/ice%20cube%20nwa/LwoaE.0.0_uzqoe9.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1639647173/ice%20cube%20nwa/image_ok9xkp.jpg', birthday=datetime.date(1969, 6, 15), gender='Male')
    Dre = User(first_name='Andre', last_name='Young', work='Aftermath Entertainment', location='Compton, CA', education='John C. Fremont High School', email='ayoung@gmail.com', alias='Dr. Dre', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640124937/dr%20dre%20nwa/beats_e2abep.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640124937/dr%20dre%20nwa/profilepic_dvybnf.jpg', birthday=datetime.date(1965, 2, 18), gender='Male')
    Kanye = User(first_name='Kanye', last_name='West', work='Def Jam', location='Atlanta, GA', education='Chicago State University', email='kwest@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640149113/kanye%20profile/-1x-1_zdkdaf.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640149112/kanye%20profile/2000_qpsl4j.jpg', birthday=datetime.date(1977, 6, 8), gender='Male')
    Ariana = User(first_name='Ariana', last_name='Grande', work='Republic', location='Boca Raton, FL', education='Pine Crest School', email='agrande@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640126351/ariana%20grande/image_ex43rp.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640126349/ariana%20grande/Ariana_Grande_at_the_2020_Grammy_Awards_yf1j2y.jpg', birthday=datetime.date(1993, 6, 26), gender='Female')
    Lisa = User(first_name='Lalisa', last_name='Manobal', work='Blackpink', location='Buriram, Thailand', education='YG Entertainment', email='lmanobal@gmail.com', alias='Lisa (Blackpink)',  password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640128206/lisa%20profile/blackpink_gettyimages-1136588782_d13div.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640128206/lisa%20profile/87e3680db94fa0baa744017596863653_mo0bzt.jpg', birthday=datetime.date(1997, 3, 27), gender='Female')
    Britney = User(first_name='Britney', last_name='Spears', work='RCA', location='McComb, MI', education='Parklane Academy', email='bspears@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640130520/britney%20profile/britney_spears_piece_of_me_show_dxhkzy.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640130173/britney%20profile/britneyspears-t_vpyd0v.jpg', birthday=datetime.date(1981, 12, 2), gender='Female')
    Weeknd = User(first_name='Abel', last_name='Tesfaye', work='Republic', location='Toronto, Ontario', education='West Hill Collegiate Institute', email='atesfaye@gmail.com', alias='The Weeknd', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640132073/weeknd%20profile/dc88d812-ab5d-416d-96a4-0d41e3e5c3e7_1400451_TABLET_LANDSCAPE_LARGE_16_9_e669it.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640132078/weeknd%20profile/NINTCHDBPICT000622131528_eyatcl.jpg', birthday=datetime.date(1990, 2, 16), gender='Male')
    Justin = User(first_name='Justin', last_name='Beiber', work='Def Jam', location='London, Ontario', education='Jeanne Sauvé Catholic School', email='jbeiber@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640134603/justin%20profile/d2959961-cc88-4697-8aca-3911aeb8e15e_1557231_TABLET_LANDSCAPE_LARGE_16_9_ikkazf.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640134710/justin%20profile/justin_bieber_2015_photo_courtesy_dfree_shutterstock_348418241_croppedjpg_cdxzbr.jpg', birthday=datetime.date(1994, 3, 1), gender='Male')
    Taylor = User(first_name='Taylor', last_name='Swift', work='Republic', location='West Reading, PA', education='Hendersonville High School', email='tswift@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640150413/taylor%20profile/gettyimages-499012194_bpvuzn.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640150411/taylor%20profile/3447_xpfbom.jpg', birthday=datetime.date(1989, 12, 13), gender='Female')
    Eminem = User(first_name='Marshall', last_name='Mathers', work='Aftermath', location='Detroit, MI', education='Lincoln High School', email='mmathers@gmail.com', alias='Eminem', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640152844/eminem%20profile/W5HOCEOFWZRT64NHD3CD7C6LGE_s2dcgi.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640152845/eminem%20profile/shutterstock_1632717139_lk2uep.jpg', birthday=datetime.date(1972, 10, 17), gender='Male')
    Tiësto = User(first_name='Tijs', last_name='Verwest', work='Spinnin\' Records', location='North Brabant, Netherlands', education='Crestwood High School', email='tverwest@gmail.com', password='password', alias='Tiësto', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640961975/tiesto%20profile/JoeJanet_Hakkasan_1.12.19_HighRes-1418_ljc8pq.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640961974/tiesto%20profile/159475286_288144352669750_4424639999113244932_o_ws0yjc.jpg', birthday=datetime.date(1969, 1, 17), gender='Male')
    Michael = User(first_name='Michael', last_name='Jackson', work='MJJ Productions', location='Gary, IN', education='Ashbury High School', email='mjackson@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640964134/michael%20jackson%20profile/Hero_Jackson5_photoKevinMazur_xbclkh.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640963560/michael%20jackson%20profile/224840_gppnl5.jpg', birthday=datetime.date(1958, 8, 29), gender='Male')
    Chester = User(first_name='Chester', last_name='Bennington', work='Linkin Park', location='Palos Verdes Estates, CA', education='Vista Verde High School', email='cbennington@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640965997/chester%20profile/161040-liking-park-chester-bennington-from-lp_zmdf1c.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640965998/chester%20profile/170720142840-01-chester-bennington-0720-restricted_ngqjqq.jpg', birthday=datetime.date(1976, 3, 20), gender='Male')
    Mariah = User(first_name='Mariah', last_name='Carey', work='Butterfly MC', location='Huntington, NY', education='Harborfields High School', email='mcarey@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640967141/mariah%20profile/mariah-carey-aiwfc-kids-today-mainv3-191220_xd288m.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640967139/mariah%20profile/MARIAH_CAREY_press-cr-dennis-leupold-billbaord-1548-1609268547_if8g2m.jpg', birthday=datetime.date(1969, 3, 27), gender='Female')
    Gaga = User(first_name='Stefani', last_name='Germanotta', work='Monster Cable Products', location='New York City, NY', education='Tisch School of the Arts', email='sgermanotta@gmail.com', password='password', alias='Lady Gaga', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640967698/lady%20gaga%20profile/Lady_20Gaga_iqel3f.png', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640967696/lady%20gaga%20profile/lady-gaga-2019-2000_f6jqlh.jpg', birthday=datetime.date(1986, 3, 28), gender='Female')
    Kendrick = User(first_name='Kendrick', last_name='Lamar', work='Top Dawg Productions', location='Compton, CA', education='Centennial High School', email='klamar@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640968216/kendrick%20profile/download_knwdhl.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640968217/kendrick%20profile/mgid_ao_image_mtv_m6xp9g.jpg', birthday=datetime.date(1987, 6, 17), gender='Male')
    Billie = User(first_name='Billie', last_name='Eilish', work='Interscope Records', location='Los Angeles, CA', education='Home', email='beilish@gmail.com', password='password', cover_photo='https://res.cloudinary.com/photofinder/image/upload/v1640968897/billie%20profile/133991_yclt2a.jpg', profile_pic='https://res.cloudinary.com/photofinder/image/upload/v1640968897/billie%20profile/billie_eilish_ejwmla.jpg', birthday=datetime.date(2001, 12, 18), gender='Female')
    # Tiësto = User(first_name='', last_name='', work='', location='', education='', email='', password='password', alias='', cover_photo='', profile_pic='', birthday=datetime.date(1969, 1, 17), gender='Male')
    # Tiësto = User(first_name='', last_name='', work='', location='', education='', email='', password='password', alias='', cover_photo='', profile_pic='', birthday=datetime.date(1969, 1, 17), gender='Male')
    # Tiësto = User(first_name='', last_name='', work='', location='', education='', email='', password='password', alias='', cover_photo='', profile_pic='', birthday=datetime.date(1969, 1, 17), gender='Male')



    db.session.add(Sean)
    db.session.add(demo)
    db.session.add(Dre)
    db.session.add(Kanye)
    db.session.add(Ariana)
    db.session.add(Lisa)
    db.session.add(Britney)
    db.session.add(Weeknd)
    db.session.add(Justin)
    db.session.add(Taylor)
    db.session.add(Eminem)

    db.session.add(Tiësto)
    db.session.add(Michael)
    db.session.add(Chester)
    db.session.add(Mariah)
    db.session.add(Gaga)
    db.session.add(Kendrick)
    db.session.add(Billie)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
