FROM mcr.microsoft.com/dotnet/core/runtime:2.2 

ENV NEO_VERSION=2.10.3 
ENV NEO_DATA=/home/neo/data

RUN apt-get update && apt-get install -y \
  screen \
  libleveldb-dev \
  sqlite3 \
  unzip \
  gosu
RUN rm -rf /var/lib/apt/lists/*
COPY docker-entrypoint.sh /entrypoint.sh

RUN useradd -m neo &&\
  mkdir /home/neo/data

WORKDIR /home/neo
RUN curl  -SLO https://github.com/neo-project/neo-cli/releases/download/v${NEO_VERSION}/neo-cli-linux-x64.zip &&\
  unzip neo-cli-linux-x64.zip &&\
  rm neo-cli-linux-x64.zip &&\
  chown -R neo neo-cli
RUN script /dev/null

WORKDIR /home/neo/neo-cli
COPY --chown=neo config.json config.json
VOLUME /home/neo/data

ENTRYPOINT ["/entrypoint.sh"]
CMD ["screen","-DmS","node","dotnet","neo-cli.dll","-r"]

