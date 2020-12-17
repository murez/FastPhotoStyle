from FPS_api import FPS
import os
from PIL import Image

files = os.listdir("qfr_out")
for file in files:
    con = Image.open('./qfr_out/'+file).convert('RGB')
    sty = Image.open('./images/style1.png').convert('RGB')
    outim = FPS(con,sty)
    outim.save('./qfr_cyber/'+file)