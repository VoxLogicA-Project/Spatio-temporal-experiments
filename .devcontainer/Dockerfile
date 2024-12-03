FROM ubuntu:24.10

RUN apt update
RUN apt -y dist-upgrade
RUN apt -y install git git-lfs wget make

RUN wget https://packages.microsoft.com/config/ubuntu/23.10/packages-microsoft-prod.deb 
RUN dpkg -i packages-microsoft-prod.deb

RUN apt update
RUN apt -y install dotnet-sdk-8.0
RUN apt -y install zip

RUN apt -y install python3 python3-pip

RUN cd ..
RUN git clone -b voxlogica2-2024 --single-branch https://github.com/vincenzoml/VoxLogicA.git VoxLogicA2
RUN cd VoxLogicA2/src && dotnet build

RUN cd ..
RUN git clone -b experimental --single-branch https://github.com/vincenzoml/VoxLogicA.git
RUN cd VoxLogicA/src && make release

USER ubuntu
