FROM openjdk:8-jre

ENV NIS_VERSION=0.6.97
ENV NIS_SHA256=a786ddd682f955bd7d22afd58d7cb0260105da12f9b5cfe1336f1ea11e67102b

RUN useradd -r nem \
  && apt-get update -y \
  && apt-get install -y gosu \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/nem
RUN wget https://bob.nem.ninja/nis-${NIS_VERSION}.tgz &&\ 
  echo "$NIS_SHA256  nis-${NIS_VERSION}.tgz" | sha256sum -c - &&\
  tar  -xzf nis-${NIS_VERSION}.tgz &&\
  rm -f nis-${NIS_VERSION}.tgz

WORKDIR /home/nem/package
RUN  sed -i -e 's/^nem.host =.*/nem.host = 0.0.0.0/g' -e 's/^nis.additionalLocalIps.*/nis.additionalLocalIps = *.*.*.*/g' nis/config.properties &&\
  mv nix.runConsole.sh ncc.sh

ENV NIS_DATA=/home/nem/nem
VOLUME /home/nem/nem

COPY docker-entrypoint.sh /entrypoint.sh
COPY --chown=nem nis.sh nis.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["./nis.sh"]
