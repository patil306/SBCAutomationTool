#!/bin/bash

sh Inbound_Basic_UAS_recorder.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder1.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder2.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder3.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder4.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder5.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder6.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder7.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder8.sh 2&>/dev/null &
sh Inbound_Basic_UAS_recorder9.sh 2&>/dev/null &
sh Inbound_Basic_UAS.sh 2&>/dev/null &
sleep 10
sh Inbound_Basic_UAC.sh
