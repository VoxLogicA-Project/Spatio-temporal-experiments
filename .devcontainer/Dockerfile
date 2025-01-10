FROM ubuntu:24.10

RUN apt update
RUN apt -y dist-upgrade
RUN apt -y install git git-lfs wget make

# RUN wget https://packages.microsoft.com/config/ubuntu/23.10/packages-microsoft-prod.deb 
# RUN dpkg -i packages-microsoft-prod.deb

RUN apt update
RUN apt -y install dotnet-sdk-9.0 zip python3 python3-pip python3-venv ffmpeg htop

#RUN adduser spatiotemporal
RUN mkdir /home/spatiotemporal
RUN chown ubuntu /home/spatiotemporal
WORKDIR /home/spatiotemporal

USER ubuntu

RUN git clone -b voxlogica2-2024 --single-branch https://github.com/vincenzoml/VoxLogicA.git VoxLogicA2
RUN (cd /home/spatiotemporal/VoxLogicA2/src && dotnet build -c release)

RUN git clone -b experimental --single-branch https://github.com/vincenzoml/VoxLogicA.git
RUN (cd /home/spatiotemporal/VoxLogicA/src && make release)

RUN python3 -m venv /home/spatiotemporal/venv
RUN /home/spatiotemporal/venv/bin/pip3 install sk-video
RUN /home/spatiotemporal/venv/bin/pip3 install scikit-image
RUN /home/spatiotemporal/venv/bin/pip3 install numpy
ENV PATH="/home/spatiotemporal/venv/bin:$PATH"
