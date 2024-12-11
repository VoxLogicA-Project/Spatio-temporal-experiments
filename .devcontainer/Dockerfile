FROM ubuntu:24.10

RUN apt update
RUN apt -y dist-upgrade
RUN apt -y install git git-lfs wget make

RUN wget https://packages.microsoft.com/config/ubuntu/23.10/packages-microsoft-prod.deb 
RUN dpkg -i packages-microsoft-prod.deb

RUN apt update
RUN apt -y install dotnet-sdk-8.0
RUN apt -y install zip

RUN adduser spatiotemporal
WORKDIR /home/spatiotemporal

RUN cd /home/spatiotemporal
RUN git clone -b voxlogica2-2024 --single-branch https://github.com/vincenzoml/VoxLogicA.git VoxLogicA2
RUN cd VoxLogicA2/src && dotnet build
RUN cd ..

RUN git clone -b experimental --single-branch https://github.com/vincenzoml/VoxLogicA.git
RUN cd VoxLogicA/src && make release

RUN apt -y install python3 
RUN apt -y install python3-pip
RUN apt -y install python3-venv
RUN apt -y install ffmpeg

RUN chown -R spatiotemporal VoxLogicA
RUN chown -R spatiotemporal VoxLogicA2
RUN mkdir /venv
RUN chown -R spatiotemporal /venv
USER spatiotemporal

RUN python3 -m venv /venv

#RUN mkdir /pyib
#RUN export PATH=$PATH:/pylib/.local/bin
#ENV PYTHONPATH=/pylib

#RUN python3 -m pip install --upgrade pip

RUN /venv/bin/pip3 install sk-video
RUN /venv/bin/pip3 install scikit-image
RUN /venv/bin/pip3 install numpy

ENV PATH="/venv/bin:$PATH"
