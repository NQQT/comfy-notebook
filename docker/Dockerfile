FROM python:3.11-slim as builder

RUN apt-get update
RUN apt-get install -y git

RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio --no-cache-dir --index-url https://download.pytorch.org/whl/cu128

WORKDIR /root
ARG COMFY_REPO="comfy-notebook"

# Installing Comfy Support
RUN git clone  https://github.com/NQQT/${COMFY_REPO}.git
RUN pip install --upgrade ${COMFY_REPO}/repository
RUN pip install --upgrade ${COMFY_REPO}/nofusion

# Installing ComfyUI
RUN python ${COMFY_REPO}/bootscript/comfy.py

RUN apt-get install -y libgl1 libglib2.0-0 libsm6 libxrender1 libxext6

RUN rm -rf /root/ComfyUI/custom_nodes/ComfyUI-Manager

# Removal of COMFY REPO
# RUN rm -rf ${COMFY_REPO}

# Final stage
FROM python:3.11-slim

# Copy only the installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /root/ /root/

WORKDIR /root

EXPOSE 8000
# Start script
CMD ["python","ComfyUI/main.py","--cpu","--port=8000","--listen"]