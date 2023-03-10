# import modules
import qrcode
from PIL import Image


def generador_qr():
    # taking image which user wants
    # in the QR code center
    Logo_link = 'ssc.jpg'

    logo = Image.open(Logo_link)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # taking url or text
    url2 = 'https://www.ssc.cdmx.gob.mx/'
    url = 'https://www.ssc.cdmx.gob.mx/storage/app/media/Convocatorias/Convocatoria_reclutamiento_analista_tactico.pdf'
    # adding URL or text to QRcode
    QRcode.add_data(url)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = '#A93226'

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code generated
    title = 'New QRCodeX'+'.png'
    QRimg.save(title)

    print('QR code generated!')
