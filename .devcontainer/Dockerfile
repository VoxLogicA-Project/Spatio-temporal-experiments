FROM ubuntu:24.10

RUN apt update
RUN apt -y dist-upgrade
RUN apt -y install git git-lfs wget make

# RUN wget https://packages.microsoft.com/config/ubuntu/23.10/packages-microsoft-prod.deb 
# RUN dpkg -i packages-microsoft-prod.deb

RUN apt update
RUN apt -y install dotnet-sdk-9.0 zip python3 python3-pip python3-venv ffmpeg htop

#RUN adduser spatiotemporal
# RUN mkdir /home/spatiotempora
# RUN chown ubuntu /home/ubuntu
# WORKDIR /home/ubuntu

WORKDIR /home/ubuntu 

USER ubuntu

RUN git clone -b voxlogica2-2024 --single-branch https://github.com/vincenzoml/VoxLogicA.git VoxLogicA2
RUN (cd /home/ubuntu/VoxLogicA2/src && dotnet build -c release)

RUN git clone -b experimental --single-branch https://github.com/vincenzoml/VoxLogicA.git
RUN (cd /home/ubuntu/VoxLogicA/src && make release)

RUN python3 -m venv /home/ubuntu/venv
RUN /home/ubuntu/venv/bin/pip3 install sk-video
RUN /home/ubuntu/venv/bin/pip3 install scikit-image
RUN /home/ubuntu/venv/bin/pip3 install numpy
ENV PATH="/home/ubuntu/venv/bin:$PATH"


