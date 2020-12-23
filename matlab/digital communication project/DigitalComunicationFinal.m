BLOCK_CODE_N = 6;
BLOCK_CODE_K = 3;
CODE_RATE = BLOCK_CODE_K/BLOCK_CODE_N;
OVER_SAMPLING_RATE = 16;
ROLL_OFF_FACTOR = 0.5;

INFO_BIT = zeros(1, 1200000);   

BLOCK_GENERATOR_I = eye(BLOCK_CODE_K);
BLOCK_GENERATOR_P = [1 1 0; 0 1 1; 1 0 1];
BLOCK_GENERATOR = [BLOCK_GENERATOR_P,BLOCK_GENERATOR_I];
PARITY_CHK_MATRIX = [BLOCK_GENERATOR_I; BLOCK_GENERATOR_P];

FILTER = rcosfir(ROLL_OFF_FACTOR,[-8 8],OVER_SAMPLING_RATE,1,'sqrt');

SNR_GROUP = -50:2:50;
QPSK_EbNo = (1/CODE_RATE) * (1/log2(4)) * SNR_GROUP;
QAM_EbNo = (1/CODE_RATE) * (1/log2(16)) * SNR_GROUP;
SNR_VS_QPSK_BER = zeros(size(SNR_GROUP));
SNR_VS_QAM_BER = zeros(size(SNR_GROUP));
SNR_VS_QPSK_MUL_BER = zeros(size(SNR_GROUP));
SNR_VS_QAM_MUL_BER = zeros(size(SNR_GROUP));
i=1;

for snr = SNR_GROUP
    qpskBER = blockQpskComunication(INFO_BIT,BLOCK_CODE_K,BLOCK_CODE_N,BLOCK_GENERATOR,PARITY_CHK_MATRIX,OVER_SAMPLING_RATE,FILTER,snr);
    SNR_VS_QPSK_BER(i) = qpskBER;
    qamBER = blockQamComunication(INFO_BIT,BLOCK_CODE_K,BLOCK_CODE_N,BLOCK_GENERATOR,PARITY_CHK_MATRIX,OVER_SAMPLING_RATE,FILTER,snr);
    SNR_VS_QAM_BER(i) = qamBER;
    qpskMultiPathBER = blockQpskMulComunication(INFO_BIT,BLOCK_CODE_K,BLOCK_CODE_N,BLOCK_GENERATOR,PARITY_CHK_MATRIX,OVER_SAMPLING_RATE,FILTER,snr);
    SNR_VS_QPSK_MUL_BER(i) = qpskMultiPathBER;
    qamMultiPathBER = blockQamMulComunication(INFO_BIT,BLOCK_CODE_K,BLOCK_CODE_N,BLOCK_GENERATOR,PARITY_CHK_MATRIX,OVER_SAMPLING_RATE,FILTER,snr);
    SNR_VS_QAM_MUL_BER(i) = qamMultiPathBER;
    i=i+1;
end

subplot(2,2,1)
semilogy(SNR_GROUP,SNR_VS_QPSK_BER,'--r+',SNR_GROUP,SNR_VS_QPSK_MUL_BER,'--b+');
legend('QPSK','QPSK MUlTI PATH');
axis([min(SNR_GROUP) max(SNR_GROUP) 1e-6 1]);
xlabel('SNR [dB]');
ylabel('BER');
title('QPSK | SNR Vs BER Curve');

subplot(2,2,2)
semilogy(SNR_GROUP,SNR_VS_QAM_MUL_BER,'--c+',SNR_GROUP,SNR_VS_QAM_BER,'--g+')
legend('16-QAM MULTI PATH','16-QAM');
axis([min(SNR_GROUP) max(SNR_GROUP) 1e-6 1]);
xlabel('SNR [dB]');
ylabel('BER');
title('QAM | SNR Vs BER Curve');

subplot(2,2,3)
semilogy(QPSK_EbNo,SNR_VS_QPSK_BER,'--r+',QPSK_EbNo,SNR_VS_QPSK_MUL_BER,'--b+');
axis([min(QPSK_EbNo) max(QPSK_EbNo) 1e-6 1]);
legend('QPSK','QPSK MUlTI PATH');
xlabel('Eb/No [dB]');
ylabel('BER');
title('QPSK | Eb/No Vs BER Curve');

subplot(2,2,4)
semilogy(QAM_EbNo,SNR_VS_QAM_MUL_BER,'--c+',QAM_EbNo,SNR_VS_QAM_BER,'--g+');
axis([min(QAM_EbNo) max(QAM_EbNo) 1e-6 1]);
legend('16-QAM MULTI PATH','16-QAM');
xlabel('Eb/No [dB]');
ylabel('BER');
title('QAM | Eb/No Vs BER Curve');



function ber = blockQpskComunication(infoBit,blockCodeK,blockCodeN,blockGenerator,parityChkMatrix,overSamplingRate,filter,snr)
    scrambleCode = scramble(infoBit);
    
    code = blockEncoding(scrambleCode,blockCodeK, blockGenerator);
    
    symIdxQPSK = symbolMappingQPSK(code);
    
    symIdxOvrQPSK = overSampling(symIdxQPSK, overSamplingRate);
    pulseOutQPSK = pulseShaping(symIdxOvrQPSK,filter);
    
    txOutQPSK = awgnChannel(pulseOutQPSK,snr);
    matchedOutQPSK = matchedFilter(txOutQPSK,filter);
    
    adcOutQPSK = analogToDigitalConverter(matchedOutQPSK,overSamplingRate);
    rxBlockQPSK = deModulationQPSK(adcOutQPSK);
    
    rxBitQPSK = blockDecoding(rxBlockQPSK, blockCodeN, parityChkMatrix);
    infoQPSK = scramble(rxBitQPSK);
    
    ber = berChk(infoBit,infoQPSK);
end

function ber = blockQamComunication(infoBit,blockCodeK,blockCodeN,blockGenerator,parityChkMatrix,overSamplingRate,filter,snr)
    scrambleCode = scramble(infoBit);
    
    code = blockEncoding(scrambleCode,blockCodeK, blockGenerator);
    
    symIdxQAM = symbolMappingQAM(code);
    
    symIdxOvrQAM = overSampling(symIdxQAM, overSamplingRate);
    pulseOutQAM = pulseShaping(symIdxOvrQAM,filter);
    
    txOutQAM = awgnChannel(pulseOutQAM,snr);
    matchedOutQAM = matchedFilter(txOutQAM,filter);
    
    adcOutQAM = analogToDigitalConverter(matchedOutQAM,overSamplingRate);
    rxBlockQAM = deModulationQAM(adcOutQAM);
    
    rxBitQAM = blockDecoding(rxBlockQAM, blockCodeN, parityChkMatrix);
    infoQAM = scramble(rxBitQAM);
    
    ber = berChk(infoBit,infoQAM);
end

function ber = blockQpskMulComunication(infoBit,blockCodeK,blockCodeN,blockGenerator,parityChkMatrix,overSamplingRate,filter,snr)
    scrambleCode = scramble(infoBit);
    
    code = blockEncoding(scrambleCode,blockCodeK, blockGenerator);
    
    symIdxQPSK = symbolMappingQPSK(code);
    
    symIdxOvrQPSK = overSampling(symIdxQPSK, overSamplingRate);
    pulseOutQPSK = pulseShaping(symIdxOvrQPSK,filter);
    channelOutQPSK = propagationChannel(pulseOutQPSK);
    
    txOutQPSK = awgnChannel(channelOutQPSK,snr);
    matchedOutQPSK = matchedFilter(txOutQPSK,filter);
    
    adcOutQPSK = analogToDigitalConverter(matchedOutQPSK,overSamplingRate);
    rxBlockQPSK = deModulationQPSK(adcOutQPSK);
    
    rxBitQPSK = blockDecoding(rxBlockQPSK, blockCodeN, parityChkMatrix);
    infoQPSK = scramble(rxBitQPSK);
    
    ber = berChk(infoBit,infoQPSK);
end

function ber = blockQamMulComunication(infoBit,blockCodeK,blockCodeN,blockGenerator,parityChkMatrix,overSamplingRate,filter,snr)
    scrambleCode = scramble(infoBit);
    
    code = blockEncoding(scrambleCode,blockCodeK, blockGenerator);
    
    symIdxQAM = symbolMappingQAM(code);
    
    symIdxOvrQAM = overSampling(symIdxQAM, overSamplingRate);
    pulseOutQAM = pulseShaping(symIdxOvrQAM,filter);
    channelOutQAM = propagationChannel(pulseOutQAM);
    
    txOutQAM = awgnChannel(channelOutQAM,snr);
    matchedOutQAM = matchedFilter(txOutQAM,filter);
    
    adcOutQAM = analogToDigitalConverter(matchedOutQAM,overSamplingRate);
    rxBlockQAM = deModulationQAM(adcOutQAM);
    
    rxBitQAM = blockDecoding(rxBlockQAM, blockCodeN, parityChkMatrix);
    infoQAM = scramble(rxBitQAM);
    
    ber = berChk(infoBit,infoQAM);
end

function scrambleCode = scramble(infoBit)
    scrambleCode = zeros(1,length(infoBit));
    seed = 2016707058;                                          %seed = 학번
    rng(seed)                                                   %seed 지정
    regs = randi([0 1],1,18);                                   %2016707058 seed에 해당하는 radom bit 생성
    for i = 1:length(infoBit)                                     %scramble 반복문
        scrCode = mod(regs(end-4) + regs(end-6) + regs(3),2);   %regs의 마지막, 마지막-6, 3번째 bit를 xor연산해 scr code에 추가
        scrambleCode(i) = mod(infoBit(i)+scrCode,2);
        regs(2:end) = regs(1:end-1);                            %shift
        regs(1) = scrCode;                                      %regs첫번째 값에 scrcode값 삽입
    end
    
end

function code_ = blockEncoding(inputBit,blockCodeK, generator)
    inputBit = reshape(inputBit,blockCodeK,[]);
    inputBit = inputBit.';
    code = mod(inputBit * generator,2);
    code_ = oneRowReshape(code);
end

function symIdx_ = symbolMappingQPSK(code)
    symIdx = (1-2*code(1:2:end))+(1i*(1-2*code(2:2:end)));
    symIdx_ = symIdx/sqrt(2);
end

function symIdx_ = symbolMappingQAM(code)
    qamLut = [-3 -1 1 3];
    askIdx = code(1:2:end)*2 + code(2:2:end);
    qamIdx = qamLut(askIdx+1);
    symIdx = (qamIdx(1:2:end))+(1i*(qamIdx(2:2:end)));
    symIdx_ = symIdx/sqrt(10);
end

function symIdxOvr = overSampling(symIdx,overSamplingRate)
    symIdxOvr(1:overSamplingRate:overSamplingRate*length(symIdx))=symIdx;
end

function pulseOut = pulseShaping(symIdxOvr,filter)
   pulseOut = conv(filter,symIdxOvr);
end

function channelOut = propagationChannel(pulseOut)
    channel = [1 0 0 0 0 0 0 0 1/2];
    channelOut = conv(pulseOut,channel);
end

function txOut = awgnChannel(pulseOut,snr)
    noisePower = snr2noisePower(snr);
    txOut = pulseOut + noisePower*crandn(1,length(pulseOut))/sqrt(2);
end

function matchedOut = matchedFilter(txOut,filter)
    matchedOut = conv(filter,txOut);
end

function adcOut = analogToDigitalConverter(matchedOut,overSamplingRate)
    adcOut = matchedOut(2*overSamplingRate*(overSamplingRate/2)+1:overSamplingRate:end-2*overSamplingRate*(overSamplingRate/2));
end

function rxBlock = deModulationQAM(adcOut)
    rxBlock = zeros(1,length(adcOut)*4);
    adcOut = adcOut*sqrt(10);
    for i = 1:length(adcOut)
        realPart = real(adcOut(i));
        ImagPart = imag(adcOut(i));
        
        if realPart>2
            rxBlock((i-1)*4+1:(i-1)*4+2) = [1 1];
        end
        if realPart>=0 && realPart<=2
            rxBlock((i-1)*4+1:(i-1)*4+2) = [1 0];
        end
        if realPart>=-2 && realPart<0
            rxBlock((i-1)*4+1:(i-1)*4+2) = [0 1];
        end
        if realPart<-2
            rxBlock((i-1)*4+1:(i-1)*4+2) = [0 0];
        end
        
        if ImagPart>2
            rxBlock((i-1)*4+3:(i-1)*4+4) = [1 1];
        end
        if ImagPart>=0 && ImagPart<=2
            rxBlock((i-1)*4+3:(i-1)*4+4) = [1 0];
        end
        if ImagPart>=-2 && ImagPart<0
            rxBlock((i-1)*4+3:(i-1)*4+4) = [0 1];
        end
        if ImagPart<-2
            rxBlock((i-1)*4+3:(i-1)*4+4) = [0 0];
        end
    end
end

function rxBlock = deModulationQPSK(adcOut)                    
    rxBlock=zeros(1,length(adcOut)*2);
    
    for i = 1:length(adcOut)
    if 0<angle(adcOut(i)) && angle(adcOut(i))<= pi/2
        rxBlock((i-1)*2+1:(i-1)*2+2) = [0 0];
    end
    if pi/2<angle(adcOut(i))&& angle(adcOut(i))<=pi
        rxBlock((i-1)*2+1:(i-1)*2+2) = [1 0];
    end
    if -pi/2<angle(adcOut(i))&&angle(adcOut(i))<=0
        rxBlock((i-1)*2+1:(i-1)*2+2) = [0 1];
    end
    if -pi<angle(adcOut(i))&&angle(adcOut(i))<=-pi/2
        rxBlock((i-1)*2+1:(i-1)*2+2) = [1 1];
    end
    end
end

function ber = berChk(txInfo,rxInfo)
    errorChk = txInfo ~= rxInfo;
    ber = sum(errorChk,'all')/length(txInfo);                
end

function rxBit = blockDecoding(rxInfo, blockCodeN,parityChkMatrix)
    rxInfo = reshape(rxInfo, blockCodeN,[]);
    rxInfo = rxInfo.';
    syndrome = mod(rxInfo*parityChkMatrix,2);                                    %receive된 비트에 parity check matrix를 곱해 syndrome 확인
    syndromes = [0 0 0; 1 0 1; 0 1 1; 1 1 0; 0 0 1; 0 1 0; 1 0 0; 1 1 1];   %(6,3)block code의 syndromes
    syndromeChks = zeros(size(rxInfo,1),1);                                      %각 block의 syndrome을 체크하기 위한 행렬

for rCol = 1:size(rxInfo,1)                                                          %앞에서 찾은 syndrome으로 각 block이 무엇을 correction해야 할지 지정
    for syndromeCol = 1:8
        syndromeChkMatrix = syndrome(rCol,:) == syndromes(syndromeCol,:);       %각 block의 syndrome과 syndromes를 비교
        syndromeChk = sum(syndromeChkMatrix,'all');                   
        if(syndromeChk == size(syndrome,2))                                             
            break;
        end
    end
    syndromeChks(rCol) = syndromeCol;                                              %일치한 syndromes의 행 번호를 저장
end
    
for rCol = 1:size(rxInfo,1)                                      %correction
    if(syndromeChks(rCol) == 2)                             %syndromeChks에 저장된 syndromes의 행번호가 2라면
        if(rxInfo(rCol,6) == 1)                                  %r의 6번째 bit 변경
            rxInfo(rCol,6) = 0;
        else
            rxInfo(rCol,6) = 1;
        end
    end
    if(syndromeChks(rCol) == 3)                             %syndromeChks에 저장된 syndromes의 행번호가 3라면               
        if(rxInfo(rCol,5) == 1)                                  %r의 5번째 bit 변경
            rxInfo(rCol,5) = 0;
        else
            rxInfo(rCol,5) = 1;
        end
    end
    if(syndromeChks(rCol) == 4)                             %syndromeChks에 저장된 syndromes의 행번호가 4라면   
        if(rxInfo(rCol,4) == 1)                                  %r의 4번째 bit 변경
            rxInfo(rCol,4) = 0;
        else
            rxInfo(rCol,4) = 1;
        end
    end
    if(syndromeChks(rCol) == 8)                             %syndromeChks에 저장된 syndromes의 행번호가 8라면   
        if(rxInfo(rCol,2) == 1)                                  %r의 2,6번째 bit 변경
            rxInfo(rCol,2) = 0;
        else
            rxInfo(rCol,2) = 1;
        end
        if(rxInfo(rCol,6) == 1)
            rxInfo(rCol,6) = 0;
        else
            rxInfo(rCol,6) = 1;
        end
    end
end

rxBit = rxInfo(:,size(rxInfo,2)-size(syndrome,2)+1:size(rxInfo,2));         %모두 correction 후 r의 msg부분만 뽑아 저장
rxBit = oneRowReshape(rxBit);
end

function noisePower = snr2noisePower(snr)
    noisePower = 10^(-snr/20);
end

function crand = crandn(m,n)                                
    seed = 2016707058;                                      
    rng(seed)
    crand = randn(m,n) + 1i*randn(m,n);
end

function reshapeMatrix = oneRowReshape(matrix)
    matrix = matrix.';
    reshapeMatrix = reshape(matrix,1,[]);
end