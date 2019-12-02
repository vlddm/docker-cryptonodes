#!/bin/bash

cd nis
java -Xms4G -Xmx4G -cp ".:./*:../libs/*" org.nem.deploy.CommonStarter
cd -
