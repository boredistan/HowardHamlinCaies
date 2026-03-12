from datetime import *
from PIL import Image, ImageDraw, ImageFont
#find the dates
#daysTillTwentyFourth
print("The date today is", date.today())
twentyFourth = date.fromisoformat("2026-04-24")
daysTillTwentyFourth = twentyFourth - (date.today())
#get days left in integer form
daysTillTwentyFourth = str(int((daysTillTwentyFourth.total_seconds())/3600/24))
print(f"days till 24th of april: {daysTillTwentyFourth}")
#daysTillNineJune
NineJune = date.fromisoformat("2026-06-09")
daysTillNineJune = NineJune - (date.today())
daysTillNineJune = str(int((daysTillNineJune.total_seconds())/3600/24))
print(f"days till 9th of June: {daysTillNineJune}")
#Image
filename = "template.png"
img = Image.open(filename)
#for 24 april
d1 = ImageDraw.Draw(img)
#for 9 june
d2 = ImageDraw.Draw(img)
Font = ImageFont.truetype('Ubuntu-Regular.ttf', 128)
d1.text((512, 256), daysTillTwentyFourth, fill=(255,0,0), font = Font)
d2.text((512, 470), daysTillNineJune, fill=(10,255,50), font = Font)
img.show()
dateToday = str(date.today())
print(dateToday)
img.save(f"Results/{dateToday}.png")

 
