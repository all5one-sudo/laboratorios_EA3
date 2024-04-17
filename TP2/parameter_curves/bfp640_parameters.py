import numpy as np
import skrf as rf
import matplotlib.pyplot as plt

path = 'E:\\Documentos\\GitHub\\laboratorios_EA3\\TP2\\bfp_transistor\\SPAR\\BFP640\\BFP640_VCE_'

VCE = ['1.0','1.5','2.0','2.5','3.0','3.5','4.0']
IC = ['18','22','28','32','37','42','48','50']

for vce in VCE:
    for ic in IC:
        bfp_model = rf.Network(path + vce + 'V_IC_' + ic + 'mA.s2p')
        fig, ax = plt.subplots(2, 1, figsize=(15,10))
        ax[0].grid(True)
        ax[0].set_title('Módulos parámetros S para BFP640 a Vce=' + vce + 'V e Ic=' + ic +', Diagrama de Bode')
        ax[0].set_ylabel('Magnitude [dB]')
        ax[0].set_xlabel('Frecuencia [GHz]')
        bfp_model.plot_s_db10(ax=ax[0],  logx=True)

        ax[1].grid(True)
        ax[1].set_title('Fase parámetros S para BFP640 a Vce=' + vce + 'V e Ic=' + ic +', Diagrama de Bode')
        ax[1].set_ylabel('Phase [°]')
        ax[1].set_xlabel('Frecuencia [GHz]')
        bfp_model.plot_s_deg(ax=ax[1], logx=True)

        plt.tight_layout()
        plt.savefig(vce + 'V_IC_' + ic + 'mA_bode.png')
        plt.savefig(vce + 'V_IC_' + ic + 'mA_bode.pdf')
        
        size = bfp_model.s.real.shape[0]

        lines = [
            {'marker_idx': [24,29,34,38], 'color': 'b', 'm': 0, 'n': 0, 'ntw': bfp_model},
            {'marker_idx': [24,29,34,38], 'color': 'y', 'm': 0, 'n': 1, 'ntw': bfp_model},
            {'marker_idx': [24,29,34,38], 'color': 'g', 'm': 1, 'n': 0, 'ntw': bfp_model},
            {'marker_idx': [24,29,34,38], 'color': 'r', 'm': 1, 'n': 1, 'ntw': bfp_model},
        ]

        fig, ax = plt.subplots(1, 1, figsize=(15,20))

        rf.plotting.smith(ax = ax, draw_labels = True, ref_imm = 50, chart_type = 'z')

        col_labels = ['Frequency', 'Real Imag']
        row_labels = []
        row_colors = []
        cell_text = []
        for l in lines:
            m = l['m']
            n = l['n']
            l['ntw'].plot_s_smith(m=m, n=n, ax = ax, color=l['color'])
            #plot markers
            for i, k in enumerate(l['marker_idx']):
                x = l['ntw'].s.real[k, m, n]
                y = l['ntw'].s.imag[k, m, n]
                z = l['ntw'].z[k, m, n]
                z = f'{z.real:.4f} + {z.imag:.4f}j ohm'
                f = l['ntw'].frequency.f_scaled[k]
                f_unit = l['ntw'].frequency.unit
                row_labels.append(f'M{i + 1}')
                row_colors.append(l['color'])
                ax.scatter(x, y, marker = 'v', s=20, color=l['color'])
                ax.annotate(row_labels[-1], (x, y), xytext=(-7, 7), textcoords='offset points', color=l['color'])
                cell_text.append([f'{f:.3f} {f_unit}', z])
        leg1 = ax.legend(loc="upper right", fontsize= 6)

        the_table = ax.table(cellText=cell_text,
                            colWidths=[0.4] * 2,
                            rowLabels=row_labels,
                            colLabels=col_labels,
                            rowColours=row_colors,
                            loc='bottom')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(8)
        plt.savefig(vce + 'V_IC_' + ic + 'mA_smith.png')
        plt.savefig(vce + 'V_IC_' + ic + 'mA_smith.pdf')
        plt.close()