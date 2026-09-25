from PIL import Image, ImageDraw, ImageFont

W, H = 900, 260
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
title = ImageFont.truetype(FONT_BOLD, 48)
sub = ImageFont.truetype(FONT, 24)
small = ImageFont.truetype(FONT_BOLD, 16)
frames = []
slides = [
    ("COME PLAY", "Spades Online  /  game night", (241, 183, 233)),
    ("MAKE SOME NOISE", "Music Mash Lab  /  your sound", (246, 207, 112)),
    ("TAKE A LITTLE DETOUR", "Haunt City  /  after dark", (255, 167, 122)),
    ("MAKE SOMETHING NEW", "GLB Factory  /  3D ideas", (130, 221, 222)),
    ("FOLLOW THE NUMBERS", "Bettin2Win  /  odds made clearer", (169, 193, 255)),
]

for i, (headline, caption, accent) in enumerate(slides):
    im = Image.new("RGB", (W, H), (19, 17, 39))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((22, 22, W - 22, H - 22), radius=27, fill=(32, 27, 59), outline=(91, 77, 124), width=2)
    d.ellipse((680, -90, 1010, 240), outline=accent, width=3)
    d.ellipse((720, -50, 970, 200), outline=(100, 82, 137), width=2)
    d.ellipse((765, -5, 925, 155), fill=accent)
    d.text((58, 48), "DACAMERAGIRL  /  SHOWCASE", font=small, fill=(246, 207, 112))
    d.text((54, 87), headline, font=title, fill=(255, 251, 255))
    d.text((58, 166), caption, font=sub, fill=accent)
    for j in range(5):
        color = accent if j == i else (88, 79, 111)
        d.rounded_rectangle((58 + j * 36, 222, 82 + j * 36, 228), radius=3, fill=color)
    frames.append(im)

frames[0].save("assets/showcase-banner.gif", save_all=True, append_images=frames[1:], duration=[1500] * len(frames), loop=0, optimize=True)
