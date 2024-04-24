clear all; close all; clc

bfp450 = sparameters('E:\Documentos\GitHub\laboratorios_EA3\TP2\bfp_transistor\SPAR\BFP450\BFP450_w_noise_VCE_1.0V_IC_0.11A.s2p');


smith(bfp450,1,1)
hold on
smith(bfp450,1,2)
hold on
smith(bfp450,2,1)
hold on
smith(bfp450,2,2)
title('BFP450 (1V, 110mA)')
%rfplot(bfp450)
%xlim([1e9 3e9])
