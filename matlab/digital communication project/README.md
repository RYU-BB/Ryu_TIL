# DigitalCommunication
 이 프로젝트는 digital communication model을 구현하였다.

AWGN, AWGN+multi path 환경에서의 QPSK, 16-QAM 변조방식의 BER vs SNR, BER vs Eb/No을 그려
총 8개의 BER curve를 비교하였다.

model

송신부
 input data -> scramble -> channel encoding -> symbol mapping -> oversampling -> pulseShaping -> AWGN or AWGN + multipath channel

수신부
 tx data -> matched filter -> adc -> de modulation -> channel encoding -> scramble