import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://discord.com/invite/uwAjHAG")
img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="./logoDiscord.png",
    module_drawer=RoundedModuleDrawer(1),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),
        center_color=(0, 0, 0),
        edge_color=(88, 101, 242),
    ),
)
img.save("QQRcode_Discord.png")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://www.facebook.com/curieosity.curieosity.3")
img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="./logoFacebook.png",
    module_drawer=RoundedModuleDrawer(1),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),
        center_color=(0, 0, 0),
        edge_color=(59, 89, 152),
    ),
)
img.save("QQRcode_Facebook.png")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://www.instagram.com/curieosity.su/?hl=fr")
img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="./logoInstagram.png",
    module_drawer=RoundedModuleDrawer(1),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),
        center_color=(0, 0, 0),
        edge_color=(178, 49, 185),
    ),
)
img.save("QQRcode_Instagram.png")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://linktr.ee/curieosity")
img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="./logo.png",
    module_drawer=RoundedModuleDrawer(1),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),
        center_color=(0, 0, 0),
        edge_color=(0, 0, 0),
    ),
)
img.save("QQRcode_linktree.png")

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://docs.google.com/forms/d/1_b-KhY9AAr72oIGTGAzjWcjVtsVd_TRz38VOWIrFGRk/edit?usp=drivesdk")
img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="./logo.png",
    module_drawer=RoundedModuleDrawer(1),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),
        center_color=(0, 0, 0),
        edge_color=(0, 0, 0),
    ),
)
img.save("QQRcode_inscription.png")
