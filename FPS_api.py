from __future__ import print_function
import argparse
import torch
import process_stylization_image
from photo_wct import PhotoWCT
from photo_gif import GIFSmoothing
from photo_smooth import Propagator
from PIL import Image 
p_wct = PhotoWCT()
p_wct.load_state_dict(torch.load('./PhotoWCTModels/photo_wct.pth'))
p_pro_fast = GIFSmoothing(r=35, eps=0.001)
p_pro_slow = Propagator()
def FPS(content_image, style_image, content_seg = None, style_seg = None, fast_smooth = True):
    if fast_smooth:
        p_pro = p_pro_fast
    else:
        p_pro = p_pro_slow
    return process_stylization_image.stylization(
        stylization_module = p_wct,
        smoothing_module = p_pro,
        content_image_path = content_image,
        style_image_path = style_image,
        content_seg_path = content_seg,
        style_seg_path = style_seg,
        cuda=1,
    )

################################################################
# test api #
con = Image.open('./images/times.png').convert('RGB')
sty = Image.open('./images/punkstyle.png').convert('RGB')
outim = FPS(con,sty)
outim.save('./results/example5.png')