import io
import av
import torch
import numpy as np
from PIL import Image
import base64

# This is PromptServer of ComfyUI
from server import PromptServer

class Mp4VideoSaveNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "fps": ("INT", {"default": 24, "min": 1, "max": 60, "step": 1}),
                "quality": ("INT", {"default": 23, "min": 0, "max": 51, "step": 1}),
            }
        }

    RETURN_TYPES = ("VIDEO_BUFFER",)
    RETURN_NAMES = ("video_buffer",)
    FUNCTION = "images_to_video_buffer"
    CATEGORY = "video"
    OUTPUT_NODE = True

    def images_to_video_buffer(self, images, fps=24, quality=23):
        """
        Convert image tensor batch to mp4 video buffer
        images: tensor of shape [batch, height, width, channels]
        """

        # Convert tensor to numpy and handle format
        if isinstance(images, torch.Tensor):
            # ComfyUI format: [batch, height, width, channels] normalized 0-1
            img_array = images.cpu().numpy()
            img_array = (img_array * 255).astype(np.uint8)

        batch_size, height, width, channels = img_array.shape

        # Create in-memory buffer
        buffer = io.BytesIO()

        # Setup av container writing to buffer
        container = av.open(buffer, mode='w', format='mp4')

        stream = container.add_stream('h264', fps)
        stream.width = width
        stream.height = height
        stream.pix_fmt = 'yuv420p'
        stream.options = {'crf': str(quality)}

        # Process each frame
        for i in range(batch_size):
            # Get single frame
            frame_data = img_array[i]

            # Convert to PIL for av compatibility
            if channels == 3:
                pil_img = Image.fromarray(frame_data, 'RGB')
            elif channels == 4:
                pil_img = Image.fromarray(frame_data, 'RGBA')
                pil_img = pil_img.convert('RGB')  # h264 doesn't do alpha
            else:
                raise ValueError(f"Unsupported channel count: {channels}")

            # Create av frame from PIL
            frame = av.VideoFrame.from_image(pil_img)

            # Encode frame
            for packet in stream.encode(frame):
                container.mux(packet)

        # Flush encoder
        for packet in stream.encode():
            container.mux(packet)

        # Close container
        container.close()

        # Get buffer data
        buffer.seek(0)
        video_data = buffer.getvalue()
        buffer.close()

        # Send data to client for download
        PromptServer.instance.send_sync("server_client_data", {
            # Triggering Files Download
            "files": [{
                # Setting the file name
                "filename": "testing.mp4",
                # Setting the data
                "data": base64.b64encode(video_data).decode('utf-8'),
                # Setting the format
                "format": "mp4"
            }]
        })

        return (video_data,)