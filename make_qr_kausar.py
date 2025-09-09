# # Demo.py
# import PasswordGenerator  # This is your file/module name

# Secret = PasswordGenerator.generate()  # Call function properly
# print("Password of mine is:", Secret)
# save as make_qr_kausar.py
from PIL import Image, ImageDraw, ImageFont
import qrcode

# --------- EDIT THIS URL to your GitHub Pages link ----------
url = "https://your-username.github.io/14-aug-countdown/"
# ------------------------------------------------------------

# Create QR (high error correction)
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#0b8a3e", back_color="white").convert("RGBA")

# Create logo circle
w = img.size[0]
logo_size = int(w * 0.22)   # ~22% (safe)
logo = Image.new("RGBA", (logo_size, logo_size), (255,255,255,0))
draw = ImageDraw.Draw(logo)
# white circle
draw.ellipse((0,0,logo_size,logo_size), fill=(255,255,255,255))
# thin green ring
ring_w = max(4, int(logo_size * 0.06))
draw.ellipse((ring_w,ring_w,logo_size-ring_w,logo_size-ring_w), outline=(11,138,62,255), width=ring_w)

# Add text "KAUSAR" centered
try:
    font = ImageFont.truetype("arial.ttf", size=int(logo_size*0.20))
except:
    font = ImageFont.load_default()
text = "KAUSAR"
bbox = draw.textbbox((0, 0), text, font=font)  # (left, top, right, bottom)
tw = bbox[2] - bbox[0]  # width
th = bbox[3] - bbox[1]  # height

draw.text(((logo_size-tw)/2,(logo_size-th)/2), text, font=font, fill=(11,138,62,255))

# Paste logo into QR center
pos = ((w-logo_size)//2, (w-logo_size)//2)
img.paste(logo, pos, logo)

# Save
img.save("qr_kausar.png")
print("Saved qr_kausar.png. Test scanning it.")
