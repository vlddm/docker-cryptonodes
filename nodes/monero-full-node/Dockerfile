# Usage: docker run --restart=always -v /var/data/blockchain-xmr:/root/.bitmonero -p 18080:18080 -p 18081:18081 --name=monerod -td kannix/monero-full-node
FROM ubuntu:18.04 AS build

ENV MONERO_VERSION=0.15.0.1

RUN apt-get update -y \
  && apt-get install -y curl bzip2 gnupg \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /root

RUN for key in \
    0x55432DF31CCD4FCD \
  ; do \
      gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key" || \
      gpg --batch --keyserver pgp.mit.edu --recv-keys "$key" || \
      gpg --batch --keyserver keyserver.pgp.com --recv-keys "$key" || \
      gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \
      gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" ; \
    done &&\
  curl -L -O https://getmonero.org/downloads/hashes.txt &&\
  gpg --verify hashes.txt &&\
  curl https://downloads.getmonero.org/cli/monero-linux-x64-v$MONERO_VERSION.tar.bz2 -O &&\
  grep "monero-linux-x64-v$MONERO_VERSION.tar.bz2" hashes.txt | sed 's/,/ /' | awk '{print $2 "  " $1}' | sha256sum -c - &&\
  tar -xvf monero-linux-x64-v$MONERO_VERSION.tar.bz2 &&\
  rm monero-linux-x64-v$MONERO_VERSION.tar.bz2 &&\
  cp ./monero-x86_64-linux-gnu-v$MONERO_VERSION/monero* .
  
FROM ubuntu:18.04

RUN apt-get update -y \
  && apt-get install -y gosu \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd -ms /bin/bash monero && mkdir -p /home/monero/.bitmonero && chown -R monero:monero /home/monero/.bitmonero
#USER monero
WORKDIR /home/monero

COPY --chown=monero:monero --from=build /root/monero* /home/monero/
COPY docker-entrypoint.sh /entrypoint.sh
ENV PATH=/home/monero:$PATH MONERO_DATA=/home/monero/.bitmonero

# blockchain loaction
VOLUME /home/monero/.bitmonero

EXPOSE 18080 18081

ENTRYPOINT ["/entrypoint.sh"]

CMD ["monerod", "--non-interactive", "--rpc-bind-ip=0.0.0.0", "--confirm-external-bind"]
