#!/bin/bash

cd nis
java -Xms2G -Xmx2G -cp ".:./*:../libs/*" org.nem.deploy.CommonStarter
cd -
