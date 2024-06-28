FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl

RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    sh Miniconda3-latest-Linux-x86_64.sh

RUN conda install pytorch torchvision torchaudio cpuonly -c pytorch

#RUN pip install --upgrade pip && pip install \
#    pytorch-lightning \
#    timm \
#    pytorch-segmentation-models

WORKDIR /app

COPY . .

CMD ["python main.py"]