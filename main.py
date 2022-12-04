from segno import helpers

# The function segno.helpers.make_vcard() returns QR code which encodes an information as vCard version 3.0

qrcode = helpers.make_vcard(
    name='Lunina; Anastasia',
    displayname='Anastasia Lunina',
    email='lunina.anastasiya@gmail.com',
    url=['https://www.linkedin.com/in/anastasia-lunina/',
         'https://github.com/AnastasiaLunina',
         'https://anastasia-codes.netlify.app/'],
    city='NYC',
    country='USA',
    title='Fullstack Software Developer',
    photo_uri='https://drive.google.com/uc?export=download&id=1VKqkCI4F57AlPNjCUN71HGVm9ZDrEkAj',
    phone='6314063798',
    memo='',
)

qrcode.save('my-vcard.png', scale=3)


