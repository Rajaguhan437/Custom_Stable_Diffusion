#%%

import gradio as gr
import torch
from torch import autocast
from diffusers import StableDiffusionImg2ImgPipeline

import inspect
import warnings
from typing import List, Optional, Union
from tqdm.auto import tqdm

import requests
from PIL import Image
from io import BytesIO

#%%

#%%


device = "cuda"
model_id = "guhan/1000" 
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

"""
g_cuda = torch.Generator(device='cuda')
seed = 52362
g_cuda.manual_seed(seed)
"""

# %%
def inference(prompt, negative_prompt="", num_samples=10, num_inference_steps=50, guidance_scale=8.5, strenght=.5, url=None):
    response = requests.get(url)
    init_image = Image.open(BytesIO(response.content)).convert("RGB")
    init_image = init_image.resize((512, 512))
    with torch.autocast("cuda"), torch.inference_mode():
        return pipe(
                prompt,
                negative_prompt=negative_prompt,
                image=init_image, 
                strength=0.5,
                num_images_per_prompt=int(num_samples),
                num_inference_steps=int(num_inference_steps), 
                guidance_scale=guidance_scale,
                #generator=g_cuda
            ).images
        
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(label="Prompt", value="((photo of guhan)) , man ,modelshoot style, (extremely detailed CG unity 8k wallpaper), professional majestic oil painting by Ed Blinkey, Atey Ghailan, Studio Ghibli, by Jeremy Mann, Greg Manchess, Antonio Moro, trending on ArtStation, trending on CGSociety, Intricate")
            negative_prompt = gr.Textbox(label="Negative Prompt", value="woman, nudes,B&W, logo, Watermark, bad artist, blur, blurry, text, b&w, 3d, bad art, poorly drawn, disfigured, deformed, extra limbs, ugly hands, extra fingers, canvas frame, cartoon, 3d, disfigured, bad art, deformed, extra limbs, weird colors, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, ugly, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, out of frame, ugly, extra limbs, bad anatomy, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, mutated hands, fused fingers, too many fingers, long neck, Photoshop, video game, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, bad art, bad anatomy, 3d render")
            with gr.Row():
                num_samples = gr.Number(label="Number of Samples", value=4)
                guidance_scale = gr.Number(label="Guidance Scale", value=8.5)
            with gr.Row():
                url = gr.Textbox(label="URL",value="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flh6.googleusercontent.com%2Fproxy%2FQBZTSycU3BmNf_YnyU4vm7Ammqx-aKnQcXSr_mD5xn28buzYMdg4G4NZOoxF8-hhW-a_HenRvkeiOnwnRw4Ll0TYjcs9HehMcoFWWsCpqA5BKAQCOUeJ5yd2eXnIlcxd_F6n7dugodr4GuwtI7aNtIqETNci0EFPeyc6sgVUx4f_1wHb_RwEXRGTxbc3L5jqYbde-ArPVo4_HRuJPBhmq-hJ86M4%3Dw1200-h630-p-k-no-nu&f=1&nofb=1")
                strength = gr.Slider(label="Strength", value=.5)   
            num_inference_steps = gr.Slider(label="Steps", value=24)
            run = gr.Button(value="Generate")
        with gr.Column():
            gallery = gr.Gallery()

    run.click(inference, inputs=[prompt, negative_prompt, num_samples,  num_inference_steps, guidance_scale, strength, url], outputs=gallery)

demo.launch(debug=True,share=True)

# %%
