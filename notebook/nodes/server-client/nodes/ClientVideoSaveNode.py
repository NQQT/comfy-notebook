import torch
import numpy as np
import av
import io

import numpy as np
from PIL import Image
# Import ComfyUI's PromptServer for client-server communication
# This allows us to send data from Kaggle (server) to the browser (client)
from server import PromptServer

class VideoSaveNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "frame_rate": ("INT", {"default": 16, "min": 1, "max": 60}),
                "codec": ("COMBO", ["libx264", "libx265", "mpeg4"],),
                "pixel_format": ("COMBO", ["yuv420p", "yuv444p"],),
            },
        }

    RETURN_TYPES = ("VIDEO_BYTES",)
    RETURN_NAMES = ("video_bytes",)
    FUNCTION = "encode_video"
    CATEGORY = "Video"

    def encode_video(self, images, frame_rate, codec, pixel_format):
        # Convert torch tensors to numpy arrays
        images_np = [np.clip(255. * img.cpu().numpy(), 0, 255).astype(np.uint8) for img in images]
        height, width, _ = images_np[0].shape

        output_memory_file = io.BytesIO()

        with av.open(output_memory_file, 'w', format='mp4') as container:
            stream = container.add_stream(codec, rate=frame_rate)
            stream.width = width
            stream.height = height
            stream.pix_fmt = pixel_format

            for img_np in images_np:
                frame = av.VideoFrame.from_ndarray(img_np, format='rgb24')
                for packet in stream.encode(frame):
                    container.mux(packet)

            # Flush stream
            for packet in stream.encode():
                container.mux(packet)

        video_bytes = output_memory_file.getvalue()

        # Send data to client for download
        PromptServer.instance.send_sync("server_client_data", {
            "files": [{
                # Setting the file name
                "filename": "test",
                # Setting the data
                "data": video_bytes,
                # Setting the format
                "format": "mp4"
            }]
        })

        return (video_bytes,)